from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        没有用到数组原先的排序
        """
        for j, i in enumerate(range(m, m + n)):
            nums1[i] = nums2[j]
        nums1.sort()

    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        从后往前比较
        """
        while m > 0 and n > 0:
            if nums1[m - 1] < nums2[n - 1]:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
            else:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1

        while n > 0:
            nums1[n - 1] = nums2[n - 1]
            n -= 1


if __name__ == "__main__":
    s = Solution()

    a = [1, 2, 3, 0, 0, 0]
    m = 3
    b = [2, 5, 6]
    n = 3

    s.merge2(a, m, b, n)
    print(a)

    a = [1]
    m = 1
    b = []
    n = 0

    s.merge2(a, m, b, n)
    print(a)
