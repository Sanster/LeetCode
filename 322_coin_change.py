from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        # f(11) = min(f(11-1), f(11-2), f(11-5)+1
        # ...
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        print(dp)
        if dp[amount] == amount + 1:
            return -1

        return dp[amount]

    def coinChange2(self, coins: List[int], amount: int) -> int:
        # Time: O()
        # Space: O()
        cache = {}

        def dp(_amount):
            if _amount == 0:
                return 0

            if _amount < 0:
                return -1

            min_count = float("inf")
            for coin in coins:
                remain = _amount - coin
                if remain in cache:
                    count = cache[remain]
                else:
                    count = dp(remain)
                    cache[remain] = count

                if 0 <= count < min_count:
                    min_count = count + 1
            return min_count if min_count != float("inf") else -1

        return dp(amount)


if __name__ == "__main__":
    s = Solution()
    a = s.coinChange2([1, 2, 5], 11)
    print(a)

    a = s.coinChange([1, 2, 5], 11)
    print(a)
