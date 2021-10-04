# https://leetcode.com/problems/maximum-average-subarray-i/
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        # 第一位 0 是为了计算方便
        sums = [0] * (n + 1)
        for i in range(1, n + 1):
            sums[i] = sums[i - 1] + nums[i - 1]

        res = float("-inf")
        for i in range(k, n + 1):
            new_res = sums[i] - sums[i - k]
            if new_res > res:
                res = new_res

        return res / k


if __name__ == "__main__":
    data = [
        ([1, 12, -5, -6, 50, 3], 4, 12.75000),
        ([5], 1, 5.0),
        ([1, 2], 1, 2.0),
        ([1, 2], 2, 1.5),
        ([1, 1], 2, 1),
        ([1, 1], 1, 1),
    ]
    for nums, k, gt in data:
        assert (
            Solution().findMaxAverage(nums, k) == gt
        ), f"{Solution().findMaxAverage(nums, k)}, gt: {gt}"
