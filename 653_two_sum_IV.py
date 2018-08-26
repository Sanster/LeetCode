from utils import TreeNode


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False

        d = {}
        nodes = [root]
        while len(nodes):
            queue = []
            for n in nodes:
                num_to_plus = k - n.val
                if num_to_plus in d.keys():
                    return True
                else:
                    d[n.val] = num_to_plus

                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)

            nodes = queue

        return False
