def decrement(x, step=1):
    return x - step


# positional arguments calls
print(decrement(10))
print(decrement(10, 2))

# keyword arguments calls
print(decrement(10, step=3))
print(decrement(step=3, x=10))


def varargs(req, *args, req_kw, opt=0, **kwargs):
    print(req, req_kw, opt)

    print(args, type(args))
    print(kwargs, type(kwargs), end="\n\n")


varargs(10, req_kw=100)
varargs(10, "hello", req_kw=100)
varargs(10, "hello", "world", 1, 2, 3, req_kw=100)

varargs(10, req_kw=100, name="Anna")
varargs(10, name="Anna", age=10, height=1.5, req_kw=100)


# Argument unpacking
l = [5, 1, 4, 7, 1]
print(l)  # called print with one argument of type list
print(*l)  # called print with len(l) arguments

person = {"name": "Jane", "age": 20, "occupation": "student"}
print("{name} is {age} years old. {name} is a {occupation}.".format(**person))


# type hints
def greet(name: str):
    # if not isinstance(name, str):
    #     raise TypeError("Expected str argument")
    print(f"hello, {name}")


greet(10)
greet("Anna")
