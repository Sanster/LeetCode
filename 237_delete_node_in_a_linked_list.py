"""
https://leetcode.com/problems/delete-node-in-a-linked-list/description/
"""

from utils import ListNode, createList, compareList


class Solution:
    def deleteNode(self, node: ListNode):
        node.val = node.next.val
        node.next = node.next.next

