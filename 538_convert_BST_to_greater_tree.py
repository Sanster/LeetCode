from utils import TreeNode


class Solution:
    """
    This method for tree traversal is known as a reverse in-order traversal,
    and allows us to guarantee visitation of each node in the desired order.
    The basic idea of such a traversal is that before visiting any node in the tree,
    we must first visit all nodes with greater value. Where are all of these nodes conveniently located? In the right subtree.
    关键在于逆序，从小到大地访问树的节点
    """
    # 保存一个全局的状态
    total = 0

    def convertBST(self, root: TreeNode) -> TreeNode:
        """
        Approach 1, Recursion
        Time O(n)
        Space O(n)
        """
        if root is not None:
            # 右子树的值肯定比 root 大，所以先计算右子树的 total
            self.convertBST(root.right)
            # 更新 total 值
            self.total += root.val
            # 更新 root 值
            root.val = self.total
            # 左子树的值肯定比右子树小，右子树的 total 算好以后直接加到左子树的节点上
            self.convertBST(root.left)
        return root

    def convertBST2(self, root: TreeNode) -> TreeNode:
        """
        Approach 2: Interation with a stack
        Time O(n)
        Space O(n)
        """
        total = 0
        node = root
        stack = []

        # 最终 stack 中没有节点，node 指向左子树的中最小节点的 left child
        # 思路类似于递归的思路，先处理所有右子树的节点，再更新 total，再处理左子树
        while len(stack) != 0 or node is not None:
            # 添加所有右子树上的节点，先处理右子树上的所有节点
            while node is not None:
                stack.append(node)
                node = node.right

            node = stack.pop()
            total += node.val
            node.val = total

            # 处理左子树
            node = node.left

        return root

    def convertBST3(self, root: TreeNode) -> TreeNode:
        # TODO: understand this
        # 获得大于当前节点值，且值最小的节点
        # the smallest-value node larger than the current
        def get_successor(node: TreeNode):
            succ = node.right
            while succ.left is not None and succ.left is not node:
                succ = succ.left
            return succ

        total = 0
        node = root
        while node is not None:
            if node.right is None:
                total += node.val
                node.val = total
                node = node.left
            else:
                succ = get_successor(node)
                if succ.left is None:
                    succ.left = node
                    node = node.right
                else:
                    succ.left = None
                    total += node.val
                    node.val = total
                    node = node.left
        return root


if __name__ == "__mian__":
    s = Solution()
