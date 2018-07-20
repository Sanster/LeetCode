from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        if self.next is None:
            return '%d -> None' % self.val
        else:
            return '%d -> %s' % (self.val, self.next)


def createList(num: List[int]) -> ListNode:
    first = ListNode(num[0])
    last = first
    for n in num[1:]:
        node = ListNode(n)
        last.next = node
        last = node
    return first


def compareList(listNode: ListNode, nums: List[int]):
    node = listNode
    for num in nums:
        if node is None or num != node.val:
            return False
        node = node.next
    return True


def printList(node: ListNode):
    n = node
    while n is not None:
        print(n)
        n = n.next
