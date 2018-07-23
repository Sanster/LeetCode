"""
https://leetcode.com/problems/roman-to-integer/description/
"""

symbols = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


class Solution:
    def romanToInt(self, s: str) -> int:
        i = 0
        total = 0
        while i < len(s):
            c = s[i]
            num = symbols[c]
            if i != (len(s) - 1):
                next_c = s[i + 1]
                if c == 'I' and next_c == 'V':
                    num = 4
                    i += 1
                if c == 'I' and next_c == 'X':
                    num = 9
                    i += 1
                if c == 'X' and next_c == 'L':
                    num = 40
                    i += 1
                if c == 'X' and next_c == 'C':
                    num = 90
                    i += 1
                if c == 'C' and next_c == 'D':
                    num = 400
                    i += 1
                if c == 'C' and next_c == 'M':
                    num = 900
                    i += 1
            i += 1

            total += num
        return total


if __name__ == '__main__':
    s = Solution()
    assert s.romanToInt("LVIII") == 58
    assert s.romanToInt("III") == 3
    assert s.romanToInt("IV") == 4
    assert s.romanToInt("IX") == 9
    assert s.romanToInt("MCMXCIV") == 1994
