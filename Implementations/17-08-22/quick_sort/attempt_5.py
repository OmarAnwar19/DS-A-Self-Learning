def quick_sort(arr):
    size = len(arr)

    if size <= 1:
        return arr

    pivot = arr.pop()
    left, right = [], []

    for item in arr:
        if item <= pivot:
            left.append(item)
        else:
            right.append(item)

    return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == "__main__":
    arr = [156, 67, 3, 12, 13, 99, 99, 81, 23, 2, 5]
    arr = quick_sort(arr)
    print(arr)
