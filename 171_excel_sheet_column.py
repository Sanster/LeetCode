class Solution:
    def titleToNumber(self, s: str) -> int:
        """看成 26 进制转换成 10 进制"""
        res = 0
        for i, c in enumerate(reversed(s)):
            res += 26 ** i * (ord(c) - ord('A') + 1)
        return res


if __name__ == '__main__':
    s = Solution()
    assert s.titleToNumber("A") == 1
    assert s.titleToNumber("Z") == 26
    assert s.titleToNumber("AA") == 27
    assert s.titleToNumber("AB") == 28
    assert s.titleToNumber("ZY") == 701
