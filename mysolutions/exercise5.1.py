# Andrei Calin

print("Control flow 1")
# Write a program that prints all integers between 500 and 525 using a for loop.
for i in range(501, 525):
    print(i)

print("\nControl flow 2")
# Do the same as the previous exercise, but this time with a while loop.
x = 501
while x < 525:
    print(x)
    x += 1

print("\nControl flow 3")
# Do the same as exercise 1, but this time print only even numbers.
for i in range(501, 525):
    if i % 2 == 0:
        print(i)

print("\nControl flow 4")
# Write a Python program for checking the speed of drivers.
#
# If speed is less than or equal to 50, it should print "OK".
# Otherwise, for every 5 km above the speed limit (50), it should give the driver one demerit point
# and print the total number of demerit points. For example, if the speed is 60, it should print: "Points: 2".
# If the driver gets more than 12 points, it should print: "License suspended"
# Define a variable called speed and assign an integer value to it.
# After running the program once, change its value and notice the changed output.


def check_speed(speed):
    demerit_points = (speed - 50) // 5
    if demerit_points <= 0:
        print(f"OK")
    elif demerit_points <= 12:
        print(f"Points: {demerit_points}")
    else:
        print(f"License suspended")


check_speed(39)
check_speed(50)
check_speed(60)
check_speed(73)
check_speed(109)
check_speed(114)
check_speed(115)


print("\nControl flow 5")
# Write a Python program which iterates the integers from 1 to 50 and prints their value.
# For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".
# If the number 30 is encountered, break the loop.
#
# Output example: 1 2 Fizz 4 Buzz [...] 13 14 FizzBuzz 16 [...]
for i in range(1, 51):
    if i % 30 == 0:
        break

    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)
