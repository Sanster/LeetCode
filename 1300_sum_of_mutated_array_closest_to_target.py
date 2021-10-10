# https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/
import math
from typing import List


class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort(reverse=True)
        max_arr = arr[0]
        """
        arr[-1] 表示排好序的数组中最小的数，如果选择了该数 arr_sum 还是比 target 小的话，
        说明 array 的和与 target 还有缩小的空间，此时换成选倒数第二小的值，arr_sum 会增大
        可能更接近 target
        如果选定了目标值(arr[-1]) 后 arr_sum 比 target 大，则返回 round(target / len(arr)) 的结果
        """
        while len(arr) > 0 and target >= arr[-1] * len(arr):
            target -= arr.pop()

        if len(arr) > 0:
            # 为什么要减 0.0001？使返回的值偏小，例如 4,9,3 选 4 或 3 都和 target 差是 1
            return int(round((target - 0.0001) / len(arr)))
        else:
            return max_arr


if __name__ == "__main__":
    data = [
        ([1, 2, 3], 10, 3),
        ([1, 2, 3], 3, 1),
        ([5, 6, 8], 3, 1),
        ([4, 9, 3], 10, 3),
        ([2, 3, 5], 10, 5),
        ([60864, 25176, 27249, 21296, 20204], 56803, 11361),
    ]
    for arr, target, gt in data:
        _arr = arr.copy()
        assert (
            Solution().findBestValue(arr, target) == gt
        ), f"arr: {_arr} pred: {Solution().findBestValue(_arr, target)} gt: {gt}"
