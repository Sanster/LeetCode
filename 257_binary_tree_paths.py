from typing import List

from utils import TreeNode


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        res, stack = [], [(root, "")]

        while stack:
            node, ls = stack.pop()
            if not node.left and not node.right:
                res.append(ls + str(node.val))

            if node.right:
                stack.append((node.right, ls + str(node.val) + "->"))

            if node.left:
                stack.append((node.left, ls + str(node.val) + "->"))

        return res
