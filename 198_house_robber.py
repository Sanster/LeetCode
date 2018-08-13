from typing import List


class Solution:
    # Base Case: nums[0] = nums[0]
    # nums[1] = max(nums[0], nums[1])
    # 重点！
    # nums[k] = max(k + nums[k-2], nums[k-1])

    def rob(self, nums: List[int]) -> int:
        """
        Time O(n)
        """
        prev = curr = 0

        for num in nums:
            temp = prev  # This represents the nums[i-2]th value
            prev = curr  # This represents the nums[i-1]th value
            curr = max(num + temp, prev)  # Here we just plug into the formula

        return curr

    def rob2(self, nums: List[int]) -> int:
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

        for i in range(2, len(nums)):
            # nums[i] + dp[i-2] 代表抢劫这座房子
            # dp[i-1] 代表不抢劫这坐房子
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        return dp[-1]

    def rob3(self, nums: List[int]) -> int:
        """
        DP 方法，不用保存所有状态，只保存前两个
        Time O(n)
        Space O(1)
        """
        rob = 0  # max monney can get if rob current house
        notrob = 0  # max money can get if not rob current house

        for i in range(len(nums)):
            # if rob current value, previous house must not be robbed
            currob = notrob + nums[i]

            # if not rob ith house, take the max value of robbed (i-1)th house and not rob (i-1)th house
            notrob = max(notrob, rob)

            rob = currob

        return max(rob, notrob)


if __name__ == "__main__":
    s = Solution()
    assert s.rob([1, 2, 3, 1]) == 4
    assert s.rob([2, 1, 1, 2]) == 4
    assert s.rob([2, 7, 9, 3, 1]) == 12
    assert s.rob([2, 7, 9, 12, 1]) == 19
    assert s.rob([2, 3, 9, 12, 1]) == 15

    assert s.rob2([1, 2, 3, 1]) == 4
    assert s.rob2([2, 1, 1, 2]) == 4
    assert s.rob2([2, 7, 9, 3, 1]) == 12
    assert s.rob2([2, 7, 9, 12, 1]) == 19
    assert s.rob2([2, 3, 9, 12, 1]) == 15

    assert s.rob3([1, 2, 3, 1]) == 4
    assert s.rob3([2, 1, 1, 2]) == 4
    assert s.rob3([2, 7, 9, 3, 1]) == 12
    assert s.rob3([2, 7, 9, 12, 1]) == 19
    assert s.rob3([2, 3, 9, 12, 1]) == 15
