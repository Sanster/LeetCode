from typing import List

from utils import TreeNode, ListNode

"""
Height balanced BST：每个 node 的两颗子树的高度差不能超过 1
"""


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        """
        :param nums: 从小到大排好序了
        """
        if not head:
            return None

        if not head.next:
            return TreeNode(head.val)

        slow = head
        fast = head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow

        # 从 mid 开始截断，这样后面再传 head 就相当于只传前半段
        tmp = mid.next
        mid.next = None

        root = TreeNode(tmp.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(tmp.next)

        return root
