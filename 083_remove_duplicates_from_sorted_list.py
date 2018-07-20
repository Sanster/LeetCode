"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
"""

from utils import ListNode, createList, compareList


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        Bad! 需要新建 node 效率低
        """
        if head is None:
            return None

        curr = out = ListNode(head.val)
        while (head is not None) and (head.next is not None):
            if curr.val != head.next.val:
                curr.next = ListNode(head.next.val)
                curr = curr.next

            head = head.next
        return out

    def deleteDuplicates2(self, head: ListNode) -> ListNode:
        """
        Time: O(n)
        Space: O(1)
        """
        curr = head
        while (curr is not None) and (curr.next is not None):
            if curr.val != curr.next.val:
                curr = curr.next
            else:
                # curr 不动，只改 curr 的 next，相当于跳过了当中一个
                curr.next = curr.next.next
        return head


if __name__ == '__main__':
    s = Solution()
    l1 = createList([1])
    assert compareList(s.deleteDuplicates(l1), [1]) == True

    l1 = createList([1, 1, 2])
    assert compareList(s.deleteDuplicates(l1), [1, 2]) == True

    l1 = createList([1, 1, 2, 3, 3])
    assert compareList(s.deleteDuplicates(l1), [1, 2, 3]) == True

    l1 = createList([1, 2, 3, 4, 5])
    assert compareList(s.deleteDuplicates(l1), [1, 2, 3, 4, 5]) == True

    l1 = createList([1, 1, 1, 1, 1])
    assert compareList(s.deleteDuplicates(l1), [1]) == True

    l1 = createList([1])
    assert compareList(s.deleteDuplicates2(l1), [1]) == True

    l1 = createList([1, 1, 2])
    assert compareList(s.deleteDuplicates2(l1), [1, 2]) == True

    l1 = createList([1, 1, 2, 3, 3])
    assert compareList(s.deleteDuplicates2(l1), [1, 2, 3]) == True

    l1 = createList([1, 2, 3, 4, 5])
    assert compareList(s.deleteDuplicates2(l1), [1, 2, 3, 4, 5]) == True

    l1 = createList([1, 1, 1, 1, 1])
    assert compareList(s.deleteDuplicates2(l1), [1]) == True
