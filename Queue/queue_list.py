if __name__ == "__main__":
    # in python, you can technically use a list as a queue

    # first, we create an empty array as the queue
    queue = []

    # to insert something into the queue, you use queue.insert(0, value)
    queue.insert(0, "first value")
    queue.insert(0, "second value")
    queue.insert(0, "third value")
    queue.insert(0, "fourth value")
    queue.insert(0, "fifth value")

    # to get something from the queue, we can use queue.pop(), this gets the first item in the list
    first_el = queue.pop()
    second_el = queue.pop()

    # printing the queue elements and queue
    print(first_el)
    print(second_el)
    print(queue)

    # the difference between how a stack and queue are implemented at lists in python is that
    # a stack uses stack.append(value), which adds the element to the end of the list,
    # while a queue uses stack.insert(0, value), which adds the element at the beginning of the list,
    # --> this pushes all previous elements at the end of the list, meaning that the first element inserted
    #     is now technically the last element in the list, so queue.pop() returning the last element really returns the first one
    # then, when we use stack.pop), this returns the last element inserted into the stack
    # when we use queue.pop(), this returns the first element inserted into the stack, which has been pushed all the way to the end
