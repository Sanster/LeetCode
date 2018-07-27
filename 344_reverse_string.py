class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

    def reverseString2(self, s):
        r = list(s)
        k = len(s) - 1
        i = 0
        while i < k:
            r[i], r[k] = r[k], r[i]
            i += 1
            k -= 1

        return ''.join(r)

if __name__ == "__main__":
    s = Solution()
    print(s.reverseString2("Hello"))
    print(s.reverseString2("H"))
    print(s.reverseString2(""))

