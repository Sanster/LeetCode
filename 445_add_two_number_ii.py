"""
https://leetcode.com/problems/add-two-numbers-ii/description/
"""

from utils import ListNode, createList, compareList


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_vals = []
        l2_vals = []
        while l1 is not None:
            l1_vals.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            l2_vals.append(l2.val)
            l2 = l2.next

        head = curr = None
        carry = 0
        while len(l1_vals) != 0 or len(l2_vals) != 0:
            num = carry
            num += (l1_vals.pop() if len(l1_vals) != 0 else 0)
            num += (l2_vals.pop() if len(l2_vals) != 0 else 0)

            carry = num // 10
            num %= 10

            head = ListNode(num)
            head.next = curr

            curr = head

        if carry == 1:
            head = ListNode(carry)
            head.next = curr

        return head


def compare(s, l1, l2, result):
    l1 = createList(l1)
    l2 = createList(l2)
    out = s.addTwoNumbers(l1, l2)
    print(out)
    assert compareList(out, result) == True


if __name__ == '__main__':
    s = Solution()
    compare(s, [7, 2, 4, 3], [5, 6, 4], [7, 8, 0, 7])
    compare(s, [7, 2, 3], [5, 6, 4], [1, 2, 8, 7])
    compare(s, [3], [4], [7])
