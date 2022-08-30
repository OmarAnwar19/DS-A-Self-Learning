def merge_sort(arr):
    size = len(arr)

    if size <= 1:
        return arr

    mid = size // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_arrays(left, right, arr)


def merge_arrays(left, right, arr):
    len_l = len(left)
    len_r = len(right)

    l = r = k = 0

    while l < len_l and r < len_r:
        if left[l] <= right[r]:
            arr[k] = left[l]
            l += 1
        else:
            arr[k] = right[r]
            r += 1

        k += 1

    while l < len_l:
        arr[k] = left[l]

        l += 1
        k += 1

    while r < len_r:
        arr[k] = right[r]

        r += 1
        k += 1


if __name__ == "__main__":
    arr = [156, 67, 3, 12, 13, 99, 99, 81, 23, 2, 5]

    merge_sort(arr)

    print(arr)
