from utils import ListNode, createList, compareList


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        odd = head
        even = head.next
        evenHead = even

        while even is not None and even.next is not None:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = evenHead
        return head


if __name__ == "__main__":
    s = Solution()
    head = createList([1, 2, 3, 4, 5])
    out = s.oddEvenList(head)
    assert compareList(out, [1, 3, 5, 2, 4])

    head = createList([2, 1, 3, 5, 6, 4, 7])
    out = s.oddEvenList(head)
    assert compareList(out, [2, 3, 6, 7, 1, 5, 4])
