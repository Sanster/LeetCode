from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # https://github.com/grandyang/leetcode/issues/518
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            # 为什么要从 coin 开始：如果 money 比 coin 小，那就无法用 coin 拼起来
            for money in range(coin, amount + 1):
                # change2 的空间优化改进
                # dp[i][j] = dp[i - 1][j] + (j >= coins[i - 1] ? dp[i][j - coins[i - 1]]: 0)
                # dp[i[[j] 只依赖于 dp[i - 1][j] 和 dp[i][j - coins[i - 1]]
                # dp[money] 等价于 dp[i-1][j]，即上一"行"的 dp 结果
                # dp[money - coin] 等价于 dp[i][j - coins[i - 1]]
                dp[money] = dp[money] + dp[money - coin]
        return dp[amount]

    def change2(self, amount: int, coins: List[int]) -> int:
        # amount 的组合方式可以分为两部分，以 amount==5, coins=[1,2] 为例
        # amount 组合的一部分可以全由 1 组成，如 1+1+1+1+1
        # 另一部分为有 2 参与，即 [1,2] 组成，那么组合里肯定有 2，所以相当于是转换成 amount=(5-2)=3 时，由 [1,2] 组成
        # 有几种方法，f(3) 也可以由同样的规律求出，dp[i][j] 表示用当前 i 个硬币组成钱数为 j 的不同种组合方法
        # dp[i - 1][j] 表示当前金额去掉一个硬币的组合方法数量
        # dp[i][j - coins[i - 1]] 表示当前金额减掉一个 coin 值后的组合方法

        # dp[i][j] = dp[i - 1][j] + (j >= coins[i - 1] ? dp[i][j - coins[i - 1]]: 0)

        # f2(5) = f(3) = 2 + 1
        # f2(5) = f(3) = 1 + 1 + 1
        # 5 = 1 + 1 + 1 + 1 + 1

        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
        # TODO: 初始化为什么是 1？
        dp[0][0] = 1
        for i in range(1, len(coins) + 1):
            # TODO: 初始化为什么是 1？
            dp[i][0] = 1
            for j in range(1, amount + 1):
                part2 = dp[i][j - coins[i - 1]] if j >= coins[i - 1] else 0
                dp[i][j] = dp[i - 1][j] + part2

        return dp[-1][-1]


if __name__ == "__main__":
    s = Solution()
    a = s.change(5, [2, 1, 5])
    print(a)

    a = s.change2(5, [2, 1, 5])
    print(a)

    a = s.change2(3, [2])
    print(a)
