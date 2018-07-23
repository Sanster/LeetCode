# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 使用 s1 作为主要存储
        self.s1 = []
        self.s2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        Time: O(n)
        Space: O(n)
        """
        # s1 的所有数据反向放到 s2 中
        for _ in range(len(self.s1)):
            self.s2.append(self.s1.pop())

        self.s2.append(x)

        # s2 数据放到 s1 里面，新加的元素 x 会被放在 s1 的最下层
        for _ in range(len(self.s2)):
            self.s1.append(self.s2.pop())

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        Time: O(1)
        """
        return self.s1.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        Time: O(1)
        """
        return self.s1[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.s1) == 0


class MyQueue2:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []
        self.front = None

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        Time: O(1)
        Space: O(n)
        """
        if len(self.s1) == 0:
            self.front = x
        self.s1.append(x)

    # Key: s2 中的内容不会移回 s1，只有当 s2 被消耗完时，才重新从 s1 取数据
    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        # s1 数据反向存入 s2
        if len(self.s2) == 0:
            for _ in range(len(self.s1)):
                self.s2.append(self.s1.pop())

        return self.s2.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.s2) != 0:
            return self.s2[-1]

        return self.front

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.s1) == 0 and len(self.s2) == 0
