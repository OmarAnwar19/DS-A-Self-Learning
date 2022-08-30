# iterative
def iterativeBinarySearch(array, x, low, high):
    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = low + (high - low)//2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1

# recursive


def recursiveBinarySearch(array, x, low, high):
    if high >= low:

        mid = low + (high - low)//2

        # If found at mid, then return it
        if array[mid] == x:
            return mid

        # Search the left half
        elif array[mid] > x:
            return recursiveBinarySearch(array, x, low, mid-1)

        # Search the right half
        else:
            return recursiveBinarySearch(array, x, mid + 1, high)

    else:
        return -1


# question template
def binary_search(array) -> int:
    def condition(value) -> bool:
        pass

    # could be [0, n], [1, n] etc. Depends on problem
    left, right = 0, len(array)-1

    while left < right:
        mid = left + (right - left) // 2

        if condition(mid):
            right = mid
        else:
            left = mid + 1

    return left


if __name__ == "__main__":
    array = [3, 4, 5, 6, 7, 8, 9]

    iterative = iterativeBinarySearch(array, 4, 0, len(array)-1)
    recursive = recursiveBinarySearch(array, 4, 0, len(array)-1)

    print(f"iterative: {iterative}, recursive: {recursive}")
