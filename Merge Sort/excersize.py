def merge_sort(arr, desc=False, key="name"):
    if len(arr) <= 1:
        return

    mid = (len(arr)) // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left, desc, key)
    merge_sort(right, desc, key)

    merge_two_sorted_arrays(left, right, arr, desc, key)


def merge_two_sorted_arrays(left, right, arr, desc, key):
    len_a = len(left)
    len_b = len(right)

    i = j = k = 0

    while i < len_a and j < len_b:
        # assigns the sign based on if desc is True or False
        # left <= right: ascending
        # left >= right: descending
        operator = (left[i][key] >= right[j][key]) if desc else (
            left[i][key] <= right[j][key])

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
    arr = [
        {'name': 'vedanth',   'age': 17, 'time_hours': 1},
        {'name': 'rajab', 'age': 12,  'time_hours': 3},
        {'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        {'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]

    merge_sort(arr, key="age", desc=False)

    print(arr)
