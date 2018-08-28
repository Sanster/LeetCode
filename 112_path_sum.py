from utils import TreeNode


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        if not root.right and not root.left:
            if root.val == sum:
                return True

        res = False
        if root.left:
            res = self.hasPathSum(root.left, sum - root.val)

        if res:
            return True

        if root.right:
            res = self.hasPathSum(root.right, sum - root.val)

        return res
