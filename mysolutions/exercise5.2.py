# Andrei Calin

print("\nException handling 1")
# Write a program to read two numbers: x and y from standard input and print the result of x / y.
# If the user inputs invalid data, display an error message and exit gracefully.
x = input("Please enter x = ")
y = input("Please enter y = ")
try:
    z = float(x) / float(y)
except ValueError as ex:
    print(f'Invalid data: "{ex}"!')
except ZeroDivisionError as ex:
    print(f'Invalid operation: "{ex}"!')
else:
    print(f'x / y = {z}')


print("\nException handling 2")
# Modify the previous program so that it asks the user to re-enter data until valid.
while True:
    x = input("\nPlease enter x = ")
    y = input("Please enter y = ")
    try:
        z = float(x) / float(y)
    except ValueError as ex:
        print(f'Invalid data: "{ex}"!')
    except ZeroDivisionError as ex:
        print(f'Invalid operation: "{ex}"!')
    else:
        print(f'x / y = {z}')
        break
