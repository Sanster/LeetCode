from typing import List


class Solution:
    # TODO
    def rob(self, nums: List[int]) -> int:
        """
        DP 方法
        Time O(n)
        Space O(n)
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        first_included = False
        for i in range(2, len(nums)):
            # nums[i] + dp[i-2] 代表抢劫这座房子
            # dp[i-1] 代表不抢劫这坐房子
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        return dp[-1]


if __name__ == "__main__":
    s = Solution()
    assert s.rob([2, 3, 2]) == 3
    assert s.rob([1, 2, 3, 1]) == 4
