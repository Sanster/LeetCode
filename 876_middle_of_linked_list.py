from utils import ListNode, createList


class Solution:
    def middleNode2(self, head: ListNode) -> ListNode:
        """
        Time O(n)
        Space O(1)
        """
        count = 0
        node = head
        while node is not None:
            count += 1
            node = node.next

        node = head
        mid_pos = int(count / 2 + 1)
        for _ in range(mid_pos - 1):
            node = node.next

        return node

    def middleNode(self, head: ListNode) -> ListNode:
        """
        Time O(n)
        Space O(1)
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


if __name__ == "__main__":
    s = Solution()
    data = [
        ([1, 2, 3, 4, 5], 3),
        ([1, 2, 3, 4, 5, 6], 4),
        ([1], 1),
        ([1, 2], 2),
        ([1, 2, 3], 2),
    ]
    for it, gt in data:
        assert (
            s.middleNode2(createList(it)).val == gt
        ), f"{it} {s.middleNode2(createList(it)).val} {gt}"
