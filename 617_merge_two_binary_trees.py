from utils import TreeNode


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        """
        Solution 1 Recursion
        Time O(m)
        Space O(m) m represents the minimum number of nodes from the two given trees
        """
        if t1 is None:
            return t2
        if t2 is None:
            return t1

        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1

    def mergeTrees2(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        """
        Solution 2: Iterative
        Time O(n)
        Space O(n) Here, nn refers to the smaller of the number of nodes in the two trees.
        """
        stack = []
        if t1 is None:
            return t2

        stack.append((t1, t2))

        while len(stack) != 0:
            t = stack.pop()
            if t[0] is None or t[1] is None:
                continue
            t[0].val += t[1].val
            if t[0].left is None:
                t[0].left = t[1].left
            else:
                stack.append((t[0].left, t[1].left))

            if t[0].right is None:
                t[0].right = t[1].right
            else:
                stack.append((t[0].right, t[1].right))

        return t1
