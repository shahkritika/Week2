# A1: Timing decorator

import time
import functools

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"'{func.__name__}' ran in {end - start:.6f} seconds")
        return result
    return wrapper


@timer
def slow_function():
    time.sleep(1)
    print("Done!")

@timer
def add(a, b):
    return a + b


# --- Test ---
slow_function()
result = add(3, 5)
print(f"Result: {result}")

