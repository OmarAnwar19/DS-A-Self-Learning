import heapq


# function to heapify a normal array
def heapify(arr):
    # create an empty heap
    heap = []

    # push each item in input arr to that heap
    for element in arr:
        heapq.heappush(heap, element)

    return heap


# funcion to sort a heap
def heap_sort(heap):
    # create a new array for the sorted heap
    sorted = []

    # while the heap still has elements
    while heap:
        # add the top element of the heap to the sorted array
        sorted.append(heapq.heappop(heap))

    # return the sorted array
    return sorted


if __name__ == "__main__":
    # create a normal array
    arr = [13, 21, 15, 5, 26, 4, 17, 18, 24, 2]
    # heapify the array
    heap = heapify(arr)

    # call heap_sort to sort the newly created heap
    sorted = heap_sort(heap)

    # print the array
    print(sorted)
