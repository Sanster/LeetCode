from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        def is_peak(index):
            if index == 0:
                if nums[0] > nums[1]:
                    return True
            if index == len(nums) - 1:
                if nums[-1] > nums[-2]:
                    return True

            return nums[index] > nums[index - 1] and nums[index] > nums[index + 1]

        l = 0
        r = len(nums) - 1
        while r > l:
            m = (r + l) // 2
            if is_peak(l):
                return l
            if is_peak(r):
                return r
            if is_peak(m):
                return m

            if nums[l] < nums[l + 1] and nums[m] < nums[m - 1]:
                r = m - 1
                continue

            if nums[r] < nums[r - 1] and nums[m] < nums[m + 1]:
                l = m + 1
                continue

        return 0


if __name__ == "__main__":
    s = Solution()

    data = [
        ([1, 2, 3, 1], 2),
        ([1, 2, 1, 3, 5, 6, 4], 5),
    ]
    for arr, gt in data:
        assert s.findPeakElement(arr)
