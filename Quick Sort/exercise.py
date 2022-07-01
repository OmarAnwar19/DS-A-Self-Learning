def partition(arr, start, end):
    pivot_index = end
    pivot = arr[pivot_index]

    p_index = start

    for i in range(start, end):
        if arr[i] <= pivot:
            arr[p_index], arr[i] = arr[i], arr[p_index]
            p_index = i+1

    arr[p_index], arr[end] = arr[end], arr[p_index]

    return p_index


def quick_sort(arr, start, end):
    if start < end:
        P_i = partition(arr, start, end)

        quick_sort(arr, start, P_i-1)
        quick_sort(arr, P_i+1, end)


if __name__ == "__main__":
    arr = [11, 9, 29, 7, 2, 15, 28]

    start = 0
    end = len(arr) - 1

    quick_sort(arr, start, end)

    print(arr)
