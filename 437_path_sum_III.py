from typing import List, Set

from utils import TreeNode, createBTree


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        # https://leetcode.com/problems/path-sum-iii/discuss/141424/Python-step-by-step-walk-through.-Easy-to-understand.-Two-solutions-comparison.-%3A-)
        if root is None:
            return 0
        self.result = 0
        self.cache = {0: 1}

        self.dfs(root, 0, sum)

        return self.result

    def dfs(self, node: TreeNode, currentPathSum, target: int):
        if node is None:
            return

        currentPathSum += node.val
        oldPathSum_to_find = currentPathSum - target
        self.result += self.cache.get(oldPathSum_to_find, 0)
        self.cache[currentPathSum] = self.cache.get(currentPathSum, 0) + 1

        self.dfs(node.left, currentPathSum, target)
        self.dfs(node.right, currentPathSum, target)

        # 当前节点和他的左右节点都判断好了，不需要这个 currPathSum 了
        self.cache[currentPathSum] -= 1


if __name__ == "__main__":
    s = Solution()
    v = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
    tree = createBTree(v)

    print(s.pathSum(tree, 8))

    assert s.pathSum(tree, 8) == 3
