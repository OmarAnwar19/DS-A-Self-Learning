def bubble_sort(elements):
    # first thing we have to do is get the size of the elements
    size = len(elements)

    # in bubble sort, we compare two elements at a time, so,
    # our outermost loop has to be to size-1, because once we reach
    # the final element, there is no elment after it (hence size-1)
    for i in range(size-1):
        # we first have to create a swapped variable, this checks if two elements have been swapped
        # if the variable does not become true, that means elements were not swapped
        # this means that the array is already sorted, so we can exit the loop
        swapped = False

        # this inner loop sorts only first element, so we need an outer loop
        # --> the outer loop will sort the first element size-1 times, until whole array is sorted

        # inner loop to sort the first two elements, then second and third in second iteration, etc...
        # loops over range size-1-i, this means that we get the size, then subtract 1,
        # this means that we loop over the entire array, then second iteration, where i = 1,
        # we loop until size - 2, then size -3 for thid iter., etc..add()
        # --> this is more efficent then looping over the entire array each time, as the
        # last elements will keep getting sorted, so no point to check them again
        for j in range(size-1-i):
            # now, we check if the first element in index j is greater than the element after it
            if elements[j] > elements[j+1]:
                # if they are greater, we have to swap the two elements

                # to swap, we have to first save the value of elements[j] in a temp var
                temp = elements[j]
                # then, we set the element at j, to the one after it (element at j+1)
                elements[j] = elements[j+1]
                # then, we set the second element as the temp var
                elements[j+1] = temp

                # finally, we set swapped = True, to indeicate that the array is not already sorted
                swapped = True

        # if the swapped variable is not True, that means nothing was swapped, i.e the array is already sorted
        if not swapped:
            # so, just break the loop
            break


if __name__ == "__main__":
    # the elements array
    elements = [5, 9, 2, 1, 67, 34, 88, 34]

    # we sort it, and it returns in place, not a new object
    bubble_sort(elements)

    # print the elements
    print(elements)
