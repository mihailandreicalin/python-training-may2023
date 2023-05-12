from datetime import date


# 1. Create a BankAccount class that receives two parameters on initialisation:
# bank name (str)
# balance (int)
# 1.A. Create two methods in this class, one to withdraw money and another one
# to deposit money into the account. The withdrawal method will not allow
# withdrawing more money than available: it will print a message and not change
# the balance.

class InsufficientFundsException(Exception):
    pass


class BankAccount:
    def __init__(self, bank_name, balance):
        self.bank_name = bank_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsException('insufficient funds')
        self.balance -= amount


# 1.B. Create a BankAccount instance and test the two methods with different
# inputs.

bank_acc = BankAccount('BRD', 100)  # create instance
print('Initial balance:', bank_acc.balance)
bank_acc.deposit(50)  # call deposit() method
print('Balance after depositing 50:', bank_acc.balance)  # should be 150
bank_acc.withdraw(70)  # call withdraw() method
print('Balance after withdrawing 70:', bank_acc.balance)  # should be 80
try:
    bank_acc.withdraw(100)  # should raise exception
except InsufficientFundsException as ex:
    print("Trying to withdraw 100:", ex)
print('Balance after trying to withdraw 100:', bank_acc.balance)

# 3. Create a class called Rectangle with attributes width and height. Add
# methods get_area and get_perimeter that calculate and return the area and
# perimeter of the rectangle.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f'Rectangle with width={self.width} and height={self.height}'


rectangle = Rectangle(5, 3)
area = rectangle.get_area()
perimeter = rectangle.get_perimeter()

print(f'{rectangle} has area of {area} and perimeter of {perimeter}.')


# 4. Create a class Employee with three instance attributes:
# name
# bank_account (it should be a BankAccount object; pass an already created
# BankAccount instance at Employee initialisation)
# salary (default 0)
# A. Write a method raise_salary that receives a parameter percent that should
# be one of the following values: 5, 10, 20. Raise a ValueError if another value
# is received by this method. The raise_salary method should raise the salary
# with 5%, 10% or 20%.
# B. Create a method receive_salary that will deposit in the employee's bank
# account an amount equal to its salary.
# C. Use a property for salary management. Salary should be set only on
# initialisation; you shouldn't be able to set the salary from outside the
# class.

class Employee:
    ACCEPTED_RAISE_VALUES = (5, 10, 20)

    def __init__(self, name: str, bank_account: BankAccount, salary: int = 0):
        self.name = name
        self.bank_account = bank_account
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    def raise_salary(self, percent):
        if percent not in self.ACCEPTED_RAISE_VALUES:
            raise ValueError(f'Invalid raise value: {percent}%')
        self._salary += (percent / 100) * self._salary

    def receive_salary(self):
        self.bank_account.deposit(self._salary)


# 4.D. Create an Employee instance and call raise_salary and receive_salary on
# it.
emp = Employee("John Doe", bank_acc, 1000)
print("Initial salary:", emp.salary)
emp.raise_salary(10)
print("Salary after 10% raise:", emp.salary)
emp.receive_salary()
print("Balance after receiving salary:", emp.bank_account.balance)
try:
    emp.raise_salary(60)
except ValueError as ex:
    print(f"Trying to raise salary with 60%: {ex}")

try:
    emp.salary = 2000
except AttributeError as ex:
    print("Trying to set salary attribute:", ex)


# 5. Create a class called Book with title, author, and year as attributes.
# Add a method is_recent that returns True if the book was published in the last
# 10 years and False otherwise. Create an instance and call the method on it.

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def is_recent(self):
        return (date.today().year - self.year) <= 10


book = Book('The Testaments', 'Margaret Atwood', 2019)
print('Book is recent:', book.is_recent()) # Output: True


# Then, add @property decorator to the method definition.
# How does the call change?
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    @property
    def is_recent(self):
        return (date.today().year - self.year) <= 10


book = Book('The Testaments', 'Margaret Atwood', 2019)
print('Book is recent:', book.is_recent) # Output: True


# 5. Create a CreditBankAccount class that inherits BankAccount and receives
# one extra argument at initialisation which allows for the balance to go below
# zero (but not under -overdraft):
# overdraft (int)
# A. Override parent withdraw method so that the new rule is implemented.

class CreditBankAccount(BankAccount):
    def __init__(self, bank_name, balance, overdraft):
        super().__init__(bank_name, balance)
        self.overdraft = overdraft

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft:
            raise InsufficientFundsException('overdraft exceeded')
        self.balance -= amount


# 6. Create an Employee instance that has a CreditBankAccount as its
# bank_account. Try calling raise_salary and receive_salary on it. Does it
# behave differently than the first instance?
cba = CreditBankAccount("ING", 200, 300)
print('Initial balance:', cba.balance)
cba.deposit(100)  # call deposit() method
print('Balance after depositing 100:', cba.balance)  # should be 300
cba.withdraw(200)  # call withdraw() method
print('Balance after withdrawing 200:', cba.balance)  # should be 100
cba.withdraw(200)  # call withdraw() method
print('Balance after withdrawing another 200:', cba.balance)  # should be -100
try:
    cba.withdraw(250)  # should raise exception
except InsufficientFundsException as ex:
    print("Trying to withdraw 250:", ex)
print('Balance after trying to withdraw 250:', cba.balance)

emp1 = Employee("Jane Doe", cba, 1200)
print("Initial salary:", emp1.salary)
print("Initial balance:", emp1.bank_account.balance)
emp1.raise_salary(10)
print("Salary after 10% raise:", emp1.salary)
emp1.receive_salary()
print("Balance after receiving salary:", emp1.bank_account.balance)
