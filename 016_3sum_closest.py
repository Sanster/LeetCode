from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        Time O(n^2)
        重点要先排好序
        """
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                tmp_sum = nums[i] + nums[j] + nums[k]
                if tmp_sum == target:
                    return tmp_sum

                if abs(tmp_sum - target) < abs(result - target):
                    result = tmp_sum

                if tmp_sum < target:
                    j += 1

                if tmp_sum > target:
                    k -= 1

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.threeSumClosest([-1, 2, 1, -4], 1))
