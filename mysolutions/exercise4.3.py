# Andrei Calin

# Boolean 4.1
print('Boolean 4.1')
print('Write an expression that returns True'
      ' if x is strictly greater than 4.3 and smaller or equal to 7.9, or if it is 3,'
      ' and try changing x to see if it works:')


def expression(x):
    result = (4.3 < x <= 7.9) or x == 3
    print(f"x = {x}, expression is: {result}")


expression(6.5)
expression(3)
expression(3.1)


# Boolean 4.2
print('\n')
print('Boolean 4.2')
print('Given two integers, x and y, create a boolean which is True only if one of them is 100 or if their sum is 100.')


def expression(x, y):
    result = x == 100 or y == 100 or x + y == 100
    print(f"x = {x}, y = {y}, expression = {result}")


expression(100, 7)
expression(5, 100)
expression(45, 55)
expression(10, 45)

# Boolean 4.3
print('\n')
print('Boolean 4.3')
print('Try out the following operations in the Python shell:')
print(f"True and 'True' is {True and 'True'} needs to evaluate the second operand "
      f"and because literal 'True' is a non empty string => 'True'")
print(f"0 or False is {0 or False}, needs to evaluate the second operand because 0 of any numeric type is False"
      f" and returns the value of the second operand => False")

# Boolean 4.4
print('\n')
print('Boolean 4.4')
print("Let's assume that variable age was initialized with a value returned by a function that is generally a number, "
      "but can also be None. How can you make sure that age is always a number (default value 0)?")
age = 10
print(age)
age = None
print(age or 0)  # print expression that contains `age` and returns 0
