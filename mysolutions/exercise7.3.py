# Andrei Calin
import function_exercises.numbers
from function_exercises.numbers import function2 as square
from function_exercises.numbers import function6
from function_exercises.strings import function4
from function_exercises.strings import function7
from function_exercises.strings import function9

from function_exercises.lists import function5
from function_exercises.lists import function5_1
from function_exercises.lists import function8

# print("Modules and Packages 1")
# Create a Python package functions_exercises with three module in it: numbers, strings and lists
# and place all functions created for the Functions chapter in the three modules.
# Modules shouldn't print anything when imported,
# so make sure you placed all code that runs the functions under the appropriate condition.

print("\nModules and Packages 2")
# Create a Python module outside functions_exercises package where you import and call some of these functions.

print("Functions 1")
function_exercises.numbers.function1(2)

print("\nFunctions 2")
print(f"square of 3 = {square(3)}")

print("\nFunctions 3")
print(f"Use function2 to compute x2 + y2 = {square(2) + square(3)}, where x = 2 and y = 3")

print("\nFunctions 4")
print(f"new string = {function4('abcdefgaeiouAEIOUd')}")

print("\nFunctions 5")
print(f"new list = {function5([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)}")
print(f"new list = {function5_1([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)} with slice")
print(f"new list = {function5([1, 2, 3, 4, 5, 6, 7, 8, 9], 2)}")
print(f"new list = {function5([1, 2, 3, 4, 5, 6, 7, 8, 9], 10)}")

print("\nFunctions 6")
a, b, c, d = function6(6, 2)
print(f"sum = {a}, difference = {b}, product = {c}, quotient = {d}")

print("\nFunctions 7")
print(f"list = {function7('hello', 'hi', 'bye', n=2)}")
print(f"list = {function7('hello', 'hi')}")
print(f"list = {function7()}")
print(f"list = {function7(n=10)}")

print("\nFunctions 8")
print(f"new_list = {function8([1, 2], [4, 6])}")
print(f"new_list = {function8([1, 2], [4, 6], [5, 7])}")
print(f"new_list = {function8()}")

print("\nFunctions 9")
print(f"dictionary = {function9(first_name='Alin', age=25, last_name='Ion', athlet=True)}")
