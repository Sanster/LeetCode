"""
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
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
            num += l1.val if l1 else 0
            num += l2.val if l2 else 0

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


if __name__ == "__main__":
    s = Solution()
    test([5], [5], [0, 1])
    test([1, 5], [5], [6, 5])
    test([5, 5, 5], [5], [0, 6, 5])
    test([5], [5, 5, 5], [0, 6, 5])
    test([1], [9, 9], [0, 0, 1])
