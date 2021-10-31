"""
请编写一个程序，对一个栈里的整型数据，按升序进行排序（即排序前，栈里
的数据是无序的，排序后最大元素位于栈顶），要求最多只能使用一个额外的
栈存放临时数据，但不得将元素复制到别的数据结构中。
"""


def main(arr):
    # 最大元素位于栈底, arr[-1] 表示栈顶部
    ret_stack = []
    while arr:
        v = arr.pop()
        if ret_stack and ret_stack[-1] < v:
            # 把 ret_stack 中小于 v 的数全移动到 arr 中
            while ret_stack and ret_stack[-1] < v:
                arr.append(ret_stack.pop())
        ret_stack.append(v)

    while ret_stack:
        arr.append(ret_stack.pop())
    return arr


if __name__ == "__main__":
    # arr[-1] 表示栈顶部
    data = ([9, 3, 3, 4, 2, 4, 1, 2], [1], [1, 1], [4, 5, 8, 2, 3])
    for it in data:
        gt = sorted(it.copy())
        pred = main(it)
        assert gt == pred, f"gt: {gt} pred: {pred}"
