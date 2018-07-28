"""
https://leetcode.com/problems/longest-palindromic-substring/description/
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Time O(n^2)
        Space O(n^2)
        """
        ans = ''
        max_len = 0
        n = len(s)
        # 初始化存放中间结果的空间
        DP = [[0] * n for _ in range(n)]

        # 所有单个字符都认为是回文
        for i in range(n):
            DP[i][i] = True
            max_len = 1
            ans = s[i]

        # 所有两个相同的字符都认为是回文
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                DP[i][i + 1] = True
                ans = s[i:i + 2]
                max_len = 2

        for j in range(n):
            for i in range(0, j - 1):
                # 如果 DP 的某个元素是回文，并且该元素左右两侧的字符相同，则认为依然是回文
                if s[i] == s[j] and DP[i + 1][j - 1]:
                    DP[i][j] = True
                    if max_len < j - i + 1:
                        ans = s[i:j + 1]
                        max_len = j - i + 1
        return ans

    def longestPalindrome2(self, s: str) -> str:
        """
        Time: O(n)
        Space: O(1)
        """
        end = 0
        start = 0
        for i in range(len(s)):
            # 对于回文字符数是奇数的情况
            len1 = self.expandAroundCenter(s, i, i)
            # 对于回文字符数是偶数的情况
            len2 = self.expandAroundCenter(s, i, i + 1)
            max_len = max(len1, len2)
            if max_len > (end - start):
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        return s[start: end + 1]

    def expandAroundCenter(self, s: str, left: int, right: int) -> int:
        # 从中间开始像两边
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome('babad'))
    print(s.longestPalindrome('aabad'))
    print(s.longestPalindrome('cbbd'))

    print(s.longestPalindrome2('babad'))
    print(s.longestPalindrome2('aabad'))
    print(s.longestPalindrome2('cbbd'))
