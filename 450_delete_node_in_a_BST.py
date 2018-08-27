from utils import TreeNode


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        """
        如果 node.val == key，分三种情况
        1. 如果 node 是叶子节点, 直接令 node = None
        2. 如果 node 只有一个子节点，则把子节点移动到当前节点替换
        3. 如果 node 有两个子节点，则用 right 的最小节点替换当前节点
        """
        if not root:
            return None

        if key < root.val:
            # 递归左侧
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            # 递归右侧
            root.right = self.deleteNode(root.right, key)
        else:
            # 当 node.val == key
            # 本身就包含了 root.left == root.right == None 的情况
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                min_node = self.findMin(root.right)
                root.val = min_node.val
                root.right = self.deleteNode(root.right, min_node.val)
        return root

    def findMin(self, root: TreeNode) -> TreeNode:
        while root.left:
            root = root.left
        return root
