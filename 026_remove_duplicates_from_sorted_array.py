from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        length = 1
        min_val = nums[0]
        for i, num in enumerate(nums[1:]):
            if num != min_val:
                min_val = num
                nums[length] = min_val
                length += 1
        return length


if __name__ == '__main__':
    s = Solution()

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    assert s.removeDuplicates(nums) == 5
    print(nums)

    nums = [1, 1, 2]
    assert s.removeDuplicates(nums) == 2
    print(nums)
