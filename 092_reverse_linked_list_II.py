# https://leetcode.com/problems/reverse-linked-list-ii/
from typing import Optional

from utils import ListNode, createList, compareList


class Solution:
    successor = None

    def reverseN(self, head: ListNode, n) -> ListNode:
        if n == 1:
            self.successor = head.next
            return head
        last = self.reverseN(head.next, n - 1)
        head.next.next = head
        head.next = self.successor
        return last

    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        """
        OMG!  https://leetcode.com/problems/reverse-linked-list-ii/solution/242639
        Time: O(n)
        Space: O(1)
        """
        if left == 1:
            reversed_N = self.reverseN(head, right)
            return reversed_N
        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head


if __name__ == "__main__":
    s = Solution()
    data = [
        ([1, 2, 3, 4, 5], 2, 4, [1, 4, 3, 2, 5]),
    ]

    for it, l, r, gt in data:
        assert compareList(s.reverseBetween(createList(it), l, r), gt) is True
