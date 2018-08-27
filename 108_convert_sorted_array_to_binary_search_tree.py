from typing import List

from utils import TreeNode

"""
Height balanced BST：每个 node 的两颗子树的高度差不能超过 1
"""


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        """
        :param nums: 从小大大排好序了
        """
        if not nums or not len(nums):
            return None

        if len(nums) == 1:
            return TreeNode(nums[0])

        mid = (0 + len(nums)) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
