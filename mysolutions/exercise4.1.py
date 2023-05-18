a = 12345
print("4.1 integer number =", a, "last digit =", a % 10, '\n')

b = 789
suma = 0

while (b // 10) > 0:
    suma = suma + b % 10
    b = b // 10
suma = suma + b
print("4.2 integer number =", b, "last digit =" + str(suma), '\n')

n = 345
print("4.3 minutes=", n, " \n", n // 60, n % 60)

