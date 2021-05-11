import itertools
from typing import List

import torch
import torch.nn as nn
import torch.nn.functional as F
from icecream import ic


class TextCNN1(nn.Module):
    # 1 层 cnn，embedding 不一起训练
    def __init__(self, n_class, kernels, num_hidden):
        super().__init__()
        self.conv = nn.Conv2d(1, num_hidden, kernels)
        self.fc = nn.Linear(in_features=num_hidden, out_features=n_class)

    def forward(self, x):
        # x.shape [batch, seq_len, embed_dim]
        x = x.unsqueeze(1)  # [batch, 1, seq_len, embed_dim]
        x = self.conv(x)  # [batch, 2, seq_len-f+1, 1]
        x = F.relu(x)
        x = F.max_pool2d(x, (x.shape[-2], 1))  # [batch, 2, 1, 1]
        x = x.squeeze()  # [batch, 2]
        x = self.fc(x)  # [batch, n_class]
        return x


class TextCNN2(nn.Module):
    # 2 层 cnn，embedding 不一起训练
    def __init__(self, n_class, kernels, num_hidden=32):
        super().__init__()
        self.conv = nn.Sequential()
        for kernel in kernels:
            self.conv.add_module(f"kernel_{kernel}", nn.Conv2d(1, num_hidden, kernel))

        self.fc = nn.Linear(in_features=num_hidden * len(kernels), out_features=n_class)

    def forward(self, x):
        # x.shape [batch, seq_len, embed_dim]
        x = x.unsqueeze(1)  # [batch, 1, seq_len, embed_dim]
        pooled = []
        for conv in self.conv:
            out = conv(x)  # [batch, 2, seq_len-h_kernel+1, 1]
            out = F.relu(out)
            out = F.max_pool2d(out, (out.shape[-2], 1))  # [batch, 2, 1, 1]
            out = out.squeeze()  # [batch, 2]
            pooled.append(out)
        x = torch.cat(pooled, dim=-1)  # [batch, 6]
        x = F.dropout(x)
        x = self.fc(x)  # [batch, n_class]
        return x


def text_cnn_without_train_embedding():
    vocab = {
        "你": [0.2, 0.3, 0.4, 0.2],
        "好": [0.4, 0.2, 0.1, 0.2],
        "吗": [0.1, 0.2, 0.3, 0.4],
    }
    texts = ["你好吗", "吗好你", "你", "好", "吗", "好吗"]
    vocab_size = len(vocab)
    embed_dim = 4
    seq_len = max([len(it) for it in texts])
    n_class = len(texts)

    x = []
    for it in texts:
        _x = [[-100] * embed_dim] * seq_len
        for i, c in enumerate(it):
            _x[i] = vocab[c]
        x.append(_x)

    # [batch_size, max_seq_len, embed_dim]
    x = torch.FloatTensor(x)
    # 每个样本一类
    y = torch.LongTensor(list(range(len(texts))))

    # model = TextCNN1(kernels=[2, embed_dim], n_class=n_class, num_hidden=16)
    model = TextCNN2(
        kernels=[[2, embed_dim], [3, embed_dim]], n_class=n_class, num_hidden=16
    )
    optim = torch.optim.Adam(model.parameters(), lr=1e-2)

    for i in range(1000):
        outputs = model(x)
        optim.zero_grad()
        loss_value = F.cross_entropy(outputs, y, ignore_index=-100)
        loss_value.backward()
        optim.step()
        if i % 100 == 0:
            print(loss_value.item())


class TextCNN3(nn.Module):
    # train with embedding
    def __init__(self, vocab_size, embed_dim, h_kernels, n_class, num_hidden):
        super().__init__()
        self.embedding = nn.Embedding(
            num_embeddings=vocab_size,
            embedding_dim=embed_dim,
        )
        self.convs = nn.ModuleList(
            [nn.Conv2d(1, num_hidden, (k, embed_dim)) for k in h_kernels]
        )
        self.fc = nn.Linear(
            in_features=num_hidden * len(h_kernels), out_features=n_class
        )

    def forward(self, x):
        # x in shape: [batch, max_seq_len]
        # embedding out shape: [batch, max_seq_len, embed_dim]
        x = self.embedding(x)
        x = x.unsqueeze(1)  # [batch, 1, seq_len, embed_dim]   增加通道维度
        pooled = []
        for conv in self.convs:
            out = conv(x)  # [batch, 2, seq_len-f+1, 1]
            out = F.relu(out)
            out = F.max_pool2d(out, (out.shape[-2], 1))  # [batch, 2, 1, 1]
            out = out.squeeze()  # [batch, 2]
            pooled.append(out)
        x = torch.cat(pooled, dim=-1)  # [batch, 6]
        x = self.fc(x)  # [batch, n_class]
        return x

    def load_embedding(self, vocab):
        # vocab = [
        #     ["你", [0.2, 0.3, 0.4, 0.2]],
        #     ["好", [0.4, 0.2, 0.1, 0.2]],
        #     ["吗", [0.1, 0.2, 0.3, 0.4]],
        # ]
        for i, it in enumerate(vocab):
            self.embedding.weight.data[i] = torch.FloatTensor(it[1])


def text_cnn_train_embedding():
    vocab = [
        ["你", [0.2, 0.3, 0.4, 0.2, 0.1]],
        ["好", [0.4, 0.2, 0.1, 0.2, 0.1]],
        ["吗", [0.1, 0.2, 0.3, 0.4, 0.1]],
    ]
    vocab2idx = {it[0]: i for i, it in enumerate(vocab)}
    idx2vocab = {v: k for k, v in vocab2idx.items()}
    texts = ["你好吗你", "吗好你", "你", "好", "吗", "好吗"]
    # +1 for padding
    vocab_size = len(vocab) + 1
    PADDING_ID = len(vocab)
    embed_dim = 5
    seq_len = max([len(it) for it in texts])
    n_class = len(texts)

    def str_2_id(text, _seq_len=None) -> List[int]:
        if _seq_len is None:
            _x = [PADDING_ID] * max(len(text), seq_len)
        else:
            _x = [PADDING_ID] * _seq_len
        for i, c in enumerate(text):
            _x[i] = vocab2idx.get(c, PADDING_ID)
        return _x

    # to one-hot
    x = []
    for it in texts:
        x.append(str_2_id(it, _seq_len=seq_len))
    # [batch_size, max_seq_len]
    x = torch.LongTensor(x)
    # 每个样本一类
    y = torch.LongTensor(list(range(len(texts))))

    model = TextCNN3(
        vocab_size=vocab_size,
        embed_dim=embed_dim,
        h_kernels=[2, 3],
        n_class=n_class,
        num_hidden=16,
    )
    model.load_embedding(vocab)
    optim = torch.optim.Adam(model.parameters(), lr=1e-2)

    for i in range(1000):
        outputs = model(x)
        optim.zero_grad()
        loss_value = F.cross_entropy(outputs, y)
        loss_value.backward()
        optim.step()
        if i % 100 == 0:
            print(loss_value.item())

    model.eval()
    y = model(torch.LongTensor([str_2_id("你好吗你")]))
    print(torch.argmax(y))

    y = model(torch.LongTensor([str_2_id("好吗")]))
    print(torch.argmax(y))


if __name__ == "__main__":
    # text_cnn_without_train_embedding()
    text_cnn_train_embedding()
