from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


def reverse_string(string):
    # create an empty stack
    stack = Stack()
    # create an empty string, this will be returned
    ret_str = ""

    # add each character in the input string to the stack
    for char in string:
        stack.push(char)

    # pop each element from the stack and add it to the ret_str
    while not stack.is_empty():
        ret_str += stack.pop()

    return ret_str


def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    return match_dict[ch1] == ch2


def is_balanced(string):
    stack = Stack()

    for char in string:
        if char == '(' or char == '{' or char == '[':
            stack.push(char)
        if char == ')' or char == '}' or char == ']':
            if stack.size() == 0:
                return False
            if not is_match(char, stack.pop()):
                return False

    return stack.size() == 0


if __name__ == "__main__":
    print(reverse_string("We will conquere COVID-19"))
    print(is_balanced("))"))
