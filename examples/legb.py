X = 100


def func(a):
    b = 11
    # global X
    # X = 0

    def inner(c):
        d = 111
        # nonlocal a
        # a = 0

        print('-- inner function --')
        print("Built-in names:", len, str, ValueError)
        print("Global names:", X, func, MyClass)
        print("Enclosing names:", a, b, inner)
        print("Local names:", c, d, end="\n\n")

    inner(222)

    print('-- func function --')
    print("Built-in names:", len, str, ValueError)
    print("Global names:", X, func, MyClass)
    print("Local names:", a, b, inner, end="\n\n")


class MyClass:
    pass


func(22)

print('-- global --')
print("Built-in names:", len, str, ValueError)
print("Global names:", X, func, MyClass)
