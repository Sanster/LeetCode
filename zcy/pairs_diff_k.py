# 给定一个数组 arr，求差值为 k 的去重数字对。例如 (0,2)  (2,0) 是重复的数字对
from typing import List


def main(arr: List[int], k: int) -> int:
    # 已近去重，可以防止出现重复数字对
    nums = set(arr)

    count = 0
    for it in nums:
        # 和 it 的差值为 k 的数可能是 it-k 或者 it+k
        # 这里只使用 it+k 可以防止出现 (0,2)  (2,0) 这种重复数字对的情况
        if it + k in nums:
            count += 1
    return count


if __name__ == "__main__":
    data = [((5, 2, 3, 7, 0, 0), 2, 3)]
    for arr, k, gt in data:
        assert main(arr, k) == gt
