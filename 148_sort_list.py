from utils import ListNode


# https://leetcode.com/problems/sort-list/discuss/46714/Java-merge-sort-solution
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        """
        冒泡
        Time O(n^2)
        """
        if not head:
            return head

        if not head.next:
            return head

        node1 = head
        while node1:
            node2 = node1.next
            while node2:
                if node1.val > node2.val:
                    tmp = node1.val
                    node1.val = node2.val
                    node2.val = tmp

                node2 = node2.next

            node1 = node1.next

        return head

    def sortList2(self, head: ListNode) -> ListNode:
        """
        merge sort
        """
        if not head or not head.next:
            return head

        # 将 list 分成两半
        prev = None
        slow = head
        fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # 用来截断，下面的 head 不会包含 slow
        prev.next = None

        # sort each half
        l1 = self.sortList2(head)
        l2 = self.sortList2(slow)

        return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, l1, l2):
        # Time:  O(n)
        # Space: O(1)
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next
