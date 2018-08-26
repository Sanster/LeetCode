from utils import TreeNode


class Solution(object):
    def insertIntoBST(self, root: TreeNode, val) -> TreeNode:
        if not root:
            return TreeNode(val)

        # BST 不允许相同值
        if val == root.val:
            return None

        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        elif val < root.val:
            root.left = self.insertIntoBST(root.left, val)

        return root
