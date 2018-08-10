from utils import TreeNode


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        """
        迭代
        """
        if root is None:
            return True

        nodes = [root]

        while len(nodes) != 0:
            queue = []
            not_none_count = 0
            for n in nodes:
                if n:
                    if n.left:
                        not_none_count += 1
                    if n.right:
                        not_none_count += 1

                    queue.append(n.left)
                    queue.append(n.right)

            if not_none_count % 2 != 0:
                return False

            mid = int(len(queue) / 2)
            last = len(queue) - 1
            for i in range(mid):
                if queue[i] and queue[last - i]:
                    if queue[i].val != queue[last - i].val:
                        return False
                elif queue[i] is None and queue[last - i] is None:
                    pass
                else:
                    return False

            nodes = queue

        return True

    def isSymmetric2(self, root: TreeNode) -> bool:
        """
        递归： 想象一棵树在照镜子
        Time O(n) 会遍历一遍每个 node，所以是 n
        Space O(n) 空间占用是递归栈的深度，最差的情况树是竖直的，所以与包含的节点个数相同
        """

        def isMirror(t1: TreeNode, t2: TreeNode) -> bool:
            if t1 is None and t2 is None:
                return True
            if t1 is None or t2 is None:
                return False

            return t1.val == t2.val and isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)

        return isMirror(root, root)

    def isSymmetric3(self, root: TreeNode) -> bool:
        """
        迭代，也想象成一棵树在照镜子
        每次向 queue 中添加一个 tuple，位于树中的镜像位置
        Time O(n)
        Space O(n)
        """
        q = []
        q.append((root, root))
        while len(q) != 0:
            t1, t2 = q.pop(0)

            if t1 is None and t2 is None:
                continue

            if t1 is None or t2 is None:
                return False

            if t1.val != t2.val:
                return False

            q.append((t1.left, t2.right))
            q.append((t1.right, t2.left))

        return True
