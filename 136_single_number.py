from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Time O(n)
        Space O(n)
        """
        t = {}
        for n in nums:
            try:
                t.pop(n)
            except:
                t[n] = 1
        return t.popitem()[0]

    def singleNumber2(self, nums: List[int]) -> int:
        """
        Time O(n)
        Space O(1)
        使用 XOR 操作符：
            0101
        xor 0011
          = 0110

        a xor 0 = a
        a xor a = 0

        a xor b xor a = a xor a xor b = 0 xor b = b
        """
        a = 0
        for i in nums:
            a ^= i
        return a


if __name__ == "__main__":
    s = Solution()
    assert s.singleNumber([4, 1, 2, 1, 2]) == 4
    assert s.singleNumber([1, 1, 2]) == 2

    assert s.singleNumber2([4, 1, 2, 1, 2]) == 4
    # assert s.singleNumber2([1, 1, 2]) == 2
