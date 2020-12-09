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

    def peek(self):
        if len(self.stack) < 1:
            raise Exception("Empty Stack")

        return self.stack[0]

    def isEmpty(self):
        return True if len(self.stack) < 1 else False


def stackLen(stack):
    temp_stack = Stack()
    length = 0
    while not (stack.isEmpty()):
        temp_stack.push(stack.pop())
        length += 1

    while not (temp_stack.isEmpty()):
        stack.push(temp_stack.pop())

    return length


def findMin(stack1, stack2, count, min_val=None):
    minimum = stack1.pop()
    cnt = 0

    for _ in range(count - 1):
        val = stack1.pop()
        if minimum > val:
            stack2.push(minimum)
            minimum = val
        else:
            stack2.push(val)
        cnt += 1
    # First minimum pushed to the empty stack 1. This condition would be True only
    # once
    if stack1.isEmpty() and minimum < stack2.peek():
        stack1.push(minimum)
        minimum = None

    # Push previous minimum value and current minimum value to stack 1
    # Return minimum = None since we want to skip pushing elements in next
    # round since stack1 and stack2 would be reversed
    if min_val is not None:
        stack1.push(min_val)
        stack1.push(minimum)
        minimum = None
    return stack1, stack2, cnt, minimum


stack = Stack()
data = np.random.randint(0, 20, 10)
for d in data:
    stack.push(d)


count = stackLen(stack)
temp_stack = Stack()
min_val = None
print("Unsorted stack ", stack.stack)

unsort = stack  # store stack for testing
length = count

for i in range(length):
    temp_stack, stack, count, min_val = findMin(stack, temp_stack, count, min_val)

if min_val is not None:
    stack.push(min_val)

if length % 2 != 0:
    stack = temp_stack
print("Sorted stack ", stack.stack)

assert (np.sort(unsort.stack) == stack.stack).all()
