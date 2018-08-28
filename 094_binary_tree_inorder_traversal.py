from typing import List

from utils import TreeNode


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        out = []

        def inorder(node: TreeNode):
            if not node:
                return

            inorder(node.left)
            out.append(node.val)
            inorder(node.right)

        inorder(root)

        return out

    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        """
        迭代
        """
        out = []
        stack = []
        while len(stack) or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                out.append(node.val)
                root = node.right
        return out
