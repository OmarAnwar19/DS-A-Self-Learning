# normal merge sort is a recursive function, so we have to keep that in mind
def merge_sort(arr):
    # first, we can get the size of the array
    size = len(arr)

    # like any recursive function, we first have to make our base case
    # the base case for merge sort is if the length of the array is 0 or 1
    # this will occur if the array is on the first step of merge after divide
    if size <= 1:
        # so, according to how recursion works, we pass in the left side
        # then the right side, and they will keep getting divided into left and right
        # until the length of the array is less than or equal to 1,
        # this means that our array is fully divided into seperate arrays of size 1
        # we then break out of the recursive loop, but we dont return anything
        return

    # for merge sort, we have to divide the array in half over and over,
    # we can do this by splitting the array into left and right
    # to do this, we first have to get the mid point of the array
    mid = size // 2
    # then, we can get the left and right side of the array
    # left is from the beginning (start): until the mid point (start):mid
    left = arr[:mid]
    # right is from the mid point mid: until the end mid:(end)
    right = arr[mid:]

    # then, we have to recursively call the function onto the left and right side
    # this will keep dividing up the array into a left and right side, until
    # each side is a bunch of arrays of length 1
    # by not assigning them a value, it is sorting arr in place
    merge_sort(left)
    merge_sort(right)

    # finally, we have to call the merge_two_sorted_arrays function,
    # this will take our one array, split up into left and right side,
    # and then merge and sort them
    # we also pass in arr, so that we can save left and right back into arr after we merge sort them
    merge_two_sorted_arrays(left, right, arr)


# after merge sort breaks up the array, it calls this function to sort it again
def merge_two_sorted_arrays(left, right, arr):
    # get the length of arrays a and b
    len_a = len(left)
    len_b = len(right)

    # in merge sort, you sort from the first element, to the last element
    # you do this using a nested loop, so we create variables i,j, and k,
    # these act as pointers for the left and right array, and the original array (arr) accordingly
    i = j = k = 0

    # next, we loop through and sort our arrays as long as i and j,
    # are less than the length of the two arrays (so we have not reached the end yet)
    # this loop will exit as soon as we reach the end of either array

    # i and j are the pointers for the two arrays
    while i < len_a and j < len_b:
        # now, we check if the element at the left array's pointer is less than the one at right array's pointer
        if left[i] <= right[j]:
            # if so, we can then append it into the correct position in our original array k
            arr[k] = left[i]
            # and we increment i, so we move the pointer for array a over by one,
            # (we dont increment j because it had the greater element, so its pointer doesn't move)
            i += 1
            # else (our else statement is automatically if right[j] >= left[i])
        else:
            # we do the same as above, but flip the arrays (append left[j], increment j)
            arr[k] = right[j]
            j += 1

        # finally, after each time we order two elements, we have to increment k,
        # this is so next time we insert, the pointer for our original array arr is one to the right
        k += 1

    # as noted above, the while statement will exit as soon as either of the arrays reaches its end
    # we can deal with this as follows:
    # as soon as one of the arrays reaches its end, we just place the remaining elements in the array,
    # they are already sorted compared to the left side, so we're good to do this
    while i < len_a:
        # so, if array b reaches its end, we just append each element left in array a into the original array
        arr[k] = left[i]
        # we cant forget to increment i, so that the loop keeps going,
        # we also increment k so that next time we insert an element into it, it is in the correct spot
        i += 1
        k += 1

    # same as above, but for array b, and counter j
    while j < len_b:
        arr[k] = right[j]
        j += 1
        k += 1


if __name__ == "__main__":
    # for this example, we only sort one, unsorted array
    arr = [10, 3, 15, 7, 8, 23, 98, 112, 29]

    # we call the merge_sort function, passing in arr from above
    merge_sort(arr)

    # finally, we print the original array, now sorted
    print(arr)
