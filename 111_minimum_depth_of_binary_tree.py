from utils import TreeNode


class Solution(object):
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        depth = 0
        nodes = [root]
        while len(nodes):
            depth += 1
            queue = []
            for n in nodes:
                if not n.left and not n.right:
                    return depth

                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)

            nodes = queue

        return 0
