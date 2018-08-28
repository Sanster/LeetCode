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
