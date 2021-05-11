import numpy as np
from matplotlib import pyplot
import matplotlib.pyplot as plt
import random


class KMeans(object):
    # k是分组数；tolerance‘中心点误差’；max_iter是迭代次数
    def __init__(self, k=2, tolerance=0.0001, max_iter=300):
        self.k_ = k
        self.tolerance_ = tolerance
        self.max_iter_ = max_iter

    def fit(self, data):
        self.centers_ = {}
        for i in range(self.k_):
            self.centers_[i] = data[i]

        for i in range(self.max_iter_):
            self.clf_ = {}
            for i in range(self.k_):
                self.clf_[i] = []
            # print("质点:",self.centers_)
            for feature in data:
                # distances = [np.linalg.norm(feature-self.centers[center]) for center in self.centers]
                distances = []
                for center in self.centers_:
                    # 欧拉距离
                    # np.sqrt(np.sum((features-self.centers_[center])**2))
                    distances.append(np.linalg.norm(feature - self.centers_[center]))
                classification = distances.index(min(distances))
                self.clf_[classification].append(feature)

            # print("分组情况:",self.clf_)
            prev_centers = dict(self.centers_)
            for c in self.clf_:
                self.centers_[c] = np.average(self.clf_[c], axis=0)

            # '中心点'是否在误差范围
            optimized = True
            for center in self.centers_:
                org_centers = prev_centers[center]
                cur_centers = self.centers_[center]
                if np.sum((cur_centers - org_centers) / org_centers) > self.tolerance_:
                    optimized = False
            if optimized:
                break

    def predict(self, p_data):
        distances = [
            np.linalg.norm(p_data - self.centers_[center]) for center in self.centers_
        ]
        index = distances.index(min(distances))
        return index


def kmeans1():
    x = np.array([[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]])
    kmeans = KMeans(k=2)
    kmeans.fit(x)

    print(kmeans.centers_)
    for center in kmeans.centers_:
        pyplot.scatter(
            kmeans.centers_[center][0], kmeans.centers_[center][1], marker="*", s=150
        )

    for cat in kmeans.clf_:
        for point in kmeans.clf_[cat]:
            pyplot.scatter(point[0], point[1], c=("r" if cat == 0 else "b"))

    predict = [[2, 1], [6, 9]]
    for feature in predict:
        cat = kmeans.predict(predict)
        pyplot.scatter(feature[0], feature[1], c=("r" if cat == 0 else "b"), marker="x")

    pyplot.show()


def distance(x, y):
    """欧式距离
    input:
        x: shape=(n_samples, n_features)
        y: shape=(k, n_features)
    output:
        z: shape=(n_smaples, k)
    """
    # shape=(n_samples, k, n_features)
    z = np.expand_dims(x, axis=1) - y
    z = np.square(z)
    z = np.sqrt(np.sum(z, axis=2))
    return z


def k_means(data, k, max_iter, tolerance):
    data = np.asarray(data, dtype=np.float32)
    n_samples, n_features = data.shape
    # 随机初始化簇中心
    indices = random.sample(range(n_samples), k)
    center = np.copy(data[indices])
    cluster = np.zeros(data.shape[0], dtype=np.int32)
    i = 1
    while i <= max_iter:
        dis = distance(data, center)
        # 样本新的所属簇
        cluster = np.argmin(dis, axis=1)
        onehot = np.zeros(n_samples * k, dtype=np.float32)
        onehot[cluster + np.arange(n_samples) * k] = 1.0
        onehot = np.reshape(onehot, (n_samples, k))
        # 以矩阵相乘的形式均值化簇中心
        # (n_samples, k)^T * (n_samples, n_features) = (k, n_features)
        new_center = np.matmul(np.transpose(onehot, (1, 0)), data)
        new_center = new_center / np.expand_dims(np.sum(onehot, axis=0), axis=1)

        diff = np.linalg.norm(center - new_center)
        if diff <= tolerance:
            print(f"stop by tolerance, diff is: {diff}. new_center: {new_center} center: {center}")
            return cluster, center

        center = new_center
        i += 1
    return cluster, center


def scatter_cluster(data, cluster, center):
    if data.shape[1] != 2:
        raise ValueError("Only can scatter 2d data!")
    # 画样本点
    plt.scatter(data[:, 0], data[:, 1], c=cluster, alpha=0.8)
    mark = ["r*", "b*", "g*"]
    # 画质心点
    print(center.shape[0])
    for i in range(center.shape[0]):
        plt.plot(center[i, 0], center[i, 1], mark[i], markersize=20)
    plt.show()


def kmenas2():
    n_samples = 500
    n_features = 2
    k = 3
    data = np.random.randn(n_samples, n_features)
    cluster, center = k_means(data, k, max_iter=20, tolerance=0.0001)

    scatter_cluster(data, cluster, center)


if __name__ == "__main__":
    # kmeans1()
    kmenas2()
