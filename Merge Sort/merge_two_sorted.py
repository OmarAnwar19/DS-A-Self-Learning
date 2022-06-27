def merge_two_sorted_arrays(arr_a, arr_b):
    # create an empty variable for our sorted array
    sorted_array = []

    # get the length of arrays a and b
    len_a = len(arr_a)
    len_b = len(arr_b)

    # in merge sort, you sort from the first element, to the last element
    # you do this using a nested loop, so we create a variable for this loop
    i = j = 0

    # next, we loop through and sort our arrays as long as i and j,
    # are less than the length of the two arrays (so we have not reached the end yet)
    # this loop will exit as soon as we reach the end of either array

    # i and j are the pointers for the two arrays
    while i < len_a and j < len_b:
        # now, we check if the element at array a's pointer is less than the one at array b's pointer
        if arr_a[i] <= arr_b[j]:
            # if so, we first add the element at the current pointer loaction in array a,
            # to the sorted_array
            sorted_array.append(arr_a[i])
            # and we increment i, so we move the pointer for array a over by one
            # (we dont increment j because it had the greater element, so its pointer doesn't move)
            i += 1
            # else (our else statement is automatically if arr_b[j] >= arr_a[i])
        else:
            # we do the same as above, but flip the arrays (append b[j], increment j)
            sorted_array.append(arr_b[j])
            j += 1

    # as noted above, the while statement will exit as soon as either of the arrays reaches its end
    # we can deal with this as follows:
    # as soon as one of the arrays reaches its end, we just place the remaining elements in the array,
    # they are already sorted compared to the left side, so we're good to do this
    while i < len_a:
        # so, if array b reaches its end, we just append each element left in array a into the sorted array
        sorted_array.append(arr_a[i])
        # we cant forget to increment i, so that the loop keeps going
        i += 1

    # same as above, but for array b, and counter j
    while j < len_b:
        sorted_array.append(arr_b[j])
        j += 1

    # finally, return the sorted array
    return sorted_array


if __name__ == "__main__":
    # for this first example, of merging two sorted arrays, we have a and b
    arr_a = [5, 8, 12, 50, 1, 11]
    arr_b = [1, 2, 42, 51]

    # we call the merge_two_sorted_arrays function, passing in arrays a and b
    merged_array = merge_two_sorted_arrays(arr_a, arr_b)

    # finally, we print the merged_array
    print(merged_array)
