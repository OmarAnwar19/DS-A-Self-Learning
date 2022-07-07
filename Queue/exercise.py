from collections import deque

import time
import threading


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def peek(self):
        return self.buffer[-1]

    def size(self):
        return len(self.buffer)


def place_order(orders):
    queue = Queue()

    def place():
        for order in orders:
            queue.enqueue(order)
            time.sleep(0.5)

    def retrieve():
        time.sleep(1)
        while True:
            order = queue.dequeue()
            print(order)
            time.sleep(0.2)

    place_thread = threading.Thread(target=place, args=())
    retrieve_thread = threading.Thread(target=retrieve, args=())

    place_thread.start()
    retrieve_thread.start()

    return queue


def print_binary():
    # get first item, then add 0
    # get first item then add 1,
    # get second item then add 0
    # get second item then add 1
    # etc, until len(arr) = 9
    queue = Queue()
    queue.enqueue("1")

    i = 0

    while i < 10:
        left = queue.peek()
        print(left)

        queue.enqueue(left + "0")
        queue.enqueue(left + "1")

        queue.dequeue()

        i += 1


if __name__ == "__main__":
    #place_order(['pizza', 'samosa', 'pasta', 'biryani', 'burger'])
    print(print_binary())
