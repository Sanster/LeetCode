"""
https://leetcode.com/problems/palindrome-number/description/

判断是否为回文
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        if x % 10 == 0:
            return False

        x_str = str(x)
        reversed_x_str = x_str[::-1]
        if x_str == reversed_x_str:
            return True
        else:
            return False

    def isPalindrome2(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

    def isPalindrome3(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        if x % 10 == 0:
            return False

        sum = 0
        num = x
        while num > 0:
            sum = sum * 10 + num % 10
            num = num // 10
        return x == sum


if __name__ == '__main__':
    s = Solution()
    assert s.isPalindrome(121) is True
    assert s.isPalindrome(1221) is True
    assert s.isPalindrome(101) is True
    assert s.isPalindrome(10) is False
    assert s.isPalindrome(-123) is False

    assert s.isPalindrome2(121) is True
    assert s.isPalindrome2(1221) is True
    assert s.isPalindrome2(101) is True
    assert s.isPalindrome2(10) is False
    assert s.isPalindrome2(-123) is False

    assert s.isPalindrome3(121) is True
    assert s.isPalindrome3(1221) is True
    assert s.isPalindrome3(101) is True
    assert s.isPalindrome3(10) is False
    assert s.isPalindrome3(-123) is False

