# 用队列实现栈
# 使用队列实现栈的下列操作：
#
# push(x) -- 元素 x 入栈
# pop() -- 移除栈顶元素
# top() -- 获取栈顶元素
# empty() -- 返回栈是否为空
# 注意:
#
# 你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty 这些操作是合法的。
# 你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
# 你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.storage_queue = []
        self.cache_que = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if not self.storage_queue and not self.cache_que:
            self.storage_queue.append(x)
        elif self.storage_queue:
            self.storage_queue.append(x)
        elif self.cache_que:
            self.cache_que.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if not self.cache_que:
            for i in range(len(self.storage_queue) - 1):
                self.cache_que.append(self.storage_queue.pop(0))
            return self.storage_queue.pop()
        if not self.storage_queue:
            for i in range(len(self.cache_que) - 1):
                self.storage_queue.append(self.cache_que.pop(0))
            return self.cache_que.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        if not self.cache_que:
            for i in range(len(self.storage_queue) - 1):
                self.cache_que.append(self.storage_queue.pop(0))
            temp = self.storage_queue[0]
            self.cache_que.append(self.storage_queue.pop(0))
            return temp
        if not self.storage_queue:
            for i in range(len(self.cache_que) - 1):
                self.storage_queue.append(self.cache_que.pop(0))
            temp = self.cache_que[0]
            self.storage_queue.append(self.cache_que[0])
            return temp

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if self.storage_queue or self.cache_que:
            return False
        return True

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


if __name__ == '__main__':
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    print(stack.top())
    print(stack.pop())
    print(stack.empty())