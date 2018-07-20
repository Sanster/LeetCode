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


def compareList(node: ListNode, nums: List[int]):
    node_vals = []
    while node is not None:
        node_vals.append(node.val)
        node = node.next

    if len(node_vals) != len(nums):
        return False

    return node_vals == nums


def printList(node: ListNode):
    n = node
    while n is not None:
        print(n)
        n = n.next
