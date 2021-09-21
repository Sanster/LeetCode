"""
给定一个字符串 s，正整数 k，返回 s 中按照字典序排序的长度为 k 的最大子串

例如：s="abceadc", k=2 ，则最长子串为 edc
"""


class Solution:
    def largestSubStr(self, s: str, k: int) -> str:
        stack = [s[0]]
        for i, c in enumerate(s[1:]):
            str_remain_leng = len(s) - (i + 1)
            # "abce"/"abc"
            if len(stack) + str_remain_leng == k:
                return "".join(stack) + s[i + 1 :]

            should_push = False
            while len(stack):
                if stack[-1] < c:
                    stack.pop()
                    should_push = True
                else:
                    break

            if should_push:
                stack.append(c)

        return "".join(stack[:3])


if __name__ == "__main__":
    f = Solution()
    data = [
        ("abceadc", 3, "edc"),
        ("abc", 3, "abc"),
        ("abce", 3, "bce")
    ]

    for s, k, gt in data:
        assert f.largestSubStr(s, k) == gt, f"s: {s}, k: {k}, gt: {gt}, pred: {f.largestSubStr(s, k)}"
