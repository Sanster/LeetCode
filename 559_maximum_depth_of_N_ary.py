"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """

        depth = 0
        level = [root] if root else []
        while len(level) != 0:
            depth += 1
            queue = []
            # 把一层的所有 node 和 leaf 加到 queue 里
            # 如果是最后一层，则 queue 为空
            for el in level:
                queue.extend(el.children)
            level = queue

        return depth
