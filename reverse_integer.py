"""
https://leetcode.com/problems/reverse-integer/description/
"""


class Solution:
    def reverse(self, x: int) -> int:
        # sign = -1 if x < 0 else 1
        sign = [1, -1][x < 0]
        num = sign * x
        num_str = str(num)

        out = 0
        for i in range(len(num_str))[::-1]:
            if out > (2 ** 31 - 1):
                return 0
            out += 10 ** i * int(num_str[i])

        return sign * out

    def reverse2(self, x: int) -> int:
        sign = [1, -1][x < 0]
        out = sign * int(str(abs(x))[::-1])
        return out if -(2 ** 31) - 1 < out < 2 ** 31 else 0


if __name__ == '__main__':
    s = Solution()
    assert s.reverse(123) == 321
    assert s.reverse(-123) == -321
    assert s.reverse(120) == 21
    assert s.reverse(100) == 1

    assert s.reverse(2 ** 31) == 0
    assert s.reverse(1534236496) == 0

    assert s.reverse2(123) == 321
    assert s.reverse2(-123) == -321
    assert s.reverse2(120) == 21
    assert s.reverse2(100) == 1

    assert s.reverse2(2 ** 31) == 0
    assert s.reverse(1534236496) == 0
