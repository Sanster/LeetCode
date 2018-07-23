from utils import ListNode


class Solution(object):
    def hasCycle(self, head: ListNode) -> bool:
        """需要额外的空间
        Time: O(n)
        Space: O(n)
        """
        d = {}
        while head is not None:
            if head.next in d:
                return True
            d[head] = 1
            head = head.next
        return False

    def hasCycle2(self, head: ListNode) -> bool:
        """
        不需要额外空间
        """
        while head:
            if head.val is None:
                return True
            head.val = None
            # listNode 的值不会为 None，所以这里赋值以后如果下一个循环
            # head.val 为 None，则认为进入了循环
            head = head.next

        return False

    def hasCycle3(self, head: ListNode) -> bool:
        """
        Two pointers 方法，不需要额外空间，
        让 faster 追赶 slow，如果是一个圈的话可以追上，否则 faster 会到结尾
        """
        slow = head
        faster = head
        while faster is not None and faster.next is not None:
            slow = slow.next
            faster = faster.next.next
            if faster == slow:
                return True
        return False
