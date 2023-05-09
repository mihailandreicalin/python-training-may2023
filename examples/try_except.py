name = input("What's your name? ")

try:
    if not name[0].isalpha():
        raise ValueError("Not a name")
    print(f"First letter of name: {name[0]}")
except IndexError as ex:
    print("Exception occurred:", ex)
except NameError:
    print("Undefined variable")
else:
    print("No exception occurred.")
finally:
    print("Executes every time")
