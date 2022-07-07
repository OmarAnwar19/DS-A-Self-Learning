# to use collections.deque, we first have to import it
from collections import deque

if __name__ == "__main__":
    # in python, you can technically use a list as a queue

    # first, we create a deque by initializing it from collections using deque()
    queue = deque()

    # to insert something into the queue, you use queue.appendleft(value)
    # this does the same thing as appending at element 0,
    # --> it adds element at beginning, so it pushes all other elements to the right
    queue.appendleft("first value")
    queue.appendleft("second value")
    queue.appendleft("third value")
    queue.appendleft("fourth value")
    queue.appendleft("fifth value")

    # to get something from the queue, we can use queue.pop(), this gets the last element in the queu
    # --> since this element has been pushed to the end due to queue.appendleft(), this is the first item in the queue
    first_el = queue.pop()
    second_el = queue.pop()

    # printing the queue elements and queue
    print(first_el)
    print(second_el)
    print(queue)


# more practically, the correct implementation of deque is to create a queue class
class Queue:
    # first, we create an internal container, which is a deque
    def __init__(self):
        self.container = deque()

    # instead of append, we use enqueue to add elements to queue
    def enqueue(self, val):
        # this preforms appendleft on the value into the container
        self.container.appendleft(val)

    # instead of pop, we use deque, which internally, just does queue.pop()
    def dequeue(self):
        # pop the first elment from the queue, and return it
        return self.container.pop()

    # is_empty, returns True or False if the length of items in the queue is 0
    def is_empty(self):
        # return whether or not length of container items is 0
        return len(self.container) == 0

    # size function, returns the length of items in the queue
    def size(self):
        # get length of items in internal container and return it
        return len(self.container)
