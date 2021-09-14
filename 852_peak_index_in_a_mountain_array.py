from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr) - 1
        while l < r:
            m = (l + r) // 2
            if arr[m] < arr[m + 1]:
                # 中点比右侧小，还在爬坡 [2, 3, 4, 5, 4] m=2
                l = m + 1
            else:
                # 中点比右侧大，在下坡了 [1, 2, 5, 4, 3, 2, 1] m=3
                r = m
        return l

    def peakIndexInMountainArray2(self, arr: List[int]) -> int:
        # 当前位置是否比 +1 位置大，如果是则返回当前位置
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return i
        return len(arr) - 1


if __name__ == "__main__":
    s = Solution()
    data = [
        ([0, 1, 0], 1),
        ([0, 2, 1, 0], 1),
        ([0, 10, 5, 2], 1),
        ([3, 4, 5, 1], 2),
        ([3, 4, 5, 6], 3),
        ([24, 69, 100, 99, 79, 78, 67, 36, 26, 19], 2),
    ]

    for it, gt in data:
        assert s.peakIndexInMountainArray2(it) == gt

    for it, gt in data:
        assert s.peakIndexInMountainArray(it) == gt
