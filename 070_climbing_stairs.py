"""
https://leetcode.com/problems/climbing-stairs/
"""

class Solution:
    d = {}

    def climbStairs(self, n: int) -> int:
        """
        递归，使用 memorization
        Time: O(n)
        Space: O(n)
        """
        if n in self.d.keys():
            return self.d[n]

        if n == 1:
            return 1
        if n == 2:
            return 2

        ways = 0

        ways += self.climbStairs(n - 1)
        ways += self.climbStairs(n - 2)

        self.d[n] = ways

        return ways

    def climbStairs2(self, n: int) -> int:
        """
        DP
        Time O(n)
        Space O(n)
        """
        if n == 1:
            return 1
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]

    def climbStairs3(self, n: int) -> int:
        """
        优化 DP，不需要保存所有的状态，只要保存前两步就可以了
        Time O(n)
        Space O(1)

        假设 n=5，则爬梯子的方法数可以是从 n=4 的地方走 1 步，或者从 n=3 的地方走 1 步(两格)
        """
        if n == 1:
            return 1
        if n == 2:
            return 2

        prev = 1
        prev_prev = 2
        out = prev + prev_prev

        for _ in range(2, n):
            out = prev + prev_prev
            prev = prev_prev
            prev_prev = out

        return out


if __name__ == "__main__":
    s = Solution()
    assert s.climbStairs(2) == 2
    assert s.climbStairs(3) == 3
    assert s.climbStairs(4) == 5
    # assert s.climbStairs(1000) == 5

    assert s.climbStairs2(2) == 2
    assert s.climbStairs2(3) == 3
    assert s.climbStairs2(4) == 5
    # assert s.climbStairs2(1000) == 5

    assert s.climbStairs3(2) == 2
    assert s.climbStairs3(3) == 3
    assert s.climbStairs3(4) == 5
