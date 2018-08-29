from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        动态规划
        Time O(n)
        Space O(1)
        """
        f1 = f2 = 0
        for x in reversed(cost):
            f = x + min(f1, f2)
            f1, f2 = f, f1
        return min(f1, f2)

    def minCostClimbingStairs2(self, cost: List[int]) -> int:
        """
        等价于：在数组中每相邻两个数至少选一个，使得加起来的总和最少
        Time O(n)
        Space O(n)
        """

        # dp 用来记录 index 位置之前最小和是多少，不包含 index 位置的值
        dp = [0] * (len(cost) + 1)
        for i in range(2, len(cost) + 1):
            # 每一步可能爬一步上来 或者 爬两步上来
            dp[i] = min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1])

        return dp[-1]
