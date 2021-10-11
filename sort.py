from typing import List


def bubble_sort(nums: List[int]):
    n = len(nums)
    for j in range(n - 1):
        for i in range(n - 1 - j):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]


def quicksort(nums: List[int]):
    # time: n*log(n)
    # space: O(n)
    if len(nums) <= 1:
        return nums

    less = []
    greater = []
    base = nums[0]

    for x in nums[1:]:
        if x < base:
            less.append(x)
        else:
            greater.append(x)

    return quicksort(less) + [base] + quicksort(greater)


def quicksort_inplace(arr: List[int], left=None, right=None):
    # time: n*log(n)
    # space: O(1)
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1
    if left < right:
        partition_idx = partition(arr, left, right)
        quicksort_inplace(arr, left, partition_idx - 1)
        quicksort_inplace(arr, partition_idx + 1, right)
    return arr


def swap(arr, idx1, idx2):
    arr[idx1], arr[idx2] = arr[idx2], arr[idx1]


def partition(arr, left, right):
    # index 表示大于 pivot 第一个元素的索引
    # 最后返回 index - 1 表示主点位置
    pivot = left
    index = pivot + 1
    i = index
    while i <= right:
        if arr[i] < arr[pivot]:
            swap(arr, i, index)
            index += 1
        i += 1
    swap(arr, pivot, index - 1)
    return index - 1


if __name__ == "__main__":
    # nums = [5, 4, 3, 2, 1]
    # bubble_sort(nums)
    # print(nums)

    tests = [[1, 5, 3], [4, 2, 1, 3], [4, 2, 1, 3, 5], [-1, 5, 3, 4, 0], [], [0]]
    for it in tests:
        assert quicksort(it) == sorted(it), f"res: {quicksort(it)}, gt: {sorted(it)}"
        assert quicksort_inplace(it) == sorted(
            it
        ), f"res: {quicksort_inplace(it)}, gt: {sorted(it)}"
