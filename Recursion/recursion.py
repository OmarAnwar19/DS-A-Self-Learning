# sum can either be done iteratively, or recursively
def sum(n):
    # recursively, we first have to decide a base case,
    # if n <= 1, return n, so that we exit our recursive loop when n is 1
    if n <= 1:
        return n

    # otherwise, add n, and n-1 by calling sum(n-1)
    return n + sum(n-1)


# fibbonaci sequence is an another example of a recursive function
def fib(n):
    # we have our base case, which is if n is either 0 or 1, return n
    if n <= 1:
        return n

    # otherwise, you call fib again, with n-1 + n-2
    return fib(n-1) + fib(n-2)


if __name__ == "__main__":
    # print the sum(n)
    print(sum(5))

    # print the fibbonaci number at 5
    print(fib(5))
