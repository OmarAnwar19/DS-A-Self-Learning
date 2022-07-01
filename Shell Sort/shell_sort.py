def shell_sort(arr):
    # get the size of the array
    size = len(arr)
    # set the gap of the array = the size of the array // 2 (// = integer division)
    gap = size // 2

    # beacause we are going to keep dividing the gap each time,
    # we have to keep our loop going as long as the gap is greater than 0
    # this means we keep dividing until our gap is = 1, then break the loop
    while gap > 0:
        # in a for loop, you can actually pass in two paramters
        # for i in range (min_val, max_val)
        # so, we start from the gap-th element, until the end of the array
        for i in range(gap, size):
            # we have to start by setting multiple variables
            # the anchor is the point we use to start our comparison,
            # it starts as the element at the index of the gap
            anchor = arr[i]
            # variable j will be used to compare the anchor with its sub array
            # we get the element at j-gap, which will give us the element in the relative beginning of the array
            # since it is = i, let's say our gap starts as 4, j=i-4=0,
            # we then pretty much compare arr[0] with arr[4], and sort if needed
            j = i

            # while j is >= gap, -->
            # to understand this line, we have to refrence j-gap, which gives us our relative_start
            # while j is either >= gap, (so as long as we have not gone below the gap),
            # AND, we still should be swapping: arr[j-gap] (arr[relative_start]) > anchor
            # --> so while the j element is not at 0 yet, and the pointer at the start > anchor value,
            #       we swap the elements, and decrement j by anchor (so we can compare the next part of subarray)
            #       this stops when j either reaches the start of the array, or we reach a value larger than anchor
            while j >= gap and arr[j-gap] > anchor:
                # so, while these two conditions are met,
                # we first swap the current element we are looping at, with the one at the relative start
                # --> this is beacuse it means the one at the start is smaller than the one at the anchor
                arr[j] = arr[j-gap]
                # then, we decrement j, so that we compare the next part of the subarray
                j -= gap

            # lastly, after we are done the loop above, we swap arr[j] (which is now arr[0]), with our anchor element
            arr[j] = anchor

        # the final thing we have to do is divide our gap by 2, so we can sort the next subarray
        gap = gap // 2


if __name__ == "__main__":
    # the array to be sorted
    arr = [21, 38, 29, 17, 4, 25, 11, 32, 9]

    # calling the shell sort function to sort the array in place
    shell_sort(arr)

    # printing the array
    print(arr)
