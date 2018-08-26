from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        # 相当于于一个指针，用于记录有效的长度
        cur_length = 1
        min_val = nums[0]
        for i, num in enumerate(nums[1:]):
            if num != min_val:
                min_val = num
                nums[cur_length] = min_val
                cur_length += 1
        return cur_length


if __name__ == '__main__':
    s = Solution()

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    assert s.removeDuplicates(nums) == 5
    print(nums)

    nums = [1, 1, 2]
    assert s.removeDuplicates(nums) == 2
    print(nums)
