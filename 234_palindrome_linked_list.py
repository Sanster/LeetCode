from utils import ListNode, createList


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """
        Time O(n)
        Space O(n)
        """
        ori = []
        while head is not None:
            ori.append(head.val)
            head = head.next

        return ori == ori[::-1]

    def isPalindrome2(self, head: ListNode) -> bool:
        """
        Time O(n)
        Space O(1)
        """
        fast = slow = head
        # find mid node, slow is the mid node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # 1->2->2->2->1 变成比较  1->2 和 2<-2<-1，中间一个不用管
        # 1->2->2->1 变成比较  1->2 和 2<-1
        # reverse node after mid(slow)
        slow_head = None
        while slow:
            next_slow_head = slow.next
            slow.next = slow_head

            slow_head = slow
            slow = next_slow_head

        while slow_head:
            if slow_head.val != head.val:
                return False
            slow_head = slow_head.next
            head = head.next
        return True


if __name__ == "__main__":
    s = Solution()
    head = createList([1, 2, 2, 1])
    assert s.isPalindrome(head) == True

    head = createList([1, 2, 2])
    assert s.isPalindrome(head) == False

    head = createList([2, 2])
    assert s.isPalindrome(head) == True

    assert s.isPalindrome(None) == True

    head = createList([1])
    assert s.isPalindrome(head) == True

    head = createList([1, 2, 2, 1])
    assert s.isPalindrome2(head) == True

    head = createList([1, 2, 2])
    assert s.isPalindrome2(head) == False

    head = createList([2, 2])
    assert s.isPalindrome2(head) == True

    assert s.isPalindrome2(None) == True

    head = createList([1])
    assert s.isPalindrome2(head) == True
