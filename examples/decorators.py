import functools


def make_pretty(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print("I got decorated")
        # print(f"func={func.__name__}, args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)

    return inner


@make_pretty
def ordinary():
    print("I am ordinary")


# ordinary = make_pretty(ordinary)  # make_pretty.<locals>.inner

# make_pretty.<locals>.inner()
ordinary()


@make_pretty
def greet(name):
    """Greets a person"""
    print(f"Hello, {name}!")


greet("Anna")
print('greet function attributes:', greet.__name__, greet.__doc__)


@make_pretty
def decrement(nr, step=1):
    return nr - step


print('decrement function attributes:', decrement.__name__)
# make_pretty.<locals>.inner(10)
print("Decremented value:", decrement(10))
print("Decremented value:", decrement(10, step=2))
