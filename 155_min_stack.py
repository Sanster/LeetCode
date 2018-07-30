"""
关键是如何实现 getMin()，使得 getMin 为时间复杂度为线性
"""


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        last_min = self.getMin()
        if last_min is not None:
            cur_min = min(x, last_min)
        else:
            cur_min = x
        # 每次 push 保存当前 stack 的最小值
        self.stack.append((x, cur_min))

    def pop(self):
        """
        :rtype: void
        """
        if len(self.stack) != 0:
            self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) != 0:
            return self.stack[-1][0]
        else:
            return None

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) != 0:
            return self.stack[-1][1]
        else:
            return None


class MinStack2:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = float('inf')
        self.val = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if x <= self.min:
            # 保存上一个 stack 状态的最小值
            self.val.append(self.min)
            # 设置当前最小值
            self.min = x
        # 添加 stack 值
        self.val.append(x)

    def pop(self):
        """
        :rtype: void
        """
        tmp = self.val.pop()
        # 如果 tmp 是 保存的最小值，则需要再做一次 pop，获得上一个状态的最小值
        if tmp == self.min:
            self.min = self.val.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.val[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min


if __name__ == "__main__":
    obj = MinStack2()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    assert obj.getMin() == -3
    obj.pop()
    assert obj.top() == 0
    assert obj.getMin() == -2
