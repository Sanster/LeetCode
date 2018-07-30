from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Time O(n)
        """
        if target < nums[0]:
            return 0

        for i, num in enumerate(nums):
            if num == target:
                return i

            if i < len(nums) - 1:
                if nums[i] < target < nums[i + 1]:
                    return i + 1

        return len(nums)

    def searchInsert2(self, nums: List[int], target: int) -> int:
        """
        Time O(n)
        """
        for i, num in enumerate(nums):
            if num >= target:
                return i

        return len(nums)

    def searchInsert3(self, nums: List[int], target: int) -> int:
        """Time O(log_n)"""
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                start = mid + 1

            if nums[mid] > target:
                end = mid - 1

        return start


if __name__ == "__main__":
    s = Solution()
    assert s.searchInsert([1, 3, 5, 6], 7) == 4
    assert s.searchInsert([1, 3, 5, 6], 5) == 2
    assert s.searchInsert([1, 3, 5, 6], 2) == 1
    assert s.searchInsert([1, 3, 5, 6], 0) == 0
    assert s.searchInsert([1, 2, 6, 8], 4) == 2

    assert s.searchInsert2([1, 3, 5, 6], 7) == 4
    assert s.searchInsert2([1, 3, 5, 6], 5) == 2
    assert s.searchInsert2([1, 3, 5, 6], 2) == 1
    assert s.searchInsert2([1, 3, 5, 6], 0) == 0
    assert s.searchInsert2([1, 2, 6, 8], 4) == 2

    assert s.searchInsert3([1, 3, 5, 6], 7) == 4
    assert s.searchInsert3([1, 3, 5, 6], 5) == 2
    assert s.searchInsert3([1, 3, 5, 6], 2) == 1
    assert s.searchInsert3([1, 3, 5, 6], 0) == 0
    assert s.searchInsert3([1, 2, 6, 8], 4) == 2
    assert s.searchInsert3([], 1) == 0
