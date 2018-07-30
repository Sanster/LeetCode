from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        d = set(nums)
        out = []
        max_num = len(nums) + 1
        for num in range(1, max_num):
            if num not in d:
                out.append(num)

        return out

    def findDisappearedNumbers2(self, nums: List[int]) -> List[int]:
        for i, num in enumerate(nums):
            index = abs(num) - 1
            if index < len(nums):
                # 对应 index 处的数字设为负数，表示已经存在了
                nums[index] = -abs(nums[index])

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]


if __name__ == '__main__':
    s = Solution()
    print(s.findDisappearedNumbers([1, 3, 5, 6, 7]))
    print(s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
    print(s.findDisappearedNumbers([]))
    print(s.findDisappearedNumbers([1]))
    print(s.findDisappearedNumbers([1, 3]))
    print(s.findDisappearedNumbers([1, 1]))

    print("*" * 20)
    print(s.findDisappearedNumbers2([1, 3, 5, 6, 7]))
    print(s.findDisappearedNumbers2([4, 3, 2, 7, 8, 2, 3, 1]))
    print(s.findDisappearedNumbers2([]))
    print(s.findDisappearedNumbers2([1]))
    print(s.findDisappearedNumbers2([1, 3]))
    print(s.findDisappearedNumbers2([1, 1]))
