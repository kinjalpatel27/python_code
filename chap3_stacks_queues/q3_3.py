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


class SetOfStacks:
    def __init__(self, max_len):
        self.head_stack = []
        self.max_len = max_len

    def push(self, data):
        if len(self.head_stack) < 1 or len(self.head_stack[-1].stack) == self.max_len:
            stack = Stack()
            self.head_stack.append(stack)
        else:
            stack = self.head_stack[-1]

        stack.push(data)

    def pop(self):
        if len(self.head_stack) < 1:
            raise Exception("Empty Set of Stacks")

        stack = self.head_stack[-1]
        data = stack.pop()
        if len(stack.stack) == 0:
            self.head_stack.pop()
        return data

    def popAt(self, index):
        if len(self.head_stack) < index + 1:
            raise Exception("No stack at requested index")
        stack = self.head_stack[index]
        data = stack.pop()
        if len(stack.stack) == 0:
            self.head_stack.pop(index)
        return data


test_stacks = SetOfStacks(2)

data = np.random.randint(0, 40, 10)
for i in range(5):
    test_stacks.push(data[i])

for j in range(4, -1, -1):
    assert data[j] == test_stacks.pop()

for i in range(5):
    test_stacks.push(data[i])

assert data[3] == test_stacks.popAt(1)
assert data[2] == test_stacks.popAt(1)
assert data[4] == test_stacks.popAt(1)
