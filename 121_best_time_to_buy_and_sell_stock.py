from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        只能交易一次
        """
        min_price = 9999999
        max_price = 0
        res = 0

        for n in prices:
            # 如果更新了 min_price，那之前的 max_price 就不能用了
            if n < min_price:
                min_price = n
                max_price = min_price

            if n > max_price:
                max_price = n
                res = max(res, max_price - min_price)

        return res


if __name__ == "__main__":
    s = Solution()
    assert s.maxProfit([7, 6, 5, 4, 3, 1]) == 0
    assert s.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert s.maxProfit([7, 2, 6, 1, 3]) == 4
