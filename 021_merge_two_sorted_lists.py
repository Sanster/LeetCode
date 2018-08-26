"""
https://leetcode.com/problems/merge-two-sorted-lists/description/
"""
from typing import List
from utils import createList, ListNode, compareList


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """worst"""
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        l1_node = l1
        l2_node = l2
        vals = []
        while l1_node is not None:
            vals.append(l1_node.val)
            l1_node = l1_node.next

        while l2_node is not None:
            vals.append(l2_node.val)
            l2_node = l2_node.next

        vals = sorted(vals)
        return createList(vals)

    # iteratively
    # l1, l2 是事先排好序的，要充分利用
    # 对于 l1=[2,2,3]  l2=[1]，l2[0]放在第一位后，l1的head直接接上去就可以了
    # 对于 l1=[1,2,3]  l2=[2]，l1[0]放在第一位，再放l2[0], 然后再把 l1[1] 接上去
    def mergeTwoLists1(self, l1, l2):
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


if __name__ == '__main__':
    s = Solution()
    l1 = createList([1, 2, 4])
    l2 = createList([1, 3, 4])
    assert compareList(l2, [1, 3, 4]) == True
    assert compareList(l2, [1, 2, 4]) == False

    assert compareList(s.mergeTwoLists1(l1, l2), [1, 1, 2, 3, 4, 4]) == True

    l1 = createList([1, 2, 4])
    l2 = createList([1])
    assert compareList(s.mergeTwoLists1(l1, l2), [1, 1, 2, 4]) == True

    l1 = createList([1, 2, 4])
    l2 = createList([5])
    assert compareList(s.mergeTwoLists1(l1, l2), [1, 2, 4, 5]) == True
