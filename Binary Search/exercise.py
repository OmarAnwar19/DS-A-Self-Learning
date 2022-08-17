def all_occur(arr, search_val):
    indices = []

    for i, el in enumerate(arr):
        if el == search_val:
            indices.append(i)

    return indices


if __name__ == "__main__":
    arr = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
    search_val = 15

    print(
        f"indices of value {search_val}: {all_occur(arr, search_val)}")
