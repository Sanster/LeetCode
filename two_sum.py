"""
https://leetcode.com/problems/two-sum/description/

Approach 1: Brute Force
    Time O(n^2), Space O(1)
    暴力搜索，两层 for 循环.

Approach 2: Two-pass Hash Table
    Time O(n), Space O(n)
    先遍历一遍 nums，把数据存在 map 里，然后再循环 check。

Approach 3: One-pash Hash Table(本代码实现)
    Time O(n), Space O(n)
    遍历 nums，一边把数据存在 map 里，一边检查 map 里是否存在
"""

from typing import List


class Solution:
    def towSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for index, num in enumerate(nums):
            complement_num = target - num
            if complement_num in d.keys():
                return [d[complement_num], index]

            d[num] = index


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9

    s = Solution()
    r = s.towSum(nums, target)

    print(r)
    assert r == [0, 1]
