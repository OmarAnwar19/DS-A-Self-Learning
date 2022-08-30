if __name__ == "__main__":
    arr = [i for i in range(15)]

    print(arr)

    del(arr[6])
    arr[0] = 999

    print(arr)
