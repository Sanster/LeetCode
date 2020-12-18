from utils import run_timeit


class Solution:
    def myPow_v0(self, x: float, n: int) -> float:
        # O(n)
        y = 1
        for i in range(n):
            y *= x
        return y

    def myPow_v1(self, x: float, n: int) -> float:
        if n == 1:
            return x
        if n == 0:
            return 1.0

        if n < 0:
            n = -n
            x = 1 / x

        if n % 2 == 0:
            _y = self.myPow_v1(x, n // 2)
            y = _y * _y
        else:
            _y = self.myPow_v1(x, (n - 1) // 2)
            y = x * _y * _y

        return y

    def myPow_v2(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        y = 1
        while n:
            if n & 1:
                y *= x
            x *= x
            n = n // 2  # n = n >> 1
        return y

    def myPow_v3(self, x: float, n: int) -> float:
        # https://leetcode.com/problems/powx-n/discuss/950137/Python-bitwise-iterative
        # 10 的二进制 1010，3^10 == pow(3, 2^3) * pow(3, 2^1)
        if not n:
            return 1
        if not x:
            return 0

        x = x if n > 0 else 1 / x
        n = abs(n)

        xx = x
        ans = 1
        for i in reversed(list(bin(n)[2:])):
            if i == "1":
                ans *= xx
            xx = xx ** 2
        return ans


if __name__ == "__main__":
    s = Solution()
    assert s.myPow_v0(4, 2) == 16
    assert s.myPow_v1(4, 0) == 1
    assert s.myPow_v1(4, 2) == 16, s.myPow_v1(4, 2)
    assert s.myPow_v1(2, -10) == pow(2, -10)
    assert s.myPow_v1(4.2, 2) == pow(4.2, 2), s.myPow_v1(4.2, 2)
    assert s.myPow_v1(2, -2) == 0.25, s.myPow_v1(2, -2)

    n = pow(2, 28)
    run_timeit("v1_large", lambda: s.myPow_v1(2, n), number=1)
    run_timeit("v2_large", lambda: s.myPow_v2(2, n), number=1)
    run_timeit("buildin large", lambda: pow(2, n), number=1)

    run_timeit("v0", lambda: s.myPow_v0(8, 1000), number=1000)
    run_timeit("v1", lambda: s.myPow_v1(8, 1000), number=1000)
    run_timeit("buildin", lambda: pow(8, 1000), number=1000)
