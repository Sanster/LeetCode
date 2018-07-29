from collections import defaultdict, Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for n in nums:
            d[n] += 1

        return max(d.items(), key=lambda x: x[1])[0]

    def majorityElement2(self, nums: List[int]) -> int:
        counter = Counter(nums)

        return counter.most_common(1)[0][0]

    def majorityElement3(self, nums: List[int]) -> int:
        # Approach 6: Boyer-Moore Voting Algorithm
        # http://www.cs.utexas.edu/~moore/best-ideas/mjrty/example.html
        # https://blog.csdn.net/chfe007/article/details/42919017
        """
        Time O(n)
        Space O(1)
        """

        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            # +1 和 -1 的步骤相当于每次从数组中查出一对元素，并「删除」
            # 不难证明，如果存在元素 e 出现次数超过半数，那最后剩下的只有 e
            count += (1 if num == candidate else -1)
        return candidate


if __name__ == "__main__":
    s = Solution()
    assert s.majorityElement([2, 2, 3]) == 2
    assert s.majorityElement([2, 1, 1, 1, 1, 2, 2]) == 1

    assert s.majorityElement2([2, 1, 1, 1, 1, 2, 2]) == 1

    assert s.majorityElement3([2, 1, 1, 1, 1, 2, 2]) == 1
    assert s.majorityElement3([2, 2, 3]) == 2
