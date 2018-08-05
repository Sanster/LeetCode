from utils import TreeNode


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """
        递归
        Time O(n)
        Space O(n)
        """
        if root is None:
            return root

        if root.left is None and root.right is None:
            return root

        root.left, root.right = root.right, root.left
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)
        return root

    def inverTree2(self, root: TreeNode) -> TreeNode:
        """
        迭代，类似广度优先搜索
        """

        if root is None:
            return None

        queue = [root]
        while len(queue) != 0:
            current = queue.pop(0)
            current.left, current.right = current.right, current.left

            if current.left is not None:
                queue.append(current.left)

            if current.right is not None:
                queue.append(current.right)
        return root
