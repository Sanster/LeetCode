"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        tmp_len = 0
        d = {}
        for i in range(len(s)):
            for c in s[i:]:
                if c in d:
                    max_len = max(max_len, tmp_len)
                    tmp_len = 0
                    d.clear()
                    break

                d[c] = c
                tmp_len += 1

        max_len = max(max_len, tmp_len)
        return max_len

    def lengthOfLongestSubstring2(self, s: str) -> int:
        max_len = 0
        d = {}
        substr_start = 0
        for j in range(len(s)):
            if s[j] in d:
                # substr_start = max(d[s[j]], substr_start)
                # 更新 start 的位置
                substr_start = d[s[j]]
            max_len = max(max_len, j - substr_start + 1)
            # 记录下最新出现的每一个字符的位置
            d[s[j]] = j + 1
        return max_len


if __name__ == '__main__':
    s = Solution()
    assert s.lengthOfLongestSubstring('abcabcbb') == 3
    assert s.lengthOfLongestSubstring('bbbbb') == 1
    assert s.lengthOfLongestSubstring('pwwkew') == 3
    assert s.lengthOfLongestSubstring('') == 0
    assert s.lengthOfLongestSubstring('c') == 1
    assert s.lengthOfLongestSubstring('abcdefg') == 7
    assert s.lengthOfLongestSubstring('dvedf') == 4

    assert s.lengthOfLongestSubstring2('abcabcbb') == 3
    assert s.lengthOfLongestSubstring2('bbbbb') == 1
    assert s.lengthOfLongestSubstring2('pwwkew') == 3
    assert s.lengthOfLongestSubstring2('') == 0
    assert s.lengthOfLongestSubstring2('c') == 1
    assert s.lengthOfLongestSubstring2('abcdefg') == 7
    assert s.lengthOfLongestSubstring2('dvedf') == 4
