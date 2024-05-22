import functools
import time

def time_it(func):
    @functools.wraps(func)
    def wrapper_time_it(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Function {func.__name__} took {(end - start)*1000:0.3f}ms")
    return wrapper_time_it

@time_it
def print_10_times(string):
    for _ in range(10):
        print(string)

print_10_times("Some random string")