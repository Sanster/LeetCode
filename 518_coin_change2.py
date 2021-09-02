from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # https://github.com/grandyang/leetcode/issues/518
        # 5 = 5
        # 5 = 2 + 2 + 1
        # 5 = 2 + 1 + 1 + 1
        # 5 = 1 + 1 + 1 + 1 + 1

        # +1 是为了初始状态
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            # TODO: 加注释
            # 为什么要从 coin 开始：如果 money 比 coin 小，那就无法用 coin 拼起来
            for money in range(coin, amount + 1):
                dp[money] += dp[money - coin]
        return dp[amount]


if __name__ == "__main__":
    s = Solution()
    a = s.change(5, [2, 1, 5])
    print(a)
