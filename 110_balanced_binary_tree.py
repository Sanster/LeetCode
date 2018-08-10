from utils import TreeNode


class Solution:

    def depth(self, node: TreeNode) -> int:
        if not node:
            return 0

        return 1 + max(self.depth(node.left), self.depth(node.right))

    def isBalanced(self, root: TreeNode) -> bool:
        """
        Top to down solution
        Time O(n^2) O(nlogn)?
        """
        if root is None:
            return True

        left_depth = self.depth(root.left)
        right_depth = self.depth(root.right)
        return abs(left_depth - right_depth) <= 1 and self.isBalanced(root.right) and self.isBalanced(root.left)

    def isBalanced2(self, root: TreeNode) -> bool:
        """
        Down to top solution
        DFS 从最下层开始计算左右子树的深度，不平衡则返回 -1 作为标记
        """
        return self.dfsHeight(root) != -1

    def dfsHeight(self, root: TreeNode) -> int:
        if root is None:
            return 0

        left = self.dfsHeight(root.left)
        if left == -1:
            return -1

        right = self.dfsHeight(root.right)
        if right == -1:
            return -1

        if abs(left - right) > 1:
            return -1
        else:
            return max(left, right) + 1
