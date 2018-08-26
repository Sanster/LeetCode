"""
https://leetcode.com/problems/longest-common-prefix/description/
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''

        min_len = len(min(strs, key=lambda x: len(x)))

        for k in range(min_len):
            same = True
            for s in strs[1:]:
                if strs[0][k] != s[k]:
                    same = False

            if not same:
                return strs[0][:k]

        return strs[0]

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

    def longestCommonPrefix3(self, strs: List[str]) -> str:
        """
        二分法查找
        Time O(S*log(n)) S is the sum of all characters in all strings
        """
        if not strs:
            return ""

        min_len = len(min(strs, key=lambda x: len(x)))

        low = 1
        high = min_len

        while low <= high:
            mid = (low + high) // 2
            if self.isCommonPrefix(strs, mid):
                low = mid + 1
            else:
                high = mid - 1

        common = strs[0][0:(low + high) // 2]
        return common

    def isCommonPrefix(self, strs: List[str], len: int) -> bool:
        s0 = strs[0][:len]
        for s in strs[1:]:
            if not s.startswith(s0):
                return False
        return True


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

    assert s.longestCommonPrefix3(["flower", "flow", "flight"]) == 'fl'
    assert s.longestCommonPrefix3(["dog", "racecar", "car"]) == ''
    assert s.longestCommonPrefix3(["dog", "dog", "dog"]) == 'dog'
    assert s.longestCommonPrefix3(["", "", ""]) == ''
