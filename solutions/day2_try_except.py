# Write a program to read two numbers: x and y from standard input and print
# the result of x / y. If the user inputs invalid data, display an error message
# and exit gracefully.

while True:
    inp1 = input("Type first number: ")
    inp2 = input("Type second number: ")
    try:
        final = int(inp1) / int(inp2)
    except ValueError:
        print("Not a number!")
    except ZeroDivisionError:
        print('Cannot divide by 0')
    else:
        print(f'Result = {final}. Good job!')
        break
