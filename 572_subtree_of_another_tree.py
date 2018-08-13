from utils import TreeNode


class Solution:

    def equals(self, x: TreeNode, y: TreeNode) -> bool:
        if x is None and y is None:
            return True

        if x is None or y is None:
            return False

        return x.val == y.val and self.equals(x.left, y.left) and self.equals(x.right, y.right)

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        """
        :param s: 目标树
        :param t: 子树
        :return:
        """
        if s is None:
            return False

        return self.equals(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
