"""
https://leetcode.com/problems/valid-parentheses/description/
"""


class Solution:
    def isValid(self, s: str) -> bool:
        """
        Time:  O(n)
        Space: O(n)
        """
        stack = []
        opens = ['(', '[', '{']
        closes = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for c in s:
            if c in opens:
                stack.append(c)
            else:
                if len(stack) == 0 or closes[c] != stack.pop():
                    return False

        return len(stack) == 0


if __name__ == '__main__':
    s = Solution()
    assert s.isValid("()") == True
    assert s.isValid("()[]{}") == True
    assert s.isValid("(]") == False
    assert s.isValid("([)]") == False
    assert s.isValid("]") == False
    assert s.isValid(")") == False
    assert s.isValid("{[]}") == True
    assert s.isValid("") == True
    assert s.isValid("[") == False
