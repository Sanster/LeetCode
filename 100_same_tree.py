from utils import TreeNode


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """
        迭代
        """
        if p is None and q is not None:
            return False
        if q is None and p is not None:
            return False
        if q is None and p is None:
            return True

        p_nodes = [p]
        q_nodes = [q]

        while len(p_nodes) != 0 and len(q_nodes) != 0:
            if len(p_nodes) != len(q_nodes):
                return False

            tmp_p_nodes = []
            tmp_q_nodes = []
            for i in range(len(p_nodes)):
                if p_nodes[i] is None and q_nodes[i] is None:
                    continue

                if p_nodes[i] is None and q_nodes[i] is not None:
                    return False

                if p_nodes[i] is not None and q_nodes[i] is None:
                    return False

                if p_nodes[i].val != q_nodes[i].val:
                    return False

                tmp_p_nodes.append(p_nodes[i].left)
                tmp_p_nodes.append(p_nodes[i].right)

                tmp_q_nodes.append(q_nodes[i].left)
                tmp_q_nodes.append(q_nodes[i].right)

            p_nodes = tmp_p_nodes
            q_nodes = tmp_q_nodes

        return True

    def isSameTree2(self, p: TreeNode, q: TreeNode) -> bool:
        """
        递归
        """
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q
