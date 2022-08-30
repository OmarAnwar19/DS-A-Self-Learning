if __name__ == "__main__":
    map = {}

    for i in range(1, 100, 1):
        for j in range(100, 1, -1):
            map[i] = j

    print(map)
