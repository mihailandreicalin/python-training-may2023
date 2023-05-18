# Andrei Calin

print("Built-in functions 1")
# Write a function filter_short_words(word_list, n) that returns the words in word_list shorter than n.
# Use filter built-in function and a lambda function.


def filter_short_words(word_list, n):
    return filter(lambda x: len(x) < n, word_list)


for item in filter_short_words("These are some of the most important built-in functions that receive iterables as parameters and produce iterables.".split(), 4):
    print(item)


print("\nBuilt-in functions 2")
# Write a function that takes a list of tuples, where each tuple contains two integers,
# and returns a new list containing the product of the two integers in each tuple.
# Use the map function and a lambda function to implement this.


def function2(l):
    return map(lambda x: x[0] * x[1], l)


touple_list = [(1, 2), (2, 3), (3, 5), (5, 8)]
for item in function2(touple_list):
    print(item)

print("\nBuilt-in functions 3")
# Write a function that takes a list of integers
# and returns a new list containing the squares of all even numbers in the original list.
# Use the filter, map, and lambda functions to implement this.


def function3(l):
    even_numbers = filter(lambda x: x % 2 == 0, l)
    return map(lambda x: x * x, even_numbers)


l = [1, 2, 2, 3, 3, 5, 5, 8]
for item in function3(l):
    print(item)


print("\nBuilt-in functions 4")
# Write a function that receives any number of strings
# and returns the list of unique strings ordered by number of appearances
# (most frequent → least frequent). Use sorted built-in function.
#
# E.g. f('hello', 'there', 'hello', 'hi', 'hi', 'hello') -> ['hello', 'hi', 'there']


def function4(*s):
    d = {}
    for key in s:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    print(d)
    return sorted(d.keys(), key=lambda key: d[key], reverse=True)


def function5(*string_list):
    return sorted(set(string_list), key=lambda elem: string_list.count(elem), reverse=True)


# for item in function4('hello', 'there', 'hello', 'hi', 'hi', 'hello'):
print(function4('hello', 'there', 'hello', 'hi', 'hi', 'hello'))
print(function5('hello', 'there', 'hello', 'hi', 'hi', 'hello'))
