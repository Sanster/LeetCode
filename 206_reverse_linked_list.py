"""
https://leetcode.com/problems/reverse-linked-list/description/
"""

from utils import ListNode, createList, compareList


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        Time: O(n)
        Space: O(1)
        """
        last_node = None
        while head is not None:
            next_head = head.next

            head.next = last_node

            last_node = head
            head = next_head
        return last_node


if __name__ == '__main__':
    s = Solution()
    l1 = createList([1, 2, 3, 4, 5])

    assert compareList(s.reverseList(l1), [5, 4, 3, 2, 1]) == True
