import math


class Solution:
    def mySqrt(self, x):
        """
        :param x:
        :return:
        """
        l, r = 0, x
        while l <= r:
            # Python int 类型无上限，不用担心 r+l 会溢出
            # 其它语言可以写成 mid = l + (r - l) // 2
            mid = (r + l) // 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif x < mid * mid:
                r = mid
            else:
                l = mid

    def mySqrt2(self, x):
        r = x
        while r * r > x:
            r = (r + x / r) // 2

        return int(r)


if __name__ == "__main__":
    s = Solution()
    assert s.mySqrt(4) == 2
    assert s.mySqrt(8) == 2
    assert s.mySqrt(0) == 0
    assert s.mySqrt(9) == 3

    assert s.mySqrt2(4) == 2
    assert s.mySqrt2(8) == 2
    assert s.mySqrt2(0) == 0
    assert s.mySqrt2(9) == 3
    assert s.mySqrt2(1283948) == 1133
