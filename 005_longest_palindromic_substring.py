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


if __name__ == '__main__':
    s = Solution()
    # print(s.longestPalindrome('babad'))
    # print(s.longestPalindrome('aabad'))
    print(s.longestPalindrome('cbbd'))
