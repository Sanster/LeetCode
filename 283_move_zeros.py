from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]):
        """
        Time O(n)
        Space O(n)
        """
        res = []

        # 循环一次找出所有非 0 值
        for n in nums:
            if n != 0:
                res.append(n)

        # 补充 0 值
        for i in range(len(nums) - len(res)):
            res.append(0)

        # 给 nums 赋值
        for i in range(len(nums)):
            nums[i] = res[i]

    def moveZeros2(self, nums: List[int]):
        """
        把原问题转换成：讲所有非 0 元素梵高
        Time O(n)
        Space O(1)
        """
        lastNoneZeroIndex = 0





if __name__ == "__main__":
    s = Solution()

    nums = [0, 1, 0, 3, 12]
    s.moveZeroes(nums)
    assert nums == [1, 3, 12, 0, 0]

    nums = [0, 1, 0, 0, 0]
    s.moveZeroes(nums)
    assert nums == [1, 0, 0, 0, 0]

    nums = [0]
    s.moveZeroes(nums)
    assert nums == [0]

    nums = [1, 2, 3, 4]
    s.moveZeroes(nums)
    assert nums == [1, 2, 3, 4]

    nums = []
    s.moveZeroes(nums)
    assert nums == []

    nums = [0, 0, 1]
    s.moveZeroes(nums)
    assert nums == [1, 0, 0]
