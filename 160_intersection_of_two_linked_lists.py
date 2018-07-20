"""
https://leetcode.com/problems/intersection-of-two-linked-lists/description/
"""

from utils import ListNode, createList, compareList


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pA = headA
        pB = headB

        len_A = 0
        while pA is not None:
            len_A += 1
            pA = pA.next
        pA = headB

        len_B = 0
        while pB is not None:
            len_B += 1
            pB = pB.next

        pB = headA

        diff = abs(len_A - len_B)

        if len_A < len_B:
            lessP, moreP = pA, pB
        else:
            lessP, moreP = pB, pA

        for i in range(diff):
            lessP = lessP.next

        while lessP and moreP:
            if lessP.val == moreP.val:
                return lessP

            lessP = lessP.next
            moreP = moreP.next

        return None

    def getIntersectionNode2(self, headA, headB):
        # the idea is if you switch head, the possible difference between length would be countered.
        # On the second traversal, they either hit or miss.
        # if they meet, pa or pb would be the node we are looking for,
        # if they didn't meet, they will hit the end at the same iteration, pa == pb == None, return either one of them is the same,None
        if headA is None or headB is None:
            return None

        pa = headA  # 2 pointers
        pb = headB

        while pa is not pb:
            # if either pointer hits the end, switch head and continue the second traversal,
            # if not hit the end, just move on to next
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next

        return pa  # only 2 ways to get out of the loop, they meet or the both hit the end=None



if __name__ == '__main__':
    s = Solution()
    l1 = createList([1, 2, 3, 4, 5])
    l2 = createList([8, 3, 4, 5])
    assert compareList(s.getIntersectionNode(l1, l2), [3, 4, 5]) == True

    l1 = createList([1, 3, 5, 7, 9, 11])
    l2 = createList([2, 4, 9, 11])
    assert compareList(s.getIntersectionNode(l1, l2), [9, 11]) == True

    l1 = createList([1, 2, 3])
    l2 = createList([1, 2])
    assert compareList(s.getIntersectionNode(l1, l2), None) == True
