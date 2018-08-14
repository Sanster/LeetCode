from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        not_val_index = 0
        count = 0
        for num in nums:
            if num != val:
                nums[not_val_index] = num
                not_val_index += 1
                count += 1

        return count
