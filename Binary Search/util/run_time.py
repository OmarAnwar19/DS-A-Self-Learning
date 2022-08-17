import time


def run_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        print(
            f"function '{func.__name__}' took {str((end-start)*1000)} milliseconds to execute.")

        return result

    return wrapper
