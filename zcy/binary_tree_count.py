# 给定一个非负整数 n，代表二叉树的节点个数。返回能形成多少种不同的二叉树结构


def main(n: int) -> int:
    if n == 0:
        return 1
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for left_count in range(i):
            dp[i] += dp[left_count] * dp[i - 1 - left_count]
    return dp[n]


data = [
    (0, 1),  # 空树也算一种
    (1, 1),
    (2, 2),
    (3, 5),
    (4, 14),
]

for n, gt in data:
    assert main(n) == gt, f"n:{n} gt: {gt} pred: {main(n)}"
