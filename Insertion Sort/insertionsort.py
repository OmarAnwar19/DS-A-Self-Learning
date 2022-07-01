def insertion_sort(elements):
    # get the size of the array
    size = len(elements)

    # since the first element in the array does not have anything before it,
    # we loop between the second element (1), until the end of the array (size element)
    for i in range(1, size):
        # we start by getting the current element, which we will compare
        curr = elements[i]

        # now that we have the current and previous elements,
        # we keep checking if the left element is less than the current one while
        # the previous element index is not 0 (we havn't reached the beginning of the array),
        # and the current element is less than the previous one (if not, then already in correct place)
        while [i-1] >= 0 and curr < elements[i-1]:
            #!swap version 1
            # then, as soon as the loop stops, that means element has to be inserted here for sort
            # first, we have to make space for the element to be inserted, we start by
            # copying the value of the current element into the index of the previous element
            # the reason we do prev+1 instead of curr, is beacuse curr could be 0, which will
            # give us an out of range error, while prev+1 will handle that
            # * elements[prev+1] = elements[prev]

            # then, we set the previous index as the index before the previous (curr-2)
            # * prev = prev-1

            # now, we set the value of the element after the new previous ((prev=curr-2)) + 1) = prev,
            # as the value of the current value
            # as with our first swap, the reason we do prev-1 instead of just prev, is to avoid
            # any out of bounds exceptions
            # * elements[prev+1] = curr

            #! swap version 2
            # first, we set the element at the current index, as the one in the prev index
            elements[i] = elements[i-1]
            # next, we decrement i, so that the next iteration starts from the next 2nd last, 3rd last, etc..
            i = i-1
            # finally, set the new current element (elements[new_i]), as curr
            elements[i] = curr


if __name__ == "__main__":
    # the elements array
    elements = [21, 38, 29, 17, 4, 25, 11, 32, 9]

    # call the function to sort the array, returns in pla
    # ce
    insertion_sort(elements)

    # print the elements
    print(elements)
