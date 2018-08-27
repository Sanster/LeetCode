from utils import TreeNode


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0

        if root.left and root.left.left is None and root.left.right is None:
            left_sum = root.left.val
        else:
            left_sum = self.sumOfLeftLeaves(root.left) if root.left else 0

        right_sum = self.sumOfLeftLeaves(root.right) if root.right else 0

        return left_sum + right_sum
