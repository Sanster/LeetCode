from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        """
        暴力搜索，时间复杂度太高
        Time O(n^3)
        """
        for i in range(len(nums) - 2):
            for k in range(i + 2, len(nums)):
                if nums[i] >= nums[k]:
                    continue
                for j in range(i + 1, k):
                    if nums[k] < nums[j]:
                        return True

        return False

    def find132pattern2(self, nums: List[int]) -> bool:
        """
        Time O(n^2)
        """

        min_i = 99999999999
        for j in range(len(nums) - 1):
            # i 的具体位置不重要，只要 nums[i] < nums[j] 就可以了
            # 以 min_i 作为 nums[i]
            min_i = min(min_i, nums[j])
            if min_i == nums[j]:
                continue

            for k in range(j + 1, len(nums)):
                if min_i < nums[k] < nums[j]:
                    return True

        return False

    def find132pattern3(self, nums: List[int]) -> bool:
        """
        https://leetcode.com/problems/132-pattern/discuss/94081/10-line-Python-Solution
        Time O(n)
        Stack
        TODO: understand this
        http://www.cnblogs.com/grandyang/p/6081984.html
        """
        stack = []
        num3 = -9999999999
        for n in nums[::-1]:
            if n < num3:
                return True
            while stack and stack[-1] < n:
                num3 = stack.pop()
            stack.append(n)
        return False


if __name__ == "__main__":
    s = Solution()
    assert s.find132pattern([]) == False
    assert s.find132pattern([1]) == False
    assert s.find132pattern([1, 2]) == False
    assert s.find132pattern([1, 2, 3]) == False
    assert s.find132pattern([1, 3, 2]) == True
    assert s.find132pattern([1, 2, 3, 4]) == False
    assert s.find132pattern([3, 1, 4, 2]) == True
    assert s.find132pattern([-1, 3, 2, 0]) == True
    assert s.find132pattern([1, 0, 1, -4, -3]) == False

    assert s.find132pattern2([1, 0, 1, -4, -3]) == False
    assert s.find132pattern2([]) == False
    assert s.find132pattern2([1]) == False
    assert s.find132pattern2([1, 2]) == False
    assert s.find132pattern2([1, 2, 3]) == False
    assert s.find132pattern2([1, 3, 2]) == True
    assert s.find132pattern2([1, 2, 3, 4]) == False
    assert s.find132pattern2([3, 1, 4, 2]) == True
    assert s.find132pattern2([-1, 3, 2, 0]) == True
