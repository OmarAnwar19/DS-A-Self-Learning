# the first thing we have to do when implementing a stack using collections.deque is import it
from collections import deque

if __name__ == "__main__":
    # then, we can initialize the stack using var = deque()
    stack = deque()

    # to push elements to the stack, we use stack.append(element)
    stack.append(1)
    stack.append(2)
    stack.append(3)
    stack.append(4)
    stack.append(5)

    # to pop the last element from the stack, you use stack.pop()
    last = stack.pop()

    # peek at the top element of the stack using stack[-1]
    # --> peek returns the top element without removing it from the stack
    print(stack[-1])

    # printing the stack and last element to prove functionality
    print(stack)
    print(last)


# we can also implement a stack using a class with deque
class Stack:
    # internally, it just creats a stack using deque
    def __init__(self):
        self.container = deque()

    # push function
    def push(self, val):
        # appends input value to the container
        self.container.append(val)

    # pop function
    def pop(self):
        # pops the most recent elment from the top of the container
        return self.container.pop()

    # peek function
    def peek(self):
        # peeks at the top element -->
        # returns the element from the top of the stack without removing it
        return self.container[-1]

    # is empty function
    def is_empty(self):
        # returns True or False depending on if the stack has any items (len == 0)
        return len(self.container) == 0

    # size funciton
    def size(self):
        # returns the length of the items in the stack
        return len(self.container)
