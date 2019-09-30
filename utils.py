from collections import deque
from typing import List, Optional


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


def compareList(node: ListNode, nums: List[int]) -> bool:
    if node is None and nums is None:
        return True

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


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)


def createBTree(vals: List[int]) -> Optional[TreeNode]:
    if vals[0] is None:
        return None

    root = TreeNode(vals[0])
    queue = deque([root])
    idx = 1
    while idx < len(vals):
        node = queue.popleft()
        if node:
            node.left = TreeNode(vals[idx]) if vals[idx] is not None else None
            queue.append(node.left)
            if idx + 1 < len(vals):
                node.right = TreeNode(vals[idx + 1]) if vals[idx + 1] is not None else None
                queue.append(node.right)
                idx += 1
            idx += 1
    return root


def btree_levelorder_traverse(tree: TreeNode) -> List[int]:
    out = [tree.val]
    queue = deque([tree])
    while len(queue) > 0:
        node = queue.popleft()
        # 代表是叶子节点
        if node.left is None and node.right is None:
            continue

        if node.left is not None:
            out.append(node.left.val)
            queue.append(node.left)
        else:
            out.append(None)

        if node.right is not None:
            out.append(node.right.val)
            queue.append(node.right)
        else:
            out.append(None)
    return out


def btree_preorder_traverse(tree: TreeNode) -> List[int]:
    if tree is None:
        return [None]

    out = [tree.val]
    if tree.left is not None:
        out.extend(btree_preorder_traverse(tree.left))
    if tree.right is not None:
        out.extend(btree_preorder_traverse(tree.right))
    return out


def btree_inorder_traverse(tree: TreeNode) -> List[int]:
    if tree is None:
        return [None]
    out = []

    if tree.left is not None:
        out.extend(btree_inorder_traverse(tree.left))

    out.append(tree.val)

    if tree.right is not None:
        out.extend(btree_inorder_traverse(tree.right))
    return out


def btree_inorder_traverse_stack(tree: TreeNode) -> List[int]:
    stack = []
    node = tree
    out = []
    while node or stack:
        # 把所有节点的左子树 append 进去
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        out.append(node.val)
        node = node.right
    return out


def btree_postorder_traverse(tree: TreeNode) -> List[int]:
    if tree is None:
        return [None]
    out = []

    if tree.left is not None:
        out.extend(btree_postorder_traverse(tree.left))

    if tree.right is not None:
        out.extend(btree_postorder_traverse(tree.right))

    out.append(tree.val)
    return out


if __name__ == "__main__":
    tree = createBTree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])

    print(btree_levelorder_traverse(tree))

    assert btree_preorder_traverse(tree) == [10, 5, 3, 3, -2, 2, 1, -3, 11]

    print(btree_inorder_traverse(tree))
    print(btree_inorder_traverse_stack(tree))

    print(btree_postorder_traverse(tree))
