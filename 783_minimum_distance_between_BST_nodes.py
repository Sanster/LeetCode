from utils import TreeNode


class Solution:
    pre = None
    min_val = 999999

    def minDiffInBST(self, root: TreeNode) -> int:
        self.pre = None
        self.min_val = 999999
        self.inorder(root)
        return self.min_val

    """
    中序遍历可以得到从小到大的值，只要当前值和前一个最小的值做减法就可以了
    """

    def inorder(self, node: TreeNode):
        if not node:
            return

        self.inorder(node.left)
        if self.pre:
            self.min_val = min(self.min_val, node.val - self.pre.val)
        self.pre = node
        self.inorder(node.right)
