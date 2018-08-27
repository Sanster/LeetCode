from typing import List

from utils import TreeNode

"""
一张很棒的图片
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34579/Python-short-recursive-solution./32947
"""


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        preorder 的第一个元素肯定是 root，
        找到 root 在 inorder 中的位置，就可以将 inorder 的输入分成 left 和 right
        """
        if len(preorder) != len(inorder):
            return None
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        root_index = inorder.index(root.val)

        left_inorder = inorder[:root_index + 1]
        right_inorder = inorder[root_index + 1:]

        left_preorder = preorder[1: len(left_inorder) + 1]
        right_preorder = preorder[len(left_inorder) + 1:]

        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)

        return root
