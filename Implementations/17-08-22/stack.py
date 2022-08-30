
#! STACK IS LIFO

class Stack:
    def __init__(self) -> None:
        self.container = []

    def push(self, val):
        self.container.append(val)

    def push_vals(self, arr):
        for val in arr:
            self.push(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def print(self):
        print(self.container)


if __name__ == "__main__":
    c_stack = Stack()

    c_stack.push(1)
    c_stack.push(5)
    c_stack.push_vals([10, 9, 8, 7, 6])

    c_stack.print()

    print(c_stack.pop())
    print(c_stack.pop())
    print(c_stack.pop())

    c_stack.print()
