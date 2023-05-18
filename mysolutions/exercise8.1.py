# Andrei Calin
import string

print("Comprehensions 1")
# Write a list comprehension that creates a list of numbers from 1 to 20 that are divisible by 3.
print([x for x in range(1, 21) if x % 3 == 0])

print("\nComprehensions 2")
# Write a list comprehension that creates a list of all the vowels in a given string.
print([x for x in 'abcdefgaeiouAEIOUd' if x.lower() in 'aeiou'])

print("\nComprehensions 3")
# Write a list comprehension that creates a list of all the words in a given string that have more than 3 letters.
print([x for x in 'Comprehensions in Python provide us with a short and concise way to construct new iterables (such as lists, set, dictionary etc.)'.split() if len(x) > 3])

print("\nComprehensions 4")
# Create a dict {"a": 97, "b": 98, ... } using comprehension. Use ord built-in to obtain ASCII code. Keys range from "a" to "e".
# >>> import string
# >>> string.ascii_lowercase
# 'abcdefghijklmnopqrstuvwxyz'
# >>> ord('a')
# 97
d1 = {x : ord(x) for x in string.ascii_lowercase if x <= 'e'}
print(d1)

print("\nComprehensions 5")
# Using the dictionary generated above, create another one where you swap keys and values.
d2 = {v: k for k, v in d1.items()}
print(d2)

print("\nComprehensions 6")
# Filter the above dictionary to contain only even keys.
d3 = {k: v for k, v in d2.items() if k % 2 == 0}
print(d3)

print("\nComprehensions 7")
# Can you obtain dictionary from ex. 6 from the given string ("abcde") in a single dict comprehension?
d4 = {ord(x) : x for x in string.ascii_lowercase if x <= 'e' and ord(x) % 2 == 0}
print(d4)
