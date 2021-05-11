# https://leetcode.com/problems/squares-of-a-sorted-array/
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1

        out = [0] * len(nums)
        while l <= r:
            left = nums[l]
            right = nums[r]
            if abs(left) > abs(right):
                out[r - l] = left * left
                l += 1
            else:
                out[r - l] = right * right
                r -= 1
        return out


if __name__ == "__main__":
    s = Solution()
    nums = [-10, -1, 2, 3]
    res = s.sortedSquares(nums)
    print(res)
    assert res == [1, 4, 9, 100]