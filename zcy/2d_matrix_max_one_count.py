"""
二维矩阵中仅有 0 和 1 组成，且每一行中，所有 0 都在所有 1 的左边，求出包含 1 数量最多的那一行有几个 1
0000001
0000111
0000011
0011111
0111111
"""


def main(matrix) -> int:
    # 从右上角开始搜索，和 2d 矩阵搜索 II 很像
    # 1. 每一行从右往左扫，如果遇到 1: max_one_count + 1，并向左移动；否则往下一行
    max_one_count = 0
    rows = len(matrix)
    cols = len(matrix[0])

    row = 0
    col = cols - 1

    while row < rows and col >= 0:
        if matrix[row][col] == 0:
            row += 1
            continue
        else:
            max_one_count += 1
            col -= 1

    return max_one_count


if __name__ == "__main__":
    data = [
        [0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 1, 1],
        [0, 0, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1],
    ]
    assert main(data) == 6, main(data)
