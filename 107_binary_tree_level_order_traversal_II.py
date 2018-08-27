from typing import List

from utils import TreeNode


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        out = []
        nodes = []
        level = 0
        if root:
            nodes = [root]

        while len(nodes) != 0:
            queue = []
            out.append([])
            for el in nodes:
                out[level].append(el.val)
                if el.left:
                    queue.append(el.left)
                if el.right:
                    queue.append(el.right)

            nodes = queue
            level += 1

        return out[::-1]
