# cleaner quick sort implementation
def quick_sort(arr):
    # get the size of the array
    size = len(arr)

    # if the size of the array is less than or equal to 1 (we have broken the array down to 1)
    if size <= 1:
        # return the array without sorting
        return arr
    # else, we have to sort
    else:
        # first thing we do, is get the pivot
        # this can be any value, but we are using the first number in the array
        # by using pop, we make sure that following sorts do not accidentally sort this number aswell
        pivot = arr.pop()

    # then, we create the arrays for everything to the left and right of the pivot
    left = []
    right = []

    # then, we loop over each item in the array
    for item in arr:
        # if the item is smaller, add it to the left array
        if item < pivot:
            left.append(item)
        # if the item is larger, add it to the right array
        else:
            right.append(item)

    # then, recursively call the function, sorting left, and right, and adding the original pivot in between
    # after we have sorted everything, this will give us a fully sorted array
    return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == "__main__":
    arr = [11, 9, 29, 7, 2, 15, 28]
    print(quick_sort(arr))
