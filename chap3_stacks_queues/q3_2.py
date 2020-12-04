import numpy as np


class Stack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, data):
        assert np.isscalar(data)
        if len(self.stack) == 0:
            self.stack.append(data)
            self.min_stack.append(data)
        else:
            if self.min_stack[-1] >= data:
                self.min_stack.append(data)

            self.stack.append(data)

    def pop(self):
        if len(self.stack) < 1:
            raise Exception("Empty stack")
        data = self.stack.pop()
        if data <= self.min_stack[-1]:
            self.min_stack.pop()
        return

    def min(self):
        if len(self.min_stack) < 1:
            raise Exception("Empty stack")
        return self.min_stack[-1]


stack_test = Stack()
arry = np.random.randint(0, 50, 20)
arry[0] = -1
# Add 10 element from an array and push on stack
for i in range(10):
    stack_test.push(arry[i])
assert len(stack_test.min_stack) == 1

for i in range(10):
    stack_test.pop()

arry[0] = 25
# Add 10 element from an array and push on stack
for i in range(10):
    stack_test.push(arry[i])

# check if stack.min returns correct minimum value
assert min(arry[:10]) == stack_test.min()

# pop few values from stack and check minimum again
for i in range(4):
    stack_test.pop()

assert min(arry[:6]) == stack_test.min()

# push few values from stack and check minimum again
for i in range(20):
    stack_test.push(arry[i])

assert min(arry) == stack_test.min()
