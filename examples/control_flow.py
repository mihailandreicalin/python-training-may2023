x = 561

while x > 0:
    print(x % 10)
    x //= 10


for i in range(3):
    print(i)

for i in range(3, 10):
    print(i)

for i in range(3, 10, 2):
    print(i)

x = 34279126
while x > 0:
    last_digit = x % 10
    if last_digit == 1:
        break
    print(last_digit)
    x //= 10

x = 1102413111543
while x > 0:
    last_digit = x % 10
    x //= 10
    if last_digit == 1:
        continue
    print(last_digit)
