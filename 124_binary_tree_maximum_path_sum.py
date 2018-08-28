from utils import TreeNode
import math

class Solution:
    maxValue = float('-inf')

    def maxPathSum(self, root: TreeNode) -> int:
        self.maxPathDown(root)
        return int(self.maxValue)

    def maxPathDown(self, node: TreeNode):
        if not node:
            return 0

        left = max(0, self.maxPathDown(node.left))
        right = max(0, self.maxPathDown(node.right))

        self.maxValue = max(self.maxValue, left + right + node.val)

        return max(left, right) + node.val
