def sum(n):
    if n <= 1:
        return n

    return n + sum(n-1)


def fib(n):
    if n <= 1:
        return n

    return fib(n-1) + fib(n-2)


def to_string(n, base):
    convStr = "0123456789ABCDEF"

    if n < base:
        return convStr[n]
    else:
        return to_string(n//base, base) + convStr[n % base]


def list_sum(arr, i=0, total=0):
    if i >= len(arr):
        return total

    if isinstance(arr[i], list):
        for num in arr[i]:
            total += num
    else:
        total += arr[i]

    return list_sum(arr, i+1, total)


def factorial(n):
    if n <= 1:
        return n

    return n * factorial(n-1)


def sum_digits(n):
    if n == 0:
        return 0

    return n % 10 + sum_digits(int(n / 10))


def sum_series(n):
    if n < 1:
        return 0

    # just n - 2 because n is already n - 2,
    # so the new sum_series(n-2) is n-4, then n-6 etc.. in comparison to the original n
    return n + sum_series(n - 2)


def harmonic_sum(n):
    if n < 2:
        return 1

    return 1 / n + (harmonic_sum(n - 1))


def geometric_sum(n):
    if n < 0:
        return 0

    return 1 / (pow(2, n)) + geometric_sum(n - 1)


def power(n, x):
    # power(3,4) = 3*3*3*3
    if n > x+1:
        return n

    return n * power(n, x-1)


def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


if __name__ == "__main__":
    print(f"**to_string: {to_string(2835, 16)}")
    print(f"sum: {sum(16)}")
    print(f"fib: {fib(6)}")
    print(f"list_sum: {list_sum([1, 2, [3, 4], [5, 6]])}")
    print(f"factorial: {factorial(6)}")
    print(f"sum_digits: {sum_digits(45)}")
    print(f"sum_series: {sum_series(6)}")
    print(f"harmonic_sum: {harmonic_sum(12)}")
    print(f"geometric_sum: {geometric_sum(12)}")
    print(f"power: {power(3,6)}")
    print(f"gcd: {gcd(8,12)}")
