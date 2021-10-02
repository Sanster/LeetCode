from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 1. 找到 peak 点
        # 2. 根据 peak 点分两段，在某一段里找 target

        l = 0
        r = len(nums) - 1

        peak = 0
        while l < r:
            if nums[0] < nums[-1]:
                break
            mid = (l + r) // 2
            """
            mid = 3 
            
            4 5 6 7 0 1 2
            nums[mid] = 7
            nums[mid] > nums[mid+1]
            """
            if nums[mid] > nums[mid + 1]:
                peak = mid + 1
                break

            """
            4 5 6 0 1 2 3
            nums[mid] = 0
            nums[mid] < nums[mid-1]
            """
            if nums[mid] < nums[mid - 1]:
                peak = mid
                break

            """
            5 6 0 1 2 3 4
            nums[mid] = 1
            nums[mid-1] < nums[mid] < nums[mid+1]
            """
            if nums[mid] < nums[l]:
                r = mid
                continue

            """
            2 3 4 5 6 0 1
            nums[mid] = 5
            nums[mid-1] < nums[mid] < nums[mid+1]
            """
            if nums[mid] > nums[r]:
                l = mid + 1

        print(f"find peak: {target}, {peak}")
        if target <= nums[-1]:
            l = peak
            r = len(nums) - 1
        else:
            l = 0
            r = peak - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                r = mid
            if nums[mid] < target:
                l = mid + 1

        if nums[l] == target:
            return l
        if nums[r] == target:
            return r

        return -1


if __name__ == "__main__":
    s = Solution()
    data = [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 0, -1),
        ([1], 1, 0),
        ([1, 3, 5], 0, -1),
        ([4, 5, 6, 7, 0, 1, 2], 2, 6),
    ]
    for nums, target, gt in data:
        assert s.search(nums, target) == gt, f"{s.search(nums, target)}, {gt}"
