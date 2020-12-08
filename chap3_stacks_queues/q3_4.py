import numpy as np


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) < 1:
            raise Exception("Empty Stack")
        return self.stack.pop()


class MyQueue:
    def __init__(self):
        self.queue = Stack()
        self.temp_stack = Stack()

    def add(self, data):
        self.queue.push(data)

    def remove(self):
        if len(self.temp_stack.stack) < 1:
            while len(self.queue.stack) > 0:
                data = self.queue.stack.pop()
                self.temp_stack.push(data)

        return self.temp_stack.pop()


queue = MyQueue()
data = np.random.randint(0, 40, 10)
for i in range(5):
    queue.add(data[i])

for i in range(3):
    assert data[i] == queue.remove()


for i in range(5, 10):
    queue.add(data[i])

for i in range(3, 7):
    assert data[i] == queue.remove()
