from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        DP 方法
        空间复杂度太大！
        """
        max_sum = max(nums)
        sum_map = []
        for i in range(len(nums)):
            sum_map.append([0] * len(nums))

        for i in range(len(nums)):
            sum_map[i][i] = nums[i]

        for i in range(len(nums)):
            for k in range(i + 1, len(nums)):
                sum_map[i][k] = nums[k] + sum_map[i][k - 1]
                max_sum = max(sum_map[i][k], max_sum)

        return max_sum

    def maxSubArray2(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                # 相当于保存当前位置最大的连续和
                nums[i] += nums[i - 1]
        return max(nums)

    def maxSubArray3(self, nums: List[int]) -> int:
        """
        DP 方法，思路和 maxSubArray2 一样，只是另外使用了空间来保存每个位置的最大连续值
        """
        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            if dp[i - 1] > 0:
                dp[i] = nums[i] + dp[i - 1]
            else:
                dp[i] = nums[i]

        return max(dp)


if __name__ == "__main__":
    s = Solution()
    assert s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert s.maxSubArray2([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert s.maxSubArray3([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
