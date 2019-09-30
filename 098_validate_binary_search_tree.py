from collections import deque

from utils import TreeNode, createBTree


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True

        return self._helper(root, float('-inf'), float('inf'))

    def _helper(self, root: TreeNode, min_val, max_val) -> bool:
        if root is None:
            return True

        if root.left and (root.val <= root.left.val or root.left.val <= min_val):
            return False

        if root.right and (root.val >= root.right.val or root.right.val >= max_val):
            return False

        left_res = self._helper(root.left, min_val, root.val)
        right_res = self._helper(root.right, root.val, max_val)

        return left_res and right_res

    def isValidBST2(self, root: TreeNode) -> bool:
        stack = []
        node = tree
        prev = None
        while node or stack:
            # 把所有节点的左子树 append 进去
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()

            if node.val is not None:
                if prev is None:
                    prev = node.val
                else:
                    if node.val <= prev:
                        return False
                    prev = node.val

            node = node.right
        return True


if __name__ == "__main__":
    s = Solution()
    a = [2, 1, 3]
    tree = createBTree(a)
    assert s.isValidBST(tree) == True
    assert s.isValidBST2(tree) == True

    a = [5, 1, 4, None, None, 3, 6]
    tree = createBTree(a)
    assert s.isValidBST(tree) == False
    assert s.isValidBST2(tree) == False
