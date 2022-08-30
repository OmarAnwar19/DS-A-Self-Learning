
#! QUEUE IS FIFO

class Queue:
    def __init__(self) -> None:
        self.container = []

    def push(self, val):
        self.container.insert(0, val)

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
    c_queue = Queue()

    c_queue.push(1)
    c_queue.push(2)
    c_queue.push(3)
    c_queue.push(4)
    c_queue.push(5)

    c_queue.print()

    c_queue.push_vals([10, 9, 8, 7, 6])

    c_queue.print()

    print(c_queue.pop())
    print(c_queue.pop())
    print(c_queue.pop())

    c_queue.print()
