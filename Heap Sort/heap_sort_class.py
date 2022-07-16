def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def max_heapify(arr, i=0):
    L_i = 2*i+1
    R_i = 2*i+2
    max_i = i

    if L_i < len(arr) and arr[max_i] < arr[L_i]:
        max_i = L_i

    if R_i < len(arr) and arr[max_i] < arr[R_i]:
        max_i = R_i

    if max_i != i:
        swap(arr, i, max_i)
        max_heapify(arr, max_i)


def heap_sort(arr):
    sz = len(arr)

    for i in range(len(arr)):
        max_heapify(arr, i)

    for j in range(len(arr)-1, 0, -1):
        swap(arr, 0, j)
        max_heapify(arr, j)

    max_heapify(arr, 0)
    max_heapify(arr, 0)
    max_heapify(arr, 0)
    max_heapify(arr, 0)


if __name__ == "__main__":
    arr = [10, 45, 23, 1, 67, 2]

    heap_sort(arr)

    print(arr)
