# 一个有序数组，求元素平方后不重复的元素个数，例如[-10, -10, -5, 0, 1, 5, 8, 10]
# 要利用上「有序」这个条件，时间复杂度 O(n)

from typing import List


class Solution:
    def uniqueSquares(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        last_max_abs = abs(nums[0])
        count = 1
        while l <= r:
            left = abs(nums[l])
            right = abs(nums[r])
            if left >= right:
                if left != last_max_abs:
                    count += 1
                    last_max_abs = left
                l += 1
            else:
                if right != last_max_abs:
                    count += 1
                    last_max_abs = right
                r -= 1
        return count


if __name__ == "__main__":
    s = Solution()
    nums = [-10, -10, -5, 0, 1, 5, 8, 10]
    res = s.uniqueSquares(nums)
    assert res == 5, res

    nums = [-10, -10]
    res = s.uniqueSquares(nums)
    assert res == 1, res

    nums = [-10]
    res = s.uniqueSquares(nums)
    assert res == 1, res

    nums = [-10, 9]
    res = s.uniqueSquares(nums)
    assert res == 2, res