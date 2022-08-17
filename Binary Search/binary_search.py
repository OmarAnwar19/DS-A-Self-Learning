# import util to get run time of a function
from util.run_time import run_time


# run_time decorator to time get how long the funciton below takes to execeute
@run_time
# function to show binary search ITERATIVELY
# takes in an array to search through, and a value to search for
def binary_search_iterative(numbers_arr, search_val):
    # the first thing we have to do is get the index of the middle element in the array
    # we can do this by getting the starting index of the left side (0 since array starts at 0)
    left_i = 0
    # and then get the index of the right side (the last index in the array)
    right_i = len(numbers_arr)-1

    # then, we loop while the left index is less than the right index
    # --> loop until we can no longer divide the array in to partitions
    while left_i <= right_i:
        # we can then get the middle index by adding the left and right indexes, and divide them by 2
        mid_i = (left_i + right_i) // 2
        # we can then get the actual middle value by accessing our array at the mid_i
        mid_val = numbers_arr[mid_i]

        # now, we can check if the middle value is the same as the search value
        if mid_val == search_val:
            # if it is, then return the index of the middle value
            return mid_i

        # otherwise, if the middle value is less than the search value,
        # that means that the search value is in the right partition of our array,
        # so, set the left index as the middle_index + 1
        # (the +1 is so that we dont check middle index again, since we already know its not the search value)
        if mid_val < search_val:
            left_i = mid_i + 1
        # otherwise, that means that the search value is greater than the mid index,
        # so that means the value is in the left partition, so we can set the right index as the middle index -1
        else:
            right_i = mid_i - 1

    # if the loop exits, that means the value was not found, so just return -1
    return -1

# function to show binary search RECURSIVELY
# takes in an array to search through, and a value to search for, aswell as the current left and right index


def binary_search_recursive(numbers_arr, search_val, left_i, right_i):
    # our base case is when the right index < left index, we return -1
    # this happens when the array can no longer be partitioned into two halfs
    if right_i < left_i:
        return -1

    # we can then get the middle index by adding the left and right indexes, and divide them by 2
    mid_i = (left_i + right_i) // 2

    # before we start preforming the recursive calls, we have to check that mid_i is valid
    # if mid_i is either greater or less than the size of the array, that means it is an invalid search value
    if mid_i >= len(numbers_arr) or mid_i < 0:
        # so, just return -1 before doing anything else
        return -1

    # we can then get the actual middle value by accessing our array at the mid_i
    mid_val = numbers_arr[mid_i]

    # now, we can check if the middle value is the same as the search value
    if mid_val == search_val:
        # if it is, then return the index of the middle value
        return mid_i

    # otherwise, if the middle value is less than the search value,
    # that means that the search value is in the right partition of our array,
    # so, set the left index as the middle_index + 1
    # (the +1 is so that we dont check middle index again, since we already know its not the search value)
    if mid_val < search_val:
        left_i = mid_i + 1
    # otherwise, that means that the search value is greater than the mid index,
    # so that means the value is in the left partition, so we can set the right index as the middle index -1
    else:
        right_i = mid_i - 1

    # finally, once we have updated either our left or right indexes, call the function recursively with the updated values
    return binary_search_recursive(numbers_arr, search_val, left_i, right_i)


if __name__ == "__main__":
    # first, we have our sorted array which we want to find a value in
    numbers_arr = [i for i in range(1000001)]
    # then, we have the value we want to find
    search_val = 9999

    # find the index of the value using iterative binary search, then print it out
    search_i = binary_search_iterative(numbers_arr, search_val)
    print(
        f"Binary Search (iterative): index of value {search_val} is {search_i}")

    # find the index of the value using recursive binary search, then print it out
    search_i = binary_search_recursive(
        numbers_arr, search_val, 0, len(numbers_arr)-1)
    print(
        f"Binary Search (recursive): index of value {search_val} is {search_i}")
