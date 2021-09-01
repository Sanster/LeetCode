from typing import List


def merge(sorted_list1: List[int], sorted_list2: List[int]):
    # time: O(n)
    # space: O(n)
    i = j = 0
    out = []
    while i < len(sorted_list1) and j < len(sorted_list2):
        if sorted_list1[i] < sorted_list2[j]:
            out.append(sorted_list1[i])
            i += 1
        else:
            out.append(sorted_list2[j])
            j += 1

    if i != len(sorted_list1):
        out.extend(sorted_list1[i:])
    if j != len(sorted_list2):
        out.extend(sorted_list2[j:])
    return out


def merge_sort(arr: List[int]):
    if len(arr) <= 1:
        return arr

    # split
    list1 = arr[: len(arr) // 2]
    list2 = arr[len(list1) :]

    sorted_list1 = merge_sort(list1)
    sorted_list2 = merge_sort(list2)

    return merge(sorted_list1, sorted_list2)


def merge_sort_iter(arr: List[int]):
    pass


if __name__ == "__main__":
    tests = [[4, 2, 1, 3], [4, 2, 1, 3, 5], [-1, 5, 3, 4, 0], [], [0]]

    for it in tests:
        assert merge_sort(it) == sorted(it)
