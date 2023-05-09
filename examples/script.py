"""This is a module exemplifying some basic Python concepts"""

print("hello world")  # inline comment
x = 5
print(x)

# implicit line joining
print("/Users/iulia/PycharmProjects/python-training-may2023/venv/bin/python "
      "/Users/iulia/PycharmProjects/python-training-may2023/examples/script.py")

# explicit line joining
command = "/Users/iulia/PycharmProjects/python-training-may2023/venv/bin/python" + \
          " /Users/iulia/PycharmProjects/python-training-may2023/examples/script.py"
print(command)

hour = 15
if hour < 18:
    greeting = "Good day"
else:
    greeting = "Good evening"
print(greeting)

print(hour)

text = "Say \"hello\" to Jim. \nBackslash: \\"
print(text)

# comparison to None, True, False should be done with `is` operator
print(text is None)
