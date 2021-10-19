from random import randint
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(l, r):
            # l,r 都包含
            ri = randint(l, r)
            print(ri)
            # ri 值移动到最右侧
            nums[r], nums[ri] = nums[ri], nums[r]
            # enumerate(..., l) 表示返回的索引从 l 开始
            # 注意要 r+1
            for i, v in enumerate(nums[l : r + 1], l):
                if v >= nums[r]:
                    # 数组从左开始为大于 ri 值的值
                    # l 记录大于区域的右边界
                    # 当 i == r 时，相当于把原来放到最右边的 ri 移动到了中间
                    nums[l], nums[i] = nums[i], nums[l]
                    l += 1
            return l - 1

        l, r = 0, len(nums) - 1
        # 把 k 的含义变成索引
        k = k - 1
        while True:
            # 表示第 pos 位置为 top(pos+1) 大的数
            pos = partition(l, r)
            if pos < k:
                # 表示 ri 选到了一个比较大的数
                # pos 前的数不够取 top k
                l = pos + 1
            elif pos > k:
                # 表示 ri 选到了一个比较小的数
                # pos 前的数超过了 top k
                r = pos - 1
            else:
                return nums[pos]

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k - 1]


if __name__ == "__main__":
    s = Solution()
    # nums = [3, 2, 1, 5, 6, 4], k = 2
    data = [
        ([3, 2, 1, 5, 6, 4], 2),
        ([1, 2, 3, 4], 1),
        ([1], 1),
    ]
    for nums, k in data:
        pred = s.findKthLargest(nums, k)
        gt = s.findKthLargest2(nums, k)
        assert pred == gt, f"nums:{nums} gt: {gt}, pred: {pred}"
