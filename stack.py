class Stack:

    def __init__(self):
        self.data = []

    def pop(self):
        return self.data.pop()

    def push(self, item):
        self.data.append(item)

    def peek(self):
        return self.data[-1]

if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)

    print(stack.peek())
    stack.pop()
    print(stack.peek())

import numpy as np

if __name__ == "__main__":
    x = np.array([1, 2, 3, 3])
    print(x.argmax())


