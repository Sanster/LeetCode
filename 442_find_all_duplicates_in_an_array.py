from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        must without extra space and in O(n) time
        https://www.geeksforgeeks.org/find-duplicates-in-on-time-and-constant-extra-space/
        """
        out = []
        for n in nums:
            index = abs(n) - 1
            if nums[index] < 0:
                out.append(abs(n))
            else:
                # 以正负号作为标志位
                nums[index] *= -1

        return out


if __name__ == "__main__":
    s = Solution()
    print(s.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))

    print(s.findDuplicates([5, 4, 6, 7, 9, 3, 10, 9, 5, 6]))
