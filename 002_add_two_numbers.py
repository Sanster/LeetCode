"""
https://leetcode.com/problems/reverse-linked-list/description/
"""

from utils import ListNode, createList, compareList


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Time: O(max(m, n))
        Space: O(max(m, n))
        """
        dummy = ListNode(0)
        current = dummy

        carry = 0
        while l1 or l2:
            num = carry
            num += (l1.val if l1 else 0)
            num += (l2.val if l2 else 0)

            carry = num // 10
            num %= 10

            current.next = ListNode(num)
            current = current.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        if carry == 1:
            current.next = ListNode(carry)

        return dummy.next


def test(l1, l2, result):
    l1 = createList(l1)
    l2 = createList(l2)
    assert compareList(s.addTwoNumbers(l1, l2), result) == True


if __name__ == '__main__':
    s = Solution()
    test([5], [5], [0, 1])
    test([1, 5], [5], [6, 5])
    test([5, 5, 5], [5], [0, 6, 5])
    test([5], [5, 5, 5], [0, 6, 5])
    test([1], [9, 9], [0, 0, 1])
