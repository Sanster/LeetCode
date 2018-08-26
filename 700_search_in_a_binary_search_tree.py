from utils import TreeNode


class Solution(object):
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None

        if val == root.val:
            return root
        elif val > root.val:
            return self.searchBST(root.right, val)
        elif val < root.val:
            return self.searchBST(root.left, val)
