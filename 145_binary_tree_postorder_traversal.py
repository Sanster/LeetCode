from typing import List

from utils import TreeNode


# https://leetcode.com/problems/binary-tree-postorder-traversal/discuss/45551/Preorder-Inorder-and-Postorder-Iteratively-Summarization
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """
        迭代
        """
        out = []
        stack = []
        while len(stack) or root:
            if root:
                stack.append(root)
                out.insert(0, root.val)
                root = root.right
            else:
                node = stack.pop()
                root = node.left
        return out
