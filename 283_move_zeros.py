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

    def moveZeroes2(self, nums: List[int]):
        """
        把原问题转换成：将所有非 0 元素移动到数组的开头，并且保持原来的顺序
        Time O(n)
        Space O(1)
        """

        # 通过一个指针来记录从哪个 index 开始后面都是 0
        lastNoneZeroIndex = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastNoneZeroIndex] = nums[i]
                lastNoneZeroIndex += 1

        for i in range(lastNoneZeroIndex, len(nums)):
            nums[i] = 0

    def moveZeroes3(self, nums: List[int]):
        """
        最优。操作数为非 0 元素的个数
        Time O(n)
        Space(1)
        """
        lastNoneZeroIndex = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                # 直接交换 0 和非 0 值
                nums[lastNoneZeroIndex], nums[i] = nums[i], nums[lastNoneZeroIndex]
                lastNoneZeroIndex += 1


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

    nums = [0, 1, 0, 3, 12]
    s.moveZeroes2(nums)
    assert nums == [1, 3, 12, 0, 0]

    nums = [0, 1, 0, 0, 0]
    s.moveZeroes2(nums)
    assert nums == [1, 0, 0, 0, 0]

    nums = [0]
    s.moveZeroes2(nums)
    assert nums == [0]

    nums = [1, 2, 3, 4]
    s.moveZeroes2(nums)
    assert nums == [1, 2, 3, 4]

    nums = []
    s.moveZeroes2(nums)
    assert nums == []

    nums = [0, 0, 1]
    s.moveZeroes2(nums)
    assert nums == [1, 0, 0]

    nums = [0, 1, 0, 3, 12]
    s.moveZeroes3(nums)
    assert nums == [1, 3, 12, 0, 0]

    nums = [0, 1, 0, 0, 0]
    s.moveZeroes3(nums)
    assert nums == [1, 0, 0, 0, 0]

    nums = [0]
    s.moveZeroes3(nums)
    assert nums == [0]

    nums = [1, 2, 3, 4]
    s.moveZeroes3(nums)
    assert nums == [1, 2, 3, 4]

    nums = []
    s.moveZeroes3(nums)
    assert nums == []

    nums = [0, 0, 1]
    s.moveZeroes3(nums)
    assert nums == [1, 0, 0]
