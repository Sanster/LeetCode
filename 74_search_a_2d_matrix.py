# https://leetcode.com/problems/search-a-2d-matrix/
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        1   2   3   4
        5   6   7   8
        9   10  11  12

        mid_index=5
        mid_val=5

        target=10 -> l = mid_index + 1
        target=2 -> r = mid_index  -> mid_index = (0+5)//2 = 2

        Time O(log(m*n))
        Space O(1)
        """
        if len(matrix) == 0:
            return False
        if len(matrix[0]) == 0:
            return False

        l = 0
        r = len(matrix) * len(matrix[0]) - 1
        while l < r:
            mid = (l + r) // 2
            mid_val = self.get_val(matrix, mid)
            if mid_val == target:
                return True

            if mid_val < target:
                l = mid + 1
            elif mid_val > target:
                r = mid

        if self.get_val(matrix, l) == target or self.get_val(matrix, r) == target:
            return True

        return False

    def get_val(self, matrix: List[List[int]], index: int):
        """
        1   2   3   4
        5   6   7   8
        9   10  11  12

        rows = 3
        cols = 4
        index = 6

        col = 6 % 4 = 2
        row = 6 // 4 = 1
        """
        rows = len(matrix)
        cols = len(matrix[0])
        col = index % cols
        row = index // cols
        val = matrix[row][col]
        return val


if __name__ == "__main__":
    s = Solution()
    data = (
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True),
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False),
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 16, True),
        ([[1], [2], [3], [4]], 6, False),
        ([[1], [2], [3], [4]], 2, True),
        ([], 1, False),
        ([[0]], 1, False),
        ([[1]], 1, True),
    )
    for matrix, target, gt in data:
        assert s.searchMatrix(matrix, target) == gt
