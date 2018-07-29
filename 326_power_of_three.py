import sys


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False

        while n % 3 == 0:
            n = n // 3

        return n == 1

    def isPowerOfThere(self, n: int) -> bool:
        # 假设输入的 n 为 int32，则 1162261467 应该是 3 的 pow 的最大值
        return n > 0 and 1162261467 % n == 0

    def findMax3Power(self):
        i = 0
        a = 0
        while True:
            b = pow(3, i)

            if b > 2 ** 31 - 1:
                break

            a = b
            i += 1

        print(a)


if __name__ == '__main__':
    s = Solution()
    assert s.isPowerOfThree(45) == False
    assert s.isPowerOfThree(27) == True
    assert s.isPowerOfThree(0) == False
    assert s.isPowerOfThree(9) == True

    # print(sys.maxsize)
    s.findMax3Power()
