def partition(arr, start, end):
    # first, we have to get the pivot
    # we can start by setting the pivot index as the start
    # this start value will increment by one on each recursive call
    pivot_index = start
    # then, we get the value of the pivot
    pivot = arr[pivot_index]

    # we keep looping, and swapping elements as long as the end counter has not crossed the start counter
    while start < end:
        # while the start index is less than the length of the array,
        # what we do, is that we keep moving the start pointer, until we find a value larger than the pivot
        # --> this is the first part of partitioning
        while start < len(arr) and arr[start] <= pivot:
            start += 1

        # same thing as above, but for the end pointer. while it is greater than the pivot, keep incrementing it
        # we dont do >=, because when they are equal, that means the array is fully sorted
        while arr[end] > pivot:
            end -= 1

        # as soon as incrementing the pointer stops, that means we need to swap the two values
        # so, we swap the values at start and end
        if start < end:
            # swap the value of the array at the start, and end indexes
            arr[start], arr[end] = arr[end], arr[start]

    # finally, after the while loop above exits (when end crosses start)
    # we have to swap the pivot and the end counter element, to place the array in the correct order
    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]

    # so, to get this working recursively, we have to return the new partition middle,
    # this means that on first recursion call, we can then partition left and right based on this middle point
    return end


def quick_sort(arr, start, end):
    # keep recursively partitioning the array as long as the end pointer has not crossed the start pointer
    if start < end:
        # the first thing we have to do is partition the array
        # call the partition function, passing in arr
        # we save the returned end as P_i, this will be the index of the middle of the array
        P_i = partition(arr, start, end)

        # then, we call quick_sort on the left side, starting from the start we passed in until the end we got above
        quick_sort(arr, start, P_i-1)
        # then, we call quick_sort on the right side, starting from the index after the end we got above until the end we passed in
        quick_sort(arr, P_i+1, end)


if __name__ == "__main__":
    # the array that we're going to sort
    arr = [11, 9, 29, 7, 2, 15, 28]

    # then, we can get the start and end pointers
    # start is the index after our pivot_index
    start = 0
    # end is the final index of the array
    end = len(arr) - 1

    # call the function to sort array arr (sorts in place)
    # we also pass in the initial start and end pointers
    quick_sort(arr, start, end)

    # output the array after it is sorted
    print(arr)
