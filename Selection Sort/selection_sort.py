def selection_sort(arr):
    # the first thing we have to do is get the size of the array
    size = len(arr)

    # then, we set our outter loop, from the beginning, until one element before the end
    # --> this is because we always check current, and current+1, so if current is end, there is no current+1
    # --> therefore there is no point to loop until the very end
    for i in range(size-1):
        # next, we have to set the index of the current min_value, this starts as the first index
        min_i = i

        # then, we loop from the element after i, until the end of the array
        for j in range(i+1, size):
            # if the element at the index after i (j=i+1), is less than the array[i]
            if arr[j] < arr[min_i]:
                # set the current index as the index of j
                min_i = j

        # finally, after we have looped over each number after index i, if the min index is i, we dont have to swap
        if i != min_i:
            # otherwise, swap the element at the current index i, with the element at the min_index
            arr[i], arr[min_i] = arr[min_i], arr[i]


if __name__ == "__main__":
    # the array which we want to sort
    arr = [78, 12, 15, 8, 61, 53, 23, 27]

    # call the selection sort function to order it in place
    selection_sort(arr)

    # print the array, now newly sorted
    print(arr)
