# Andrei Calin
import random

print("Iterators 1")
# Write a generator function that takes a list of numbers and yields only the even numbers from the list.


def gen(l):
    for x in l:
        if x % 2 == 0:
            yield x


for num in gen([1, 2, 3, 4, 5, 6, 7, 8, 9]):
    print(num)


print("\nIterators 2")
# Create a generator function that receives a parameter max_nr and yields a random number between 1 and max_nr, indefinitely.
# >>> import random
# >>> random.randint(1, 10)  # returns a random integer between 1 and 10
# 1
# >>> random.randint(1, 10)
# 10
# >>> random.randint(1, 10)
# 6


def gen2(max_nr):
    # while True:
        yield random.randint(1, max_nr)


for num in gen2(4):
    print(num)

print("\nIterators 3")
# Write a generator function that yields unique elements from an iterable received as parameter.


def gen3(l):
    s = set(l)
    for x in s:
        yield x


def gen4(l):
    l2 = []
    for x in l:
        if x not in l2:
            l2.append(x)
            yield x


print("solution 1")
for num in gen3([1, 1, 3, 3, 5, 5, 7, 8, 7]):
    print(num)

print("solution 2")
for num in gen4([1, 1, 3, 3, 5, 5, 7, 8, 7]):
    print(num)
