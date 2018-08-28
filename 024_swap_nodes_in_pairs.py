from utils import ListNode


# https://leetcode.com/problems/swap-nodes-in-pairs/discuss/11312/Python-concise-iterative-and-recursive-solutions.
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        dummy = pre = ListNode(0)
        dummy.next = head

        while head and head.next:
            next = head.next.next
            pre.next = head.next
            head.next.next = head

            pre = head
            head.next = next
            head = head.next

        return dummy.next
