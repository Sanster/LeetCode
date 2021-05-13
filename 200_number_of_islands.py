# https://leetcode.com/problems/number-of-islands/
# https://leetcode.com/problems/number-of-islands/discuss/345981/Python3Number-of-Islands-BFS-%2B-DFS
from typing import List
from collections import deque


class Solution:
    def numIslands_space_On(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        rows = len(grid)
        cols = len(grid[0])

        visited = [[False for _ in range(cols)] for _ in range(rows)]
        count = 0

        def search(i, j):
            qu = deque([(i, j)])
            while qu:
                i, j = qu.popleft()
                if (
                    0 <= i < rows
                    and 0 <= j < cols
                    and grid[i][j] == "1"
                    and visited[i][j] == False
                ):
                    visited[i][j] = True
                    qu.extend([(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)])

        for i in range(rows):
            for j in range(cols):
                v = grid[i][j]
                if v == "1" and visited[i][j] == False:
                    count += 1
                    search(i, j)

        return count

    def numIslands_space_O1(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        count = 0

        def search(i, j):
            qu = deque([(i, j)])
            while qu:
                i, j = qu.popleft()
                if 0 <= i < rows and 0 <= j < cols and grid[i][j] == "1":
                    grid[i][j] = "0"
                    qu.extend([(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)])

        for i in range(rows):
            for j in range(cols):
                v = grid[i][j]
                if v == "1":
                    count += 1
                    search(i, j)

        return count


if __name__ == "__main__":
    s = Solution()
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    res = s.numIslands_space_O1(grid)
    assert res == 1, res

    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    res = s.numIslands_space_O1(grid)
    assert res == 3, res