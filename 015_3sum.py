from collections import defaultdict
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums) - 2):
            # 重要防止出现重复的结果
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                tmp_sum = nums[i] + nums[l] + nums[r]
                if tmp_sum == 0:
                    result.append([nums[i], nums[l], nums[r]])

                    # 重要防止出现重复的结果
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1

                    # 因为已经等于 0 了，所以只移动一个不会再等于0
                    l += 1
                    r -= 1

                if tmp_sum < 0:
                    l += 1

                if tmp_sum > 0:
                    r -= 1

        return result

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        lookup = defaultdict(int)
        for n in nums:
            lookup[n] += 1

        if 0 in lookup and lookup[0] > 2:
            res = [[0, 0, 0]]
        else:
            res = []

        pos = [p for p in lookup if p > 0]
        neg = [n for n in lookup if n < 0]

        for p in pos:
            for n in neg:
                # 由 i + p + n=0 变换而来
                i = -p - n
                if i not in lookup:
                    continue
                if i == 0 and lookup[i] > 0:
                    res.append([n, 0, p])
                elif i == p and lookup[i] > 1:
                    res.append([n, p, p])
                elif i == n and lookup[i] > 1:
                    res.append([n, n, p])
                elif i > p:
                    res.append([n, p, i])
                elif i < n:
                    res.append([i, n, p])

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))
