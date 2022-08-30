def freq_substr(arr, substr):
    count = 0

    for item in arr:
        if substr in item:
            count += 1

    return round((count / len(arr)), 2)


if __name__ == "__main__":
    arr = ["cakittycat", "tikittytok", "john", "kittey", "kitkakitty"]
    print(freq_substr(arr, "kitty"))
