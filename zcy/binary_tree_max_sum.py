# 二叉树每个结点都有一个int型权值，给定一棵二叉树，要求计算出从根结点到叶结点的所有路径中，权值和最大的值为多少
from typing import Optional

from utils import createBTree, TreeNode


def main(root: Optional[TreeNode]) -> int:
    # 递归
    if root is None:
        return 0
    res = root.val
    return res + max(main(root.left), main(root.right))


def main2(root: Optional[TreeNode]) -> int:
    # 节点值一路累加，记录在 pre_sum 中
    val = 0

    def f(node: TreeNode, pre_sum: int):
        nonlocal val
        if node.left is None and node.right is None:
            val = max(node.val + pre_sum, val)
            return

        if node.left is not None:
            f(node.left, pre_sum + node.val)
        if node.right is not None:
            f(node.right, pre_sum + node.val)

    f(root, 0)
    return val


if __name__ == "__main__":
    data = [[2, 1, 3, 2, 4, None, 5]]
    for it in data:
        assert main(createBTree(it)) == 10
        assert main2(createBTree(it)) == 10, main2(createBTree(it))
