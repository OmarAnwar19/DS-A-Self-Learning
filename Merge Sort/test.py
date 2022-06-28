def merge_sort(arr, desc=False):
    if len(arr) <= 1:
        return

    mid = (len(arr)) // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left, desc)
    merge_sort(right, desc)

    merge_two_sorted_arrays(left, right, arr, desc)


def merge_two_sorted_arrays(left, right, arr, desc):
    len_a = len(left)
    len_b = len(right)

    i = j = k = 0

    while i < len_a and j < len_b:
        # assigns the sign based on if desc is True or False
        # left <= right: ascending
        # left >= right: descending
        operator = (left[i] >= right[j]) if desc else (
            left[i] <= right[j])

        if operator:
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

    merge_sort(arr, key="age", desc=False)

    print(arr)
