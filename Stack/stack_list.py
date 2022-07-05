if __name__ == "__main__":
    # in python, one way to create a stack is to create an empty list,
    stack = []

    # then, to push an element to the stack, simply use array.append(val)
    stack.append(1)
    stack.append(2)
    stack.append(3)
    stack.append(4)
    stack.append(5)

    # to pop an element from the stack (get element from top of stack),
    # use stack.pop
    last = stack.pop()

    # printing the stack and last popped element to prove this
    print(stack)
    print(last)
