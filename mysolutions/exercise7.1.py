# Andrei Calin

print("Functions 1")
# Write a function that takes a number as a parameter and prints its square.


def function1(param):
    """prints number square"""
    print(param * param)


function1(2)

print("\nFunctions 2")
# Write another function that takes a number as a parameter and returns the square.


def function2(param):
    """returns number square"""
    return param * param


print(f"square of 3 = {function2(3)}")

print("\nFunctions 3")
# Are the results of the two functions above different? Which of the two functions can be used to compute x2 + y2 ?


print(f"Use function2 to compute x2 + y2 = {function2(2) + function2(3)}, where x = 2 and y = 3")


print("\nFunctions 4")
# Write a function that takes a string as an argument and returns a new string with all the vowels removed.


def function4(s):
    """returns a new string with all the vowels removed"""
    new_s = s
    # vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vowels = 'aeiouAEIOU'
    for char in vowels:
        new_s = new_s.replace(char, '')
    return new_s


print(f"new string = {function4('abcdefgaeiouAEIOUd')}")


print("\nFunctions 5")
# Write a function that takes a list and an integer n as arguments
# and returns a new list that contains every n-th element from the original list.


def function5(l, n):
    """returns a new list that contains every n-th element from the original list"""
    new_list = []
    for i in range(n - 1, len(l), n):
        new_list.append(l[i])
    return new_list

def function5_1(l, n):
    """returns a new list that contains every n-th element from the original list"""
    return l[n-1::n]

print(f"new list = {function5([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)}")
print(f"new list = {function5_1([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)} with slice")
print(f"new list = {function5([1, 2, 3, 4, 5, 6, 7, 8, 9], 2)}")
print(f"new list = {function5([1, 2, 3, 4, 5, 6, 7, 8, 9], 10)}")

print("\nFunctions 6")
# Write a function that takes two numbers as arguments and returns their sum, difference, product, and quotient.
# Call the function and assign the result to 4 different variables.


def function6(x, y):
    """returns x, y sum, difference, product, and quotient"""
    return x + y, x - y, x * y, x / y


a, b, c, d = function6(6, 2)

print(f"sum = {a}, difference = {b}, product = {c}, quotient = {d}")


print("\nFunctions 7")
# Write a function that takes any number of strings and an integer n as parameters.
# n should be an optional parameter.
# Return the list of strings longer than n. By default (when n not given), it should return a list containing all words.
#
# E.g.
#
# f('hello', 'hi', 'bye', n=2) -> ['hello', 'bye']
# f('hello', 'hi') -> ['hello', 'hi']
# f() -> []
# f(n=10) -> []


def function7(*strings, n=0):
    """Return the list of strings longer than n"""
    l = []
    for s in strings:
        if len(s) > n:
            l.append(s)
    return l


print(f"list = {function7('hello', 'hi', 'bye', n=2)}")
print(f"list = {function7('hello', 'hi')}")
print(f"list = {function7()}")
print(f"list = {function7(n=10)}")


print("\nFunctions 8")
# Write a function that takes a variable number of lists as arguments
# and returns a new list that contains all the elements from all the input lists.


def function8(*lists):
    """returns a new list that contains all the elements from all the input lists"""
    new_list = []
    for l in lists:
        new_list.extend(l)
    return new_list


print(f"new_list = {function8([1, 2], [4, 6])}")
print(f"new_list = {function8([1, 2], [4, 6], [5, 7])}")
print(f"new_list = {function8()}")


print("\nFunctions 9")
# Write a function that takes a variable number of keyword arguments
# and returns a new dictionary containing only the key-value pairs where the key starts with the letter 'a'.


def function9(**kwargs):
    """returns a new dictionary containing only the key-value pairs where the key starts with the letter 'a'"""
    d = dict()
    for key, val in kwargs.items():
        if key.startswith('a'):
            d[key] = val
    return d


print(f"dictionary = {function9(first_name='Alin', age=25, last_name='Ion', athlet=True)}")


print("\nFunctions 10")
# Print a sentence using the following dictionary, the str.format method and ** unpacking:
#
# country = {
#     "name": "Romania",
#     "population": "19 million",
#     "capital": "Bucharest",
#     "currency": "RON"
# }
# E.g.
#
# Romania has a population of 19 million people. The capital is Bucharest and uses RON as currency.
country = {
    "name": "Romania",
    "population": "19 million",
    "capital": "Bucharest",
    "currency": "RON"
}

print("{name} has a population of {population} people. The capital is {capital} and uses {currency} as currency.".format(**country))


print("\nFunctions 11")
# Using * unpacking and range, print the numbers 1 to 20, separated by commas.
# You will have to provide an argument for print function's sep parameter for this exercise.

print(*range(1, 21), sep=',')


print("\nFunctions 12")
# Modify your code from the previous exercise so that each number prints on a different line.
# You can only use a single print call.

print(*range(1, 21), sep='\n')
