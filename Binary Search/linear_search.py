# import util to get run time of a function
from util.run_time import run_time


# run_time decorator to time get how long the funciton below takes to execeute
@run_time
# function to show linear search, takes in an array to search through, and a value to search for
def linear_search(numbers_arr, search_val):
    # we simply enumerate through the numbers array, keeping track of each element and its index
    for i, el in enumerate(numbers_arr):
        # then, we check if the element equal to our search value
        if el == search_val:
            # if it is, you return the index of that element
            return i

    # if the loop is exited, that means the value was not found, so return -1
    return -1


if __name__ == "__main__":
    # first, we have our sorted array which we want to find a value in
    numbers_arr = [i for i in range(1000001)]
    # then, we have the value we want to find
    search_val = 9999

    # find the index of the value using linear search, then print it out
    search_i = linear_search(numbers_arr, search_val)
    print(f"Linear Search: index of value {search_val} is {search_i}")
