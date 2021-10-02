# https://leetcode.com/problems/search-a-2d-matrix-ii/
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        target = 4

        1  2  3  [7]
        3  5  8  9
        4  5  7  8
        ------------
        1  2  [3]  7
        3  5  8  9
        4  5  7  8
        ------------
        1  2  3  7
        3  5  [8]  9
        4  5  7  8
        ------------
        1  2  3  7
        3  [5]  8  9
        4  5  7  8
        ------------
        1  2  3  7
        [3]  5  8  9
        4  5  7  8
        ------------
        1  2  3  7
        3  5  8  9
        [4]  5  7  8

        """

        # 从右上角开始搜索
        rows = len(matrix)
        cols = len(matrix[0])

        row = 0
        col = cols - 1

        while row < rows and col >= 0:
            if matrix[row][col] > target:
                col -= 1
            elif matrix[row][col] < target:
                row += 1
            else:
                return True
        return False


if __name__ == "__main__":
    s = Solution()
    data = (
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True),
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False),
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 16, True),
        ([[1], [2], [3], [4]], 6, False),
        ([[1], [2], [3], [4]], 2, True),
        ([[0]], 1, False),
        ([[1]], 1, True),
    )
    for matrix, target, gt in data:
        assert s.searchMatrix(matrix, target) == gt
    pass
