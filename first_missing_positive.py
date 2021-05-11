from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 1. for any array whose length is l, the first missing positive must be in range [1,...,l+1],
        #         so we only have to care about those elements in this range and remove the rest.
        # 2. we can use the array index as the hash to restore the frequency of each number within
        #      the range [1,...,l+1]

        # useful when input is [1, 2, 3]
        nums.append(0)

        for i, n in enumerate(nums):
            if n >= len(nums) or n < 0:
                nums[i] = 0

        n = len(nums)
        for i in range(
            len(nums)
        ):  # use the index as the hash to record the frequency of each number
            nums[nums[i] % n] += n
        print(nums)

        for i in range(1, len(nums)):
            if nums[i] / n == 0:
                return i

        return n

    def run(self, nums):
        nums.append(0)
        n = len(nums)
        for i in range(len(nums)):  # delete those useless elements
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0
        for i in range(len(nums)):  # use the index as the hash to record the frequency of each number
            nums[nums[i] % n] += n
        for i in range(1, len(nums)):
            if nums[i] / n == 0:
                return i
        return n


if __name__ == "__main__":
    s = Solution()
    # print(s.firstMissingPositive([1, 2, 3]))
    print(s.run([3,4,1,-1]))
