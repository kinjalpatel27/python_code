class stacks:
    def __init__(self, length):
        self.array = []
        self.stack_head = [None, None, None]
        self.track_head = 0

        for i in range(length - 1):
            self.array.append((i + 1, None))
        self.array.append((length, None))

    def push(self, stack, data):
        if stack > 3 or stack < 0:
            raise Exception("Invalid Stack")
        # if self.track_head is None:
        #     raise Exception("Out of Memory")
        tmp = self.array[self.track_head][0]
        self.array[self.track_head] = (self.stack_head[stack - 1], data)
        self.stack_head[stack - 1] = self.track_head

        self.track_head = tmp if tmp < len(self.array) else None

    def pop(self, stack):
        if stack > 3 or stack < 0:
            raise Exception("Invalid Stack")

        head = self.stack_head[stack - 1]
        if head is None:
            raise Exception("No element present is stack")
        data = self.array[head][1]
        self.stack_head[stack - 1] = self.array[head][0]
        self.array[head] = (self.track_head, None)
        self.track_head = head
        return data


# create a stack of known length
test_stack = stacks(10)
# create a tuple of data to push on stack
data = [
    (1, 2),
    (3, 0),
    (2, 9),
    (3, 5),
    (1, 3),
    (1, 0),
    (3, 4),
    (2, 10),
    (1, 6),
    (2, 10),
]
# Push first four element to respective stacks
for d in data[:4]:
    test_stack.push(d[0], d[1])

# pop element from stack 1 & 2 and check if its valid
data2 = test_stack.pop(2)
assert data2 == data[2][1]
data1 = test_stack.pop(1)
assert data1 == data[0][1]

# Change one of the element in the data
data[4] = (2, 45)
# since we first pushed 4 elements and 2 are popped, we have 8 spaces to
# fill whole stack
for d in data[2:]:
    test_stack.push(d[0], d[1])

# pop element from stack 2 & 3 and check if its valid
data3 = test_stack.pop(3)
assert data3 == data[-4][1]
data2 = test_stack.pop(2)
assert data2 == data[-1][1]
