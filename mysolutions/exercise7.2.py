# Andrei Calin

print("Variable Scope and Lifetime 1")
# Write a function that takes an argument and modifies its value.
# Call the function on a variable defined before the function call
# and print the variable outside the function. Is the variable modified outside the function?


def function1(param):
    """prints number square"""
    param = 'altceva'


ceva = 'ceva'
function1(ceva)
print(f"ceva = {ceva}. The variable was not modified")


print("\nVariable Scope and Lifetime 2")
# Write a function that creates a variable inside the function, modifies it and returns it.
# Call the function and print the variable outside the function. Is the variable modified outside the function?

x = 0
print(f"{x}")

def function2():
    global x  # do not do this
    x = 2
    print = 'ceva'  # shadowing for exercise purpose
    print = 'altceva'
    return print


function_print = function2()
print(f"{print}, {function_print}")
print(f"{x}")
