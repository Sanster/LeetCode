"""
https://leetcode.com/problems/implement-strstr/
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Time: O(n * m)
        Space: O(1)
        """
        if needle == '':
            return 0

        for i in range(len(haystack)):
            # python 中的字符串 slice 会做 copy，重新创建一个 clone，这样效率低
            # https://stackoverflow.com/questions/35180377/time-complexity-of-string-slice
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1

    def strStr2(self, haystack: str, needle: str) -> int:
        """
        KMP 算法
        http://jakeboxer.com/blog/2009/12/13/the-knuth-morris-pratt-algorithm-in-my-own-words/
        """
        if needle == '':
            return 0

        # 生成部分匹配表 Partial Match Table
        lps = [0] * len(needle)  # longest prefix suffix
        i = 1
        length = 0  # length of the previous longest prefix suffix
        while i < len(needle):
            # example "abababca" and i == 5, len == 3. The longest prefix
            # suffix is "aba", when pat[i] == pat[len],
            # we get new prefix "abab" and new suffix "abab", so increase length
            # of current lps by 1 and go to next iteration.
            if needle[i] == needle[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    # This is tricky.Consider the example "ababe......ababc", i is index of 'c', len == 4. The longest prefix suffix is "abab",
                    # when pat[i]!=pat[len], we get new prefix "ababe" and suffix "ababc", which are not equal.
                    # This means we can't increment length of lps based on current lps "abab" with len==4. We may want to increment it based on
                    # the longest prefix suffix with length < len==4, which by definition is lps of "abab". So we set len to lps[len-1],
                    # which is 2, now the lps is "ab". Then check pat[i]==pat[len] again due to the while loop, which is also the reason
                    # why we do not increment i here. The iteration of i terminate until len==0 (didn't find lps ends with pat[i]) or found
                    # a lps ends with pat[i].
                    length = lps[length - 1]
                else:
                    # there isn 't any lps ends with pat[i], so set lps[i] = 0 and go to next iteration.
                    lps[i] = 0
                    i += 1

        i = 0
        j = 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1

            if j == len(needle):
                return i - j

            if (i < len(haystack)) and (haystack[i] != needle[j]):
                if j:
                    j = lps[j - 1]
                else:
                    i += 1
        return -1


if __name__ == "__main__":
    s = Solution()
    assert s.strStr('hello', 'll') == 2
    assert s.strStr('aaaaa', 'bba') == -1
    assert s.strStr('aaaaa', 'a') == 0
    assert s.strStr('aaaab', 'b') == 4
    assert s.strStr('aaa', 'aaaa') == -1
    assert s.strStr('aaa', 'aaaa') == -1
    assert s.strStr('abcdef', 'abcdef') == 0
    assert s.strStr('abcdef', '') == 0
    assert s.strStr('', '') == 0

    assert s.strStr2('CCVVABCDABDA', 'ABCDABD') == 4
    assert s.strStr2('hello', 'll') == 2
    assert s.strStr2('aaaaa', 'bba') == -1
    assert s.strStr2('aaaaa', 'a') == 0
    assert s.strStr2('aaaab', 'b') == 4
    assert s.strStr2('aaa', 'aaaa') == -1
    assert s.strStr2('aaa', 'aaaa') == -1
    assert s.strStr2('abcdef', 'abcdef') == 0
    assert s.strStr2('abcdef', '') == 0
    assert s.strStr2('', '') == 0
