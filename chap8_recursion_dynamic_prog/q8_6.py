class Stack:
    def __init__(self, name):
        self.name = name
        self.stack = []

    def __repr__(self):
        return self.name

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            AssertionError("Empty stack")

    def print_val(self):
        print(self.stack)


def hanoi(n, start, center, end):
    if n == 1:
        val = start.pop()
        end.push(val)
        print(start, "[disk: %d]" % val, " ----> ", end)
        return
    hanoi(n - 1, start, end, center)
    val = start.pop()
    end.push(val)
    print(start, "[disk: %d]" % val, " ----> ", end)
    hanoi(n - 1, center, start, end)


n = 4
start = Stack("start")
center = Stack("center")
end = Stack("end")
start.stack = list(range(n, 0, -1))

hanoi(n, start, center, end)

print("Start: ", start.stack)
print("End:   ", end.stack)
