from utils import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """
        类似获得 tree 的最大深度，采用递归，递归过程中保存最大的 path 路径（即左子树的深度加上右子树的深度）
        Time O(n)
        Space O(n)
        """
        res = 1

        def depth(node: TreeNode) -> int:
            # 使得子函数中可以修改父函数中的变量
            nonlocal res

            if node is None:
                return 0

            left_depth = depth(node.left)
            right_depth = depth(node.right)
            res = max(res, left_depth + right_depth + 1)
            return max(left_depth, right_depth) + 1

        depth(root)
        return res - 1
