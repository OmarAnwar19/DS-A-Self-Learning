import statistics


def insertion_sort(elements):
    size = len(elements)

    for i in range(1, size):
        curr = elements[i]
        prev = i-1

        while prev >= 0 and curr < elements[prev]:
            elements[prev+1] = elements[prev]
            prev = prev-1
            elements[prev+1] = curr

        median = statistics.median(elements)

        print(elements, median)


if __name__ == "__main__":
    elements = [21, 38, 29, 17, 4, 25, 11, 32, 9]

    insertion_sort(elements)
