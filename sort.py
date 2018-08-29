from typing import List


def bubble_sort(nums: List[int]):
    n = len(nums)
    for j in range(n - 1):
        for i in range(n - 1 - j):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]


def quicksort(nums: List[int]):
    if len(nums) <= 1:
        return nums

    less = []
    greater = []
    base = nums.pop()

    for x in nums:
        if x < base:
            less.append(x)
        else:
            greater.append(x)

    return quicksort(less) + [base] + quicksort(greater)


if __name__ == '__main__':
    nums = [5, 4, 3, 2, 1]
    bubble_sort(nums)
    print(nums)

    nums = [5, 4, 3, 2, 1]
    print(quicksort(nums))
