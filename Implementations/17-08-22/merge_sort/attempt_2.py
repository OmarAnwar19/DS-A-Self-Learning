def merge_sort(arr):
    size = len(arr)

    if size <= 1:
        return arr

    mid = size // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    sort_arrays(left, right, arr)


def sort_arrays(left, right, arr):
    len_l = len(left)
    len_r = len(right)

    i = j = k = 0

    while i < len_l and j < len_r:
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1

        k += 1

    while i < len_l:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len_r:
        arr[k] = right[j]
        j += 1
        k += 1


if __name__ == "__main__":
    arr = [156, 67, 3, 12, 13, 99, 99, 81, 23, 2, 5]
    merge_sort(arr)
    print(arr)
