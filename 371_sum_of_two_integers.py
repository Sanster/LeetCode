class Solution:
    # https://leetcode.com/problems/sum-of-two-integers/discuss/84282/Python-solution-with-no-%22+-*%22-completely-bit-manipulation-guaranteed
    def getSum(self, a: int, b: int) -> int:
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        while b != 0:
            # TODO: why?
            # ^ get different bits and & gets double 1s, << moves carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= MAX else ~(a ^ mask)


if __name__ == "__main__":
    s = Solution()
    assert s.getSum(1, 3) == 4
    assert s.getSum(1, 0) == 1
    assert s.getSum(0, 0) == 0
    assert s.getSum(11, 34) == 45
    assert s.getSum(1, -3) == -2
    assert s.getSum(-1, -3) == -4
