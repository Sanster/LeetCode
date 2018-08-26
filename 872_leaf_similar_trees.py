from typing import List

from utils import TreeNode


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 and not root2:
            return True

        seq1 = self.findLeaf(root1)
        seq2 = self.findLeaf(root2)

        return seq1 == seq2

    def findLeaf(self, root: TreeNode) -> List[int]:
        if root.left is None and root.right is None:
            return [root.val]

        leftLeafs = self.findLeaf(root.left) if root.left is not None else []
        rightLeafs = self.findLeaf(root.right) if root.right is not None else []

        leftLeafs.extend(rightLeafs)
        return leftLeafs
