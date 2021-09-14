import math
from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people) - 1
        count = 0
        while l <= r:
            if people[l] + people[r] <= limit:
                count += 1
                l += 1
                r -= 1
            else:
                # 如果最胖的人和最瘦的人都不能做一船，那 r 位置的人肯定只能一人一船
                r -= 1
                count += 1

        return count

    def numRescueBoats2(self, people: List[int], limit: int) -> int:
        """
        1. 排序
        2. 找到 <= limit/2 最右的位置，例如  1,2,2,3,4,  limit=4，要取第二个2
        3. L==m，m 右边一位为 R，使用左边的去和右边的凑小于 limit 的对
        4. 左侧没凑成功的数量除以 2 上取整，右侧没凑成功的数量直接加到最后结果中(因为没有符合 < limit 条件的可以凑的数了)
        """
        people.sort()
        m_val = limit / 2
        m = 0

        for i, it in enumerate(people):
            if it <= m_val:
                m = i
            elif it > m_val:
                break

        L = m
        R = m + 1
        left_not_match = 0
        match = 0
        # 两种情况
        # 左侧先消耗完
        # 右侧先消耗完
        while L >= 0 and R <= len(people) - 1:
            if people[L] + people[R] <= limit:
                L -= 1
                R += 1
                match += 1
            else:
                left_not_match += 1
                L -= 1

        R_not_match = len(people) - R
        L_not_match = left_not_match + L + 1 if L > 0 else left_not_match
        count = math.ceil(L_not_match / 2) + match + R_not_match
        return count


if __name__ == "__main__":
    s = Solution()
    data = [
        {"weights": [1, 2], "limit": 3, "output": 1},
        {"weights": [2, 2], "limit": 6, "output": 1},
        {"weights": [5, 1, 4, 2], "limit": 6, "output": 2},
        {"weights": [3, 2, 2, 1], "limit": 3, "output": 3},
        {"weights": [3, 5, 3, 4], "limit": 5, "output": 4},
        {"weights": [3, 2, 3, 2, 2], "limit": 6, "output": 3},
    ]
    for it in data:
        val = s.numRescueBoats(it["weights"], it["limit"])
        assert val == it["output"], f"in: {it['weights']} ret: {val} gt: {it['output']}"

        val = s.numRescueBoats2(it["weights"], it["limit"])
        assert val == it["output"], f"in: {it['weights']} ret: {val} gt: {it['output']}"
