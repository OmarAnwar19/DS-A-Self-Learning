def partition(arr):
    if len(arr) <= 1:
        return

    mid = (len(arr)) // 2
    left = arr[:mid]
    right = arr[mid:]

    partition(left)
    partition(right)

    merge_sort(left, right, arr)


def merge_sort(left, right, arr):
    len_a = len(left)
    len_b = len(right)

    i = j = k = 0

    while i < len_a and j < len_b:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1

        k += 1

    while i < len_a:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len_b:
        arr[k] = right[j]
        j += 1
        k += 1


if __name__ == "__main__":
    arr = [5, 90, 72, 15, 122, 34, 56, 12, 1]

    merge_sort(arr)

    print(arr)
