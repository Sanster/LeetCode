from utils import TreeNode


class Solution:
    def averageOfLevels(self, root: TreeNode):
        """
        BFS 广度优先搜索
        """
        out = []
        level = [root] if root else []
        while len(level) != 0:
            queue = []
            # 把一层的所有 node 和 leaf 加到 queue 里
            # 如果是最后一层，则 queue 为空
            level_sum = 0
            level_count = len(level)
            for el in level:
                level_sum += el.val
                if el.left:
                    queue.append(el.left)
                if el.right:
                    queue.append(el.right)
            out.append(level_sum / level_count)
            level = queue

        return out
