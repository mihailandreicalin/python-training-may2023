# Andrei Calin
import functools
import time

print("Decorators 1")
# Write a decorator that computes (and displays) execution time for a function.
# Hint: time.time() function returns current time in seconds.


def funct_decorator(func):
    def inner(*args, **kwargs):
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        print(f"execution time {end-start}s")
        return value
    return inner


@funct_decorator
def funct_sleep():
    time.sleep(1)


@funct_decorator
def funct_compute(x, y):
    prod = 1
    for i in range(x):
        for j in range(y):
            prod *= i * y
    return prod


funct_sleep()
funct_compute(123, 345)

print("\nDecorators 2")
# Write a decorator function that takes a function as an argument
# and prints the number of times the function has been called.


def funct_decorator(func):
    """Decoration Function"""
    calls = 0

    @functools.wraps(func)
    def inner(*args, **kwargs):
        """inner Function"""
        nonlocal calls
        calls += 1
        value = func(*args, **kwargs)
        print(f"called {calls} time")
        return value
    return inner


@funct_decorator
def funct_d():
    """Decorated Function"""
    return time.time()


@funct_decorator
def funct_e():
    time.sleep(1)
    return time.time()


print(f"function d result: {funct_e()}")
print(f"function d result: {funct_d()}")
print(f"function d result: {funct_d()}")
print(f"function d result: {funct_d()}")

print(funct_d, funct_d.__doc__)
