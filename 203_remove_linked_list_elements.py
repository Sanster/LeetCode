from utils import ListNode, createList, compareList


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        """
        Time O(n)
        Space O(1)
        """
        # 找到第一个不是 val 的节点
        while head is not None:
            if head.val != val:
                break
            else:
                head = head.next

        prev = None
        curr = head
        while curr is not None:
            if curr.val == val:
                # prev 为 head 的引用，这一步相当于在原始 llinked list 上操作
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
        return head


if __name__ == "__main__":
    s = Solution()
    head = createList([1, 2, 6, 3, 4, 5, 6])
    out = s.removeElements(head, 6)
    assert compareList(out, [1, 2, 3, 4, 5])

    head = createList([6, 2, 6, 3, 4, 5, 6])
    out = s.removeElements(head, 6)
    assert compareList(out, [2, 3, 4, 5])

    head = createList([6, 6, 6])
    out = s.removeElements(head, 6)
    assert compareList(out, [])
