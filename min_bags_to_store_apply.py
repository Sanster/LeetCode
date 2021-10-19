"""
两种袋子，一种只能装 6 个苹果，一种只能装 8 个苹果，不能小于或者大于
给定 n 个苹果，求最小能用几个袋子装。例如 n=14，可以两个袋子各用一个

如果无法装满两个袋子，例如给了 9 个，返回 -1

n>=1
"""


def min_bags(n: int) -> int:
    if n % 2 != 0:
        # 奇数肯定装不了
        return -1

    # 26
    # 3*8+2
    bag6 = -1
    bag8 = int(n / 8)  # 下取整
    rest = n - bag8 * 8
    while bag8 >= 0 and (0 < rest < 24):
        # 为什么终止条件有 < 24?
        # 24 是 6 和 8 的最小公倍数，能被6和8整除，rest 对 24 取余数的结果再之前都没命中，所以大于 24 就没必要考虑了
        if rest % 6 == 0:
            bag6 = rest / 6
            break
        bag8 -= 1
        rest = n - bag8 * 8
    print(f"n: {n}, bag8: {bag8}")
    return bag8 + bag6 if bag6 != -1 else bag8


if __name__ == "__main__":
    data = [
        (9, -1),
        (6, 1),
        (8, 1),
        (12, 2),
        (14, 2),
        (48, 6),
        (108, 14),
        (110, 14),
        (112, 14),
        (114, 15),
        (116, 15),
        (118, 15),
        (117, -1),
        (26, 4),
        (22, 3),
    ]
    for n, gt in data:
        pred = min_bags(n)
        assert pred == gt, f"n: {n}, gt: {gt}, pred: {pred}"
