from utils import TreeNode


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """
        递归
        :param root:
        :return:
        """
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepth2(self, root: TreeNode) -> int:
        """
        BFS 广度优先搜索
        """
        depth = 0
        level = [root] if root else []
        while len(level) != 0:
            depth += 1
            queue = []
            # 把一层的所有 node 和 leaf 加到 queue 里
            # 如果是最后一层，则 queue 为空
            for el in level:
                if el.left:
                    queue.append(el.left)
                if el.right:
                    queue.append(el.right)
            level = queue

        return depth


if __name__ == "__main__":
    s = Solution()
    # s.maxDepth()
