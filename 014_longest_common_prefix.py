"""
https://leetcode.com/problems/longest-common-prefix/description/
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''

        min_len = len(min(strs, key=lambda x: len(x)))

        out = ''
        for k in range(min_len):
            same = True
            for s in strs[1:]:
                if strs[0][k] != s[k]:
                    same = False

            if same:
                out += strs[0][k]
            else:
                return out

        return out

    def longestCommonPrefix2(self, strs: List[str]) -> str:
        """
        Time:  O(n * k), k is the length of the common prefix
        Space: O(1)
        """
        if not strs:
            return ""

        for i in range(len(strs[0])):
            for string in strs[1:]:
                if i >= len(string) or string[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]


if __name__ == '__main__':
    s = Solution()
    assert s.longestCommonPrefix(["flower", "flow", "flight"]) == 'fl'
    assert s.longestCommonPrefix(["dog", "racecar", "car"]) == ''
    assert s.longestCommonPrefix(["dog", "dog", "dog"]) == 'dog'
    assert s.longestCommonPrefix(["", "", ""]) == ''

    assert s.longestCommonPrefix2(["flower", "flow", "flight"]) == 'fl'
    assert s.longestCommonPrefix2(["dog", "racecar", "car"]) == ''
    assert s.longestCommonPrefix2(["dog", "dog", "dog"]) == 'dog'
    assert s.longestCommonPrefix2(["", "", ""]) == ''
