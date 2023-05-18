# Andrei Calin
import datetime
from examples.exercise10_1 import BankAccount

# print("Static and class methods 1")
# Create a class Employee with three instance attributes:
#
# name
# bank_account (it should be a BankAccount object; pass an already created BankAccount instance at Employee initialisation)
# salary (default 0)
# Write a method raise_salary that receives a parameter percent that should be one of the following values: 5, 10, 20. Raise a ValueError if another value is received by this method. The raise_salary method should raise the salary with 5%, 10% or 20%.
# Create a method receive_salary that will deposit in the employee's bank account an amount equal to its salary.
# Use a property for salary management. Salary should be set only on initialisation; you shouldn't be able to set the salary from outside the class.
# Create an Employee instance and call raise_salary and receive_salary on it.


class Employee:
    def __init__(self, name: int, bank_account: BankAccount, salary=0):
        self.name = name
        self.bank_account = bank_account
        self.__salary = salary

    def __repr__(self):
        return f"Employee (name = {self.name}, account={self.bank_account.balance}, salary={self.__salary})"

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        raise ValueError("You cannot set the salary")

    @salary.deleter
    def salary(self):
        raise ValueError("You cannot delete the salary")

    def raise_salary(self, percent):
        if percent not in (5, 10, 20):
            raise ValueError("Percent should have one of the values: 5, 10, 20")
        self.__salary = self.__salary + self.__salary * percent / 100

    def receive_salary(self):
        self.bank_account.deposit(self.__salary)


# print("\nStatic and class methods 1")
# Create a class called Book with title, author, and year as attributes.
# Add a method is_recent that returns True if the book was published in the last 10 years and False otherwise.
# Create an instance and call the method on it. Then, add @property decorator to the method definition. How does the call change?


class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f"Book (title = {self.title}, author={self.author}, year={self.year})"

    @property
    def is_recent(self):
        return self.year + 10 > datetime.date.today().year


if __name__ == "__main__":
    bank1 = BankAccount('BCR', 1000)
    employee = Employee('Ion', bank1, 1000)
    print(employee)
    try:
        employee.raise_salary(23)
    except ValueError as ex:
        print(ex)
    try:
        employee.salary = 99999
    except ValueError as ex:
        print(ex)
    try:
        del employee.salary
    except ValueError as ex:
        print(ex)
    employee.raise_salary(10)
    employee.receive_salary()
    print(employee)

    book = Book('Ceva', 'Popescu', 2020)
    print(f"Book {book} is recent {book.is_recent}")
    book = Book('Altceva', 'Popescu', 2013)
    print(f"Book {book} is recent {book.is_recent}")

