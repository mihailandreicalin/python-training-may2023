# Andrei Calin

# print("Classes and Instances 1")
# Create a BankAccount class that receives two parameters on initialisation:
# bank name (str)
# balance (int)
# Create two methods in this class, one to withdraw money and another one to deposit money into the account.
# The withdraw method will not allow withdrawing more money than available:
# it will raise an exception and not change the balance.
# Create a BankAccount instance and test the two methods with different inputs.


class BankAccount:
    """Docstring for BankAccount class"""

    def __init__(self, bank_name: str, balance: int):
        self.bank_name = bank_name
        self.balance = balance
        print(f"Initial balance = {self.balance} for bank = {self.bank_name}")

    def withdraw(self, money: int):
        if money > self.balance:
            error_message = f"Insufficient funds ({self.balance}) to withdraw {money}"
            raise ValueError(error_message)
        self.balance -= money
        print(f"funds = {self.balance} after withdraw {money}")

    def deposit(self, money):
        self.balance += money
        print(f"funds = {self.balance} after deposit {money}")


# print("\nClasses and Instances 2")
# Create a class called Rectangle with attributes width and height.
# Add methods get_area and get_perimeter that calculate and return the area and perimeter of the rectangle.


class Rectangle:
    """Docstring for BankAccount class"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.width + self.height) * 2


if __name__ == "__main__":
    r1 = Rectangle(2, 3)
    print(f"Rectangle with width = {r1.width} and height = {r1.height} has area = {r1.get_area()} and perimeter = {r1.get_perimeter()}")
    r1 = Rectangle(5, 9)
    print(f"Rectangle with width = {r1.width} and height = {r1.height} has area = {r1.get_area()} and perimeter = {r1.get_perimeter()}")

    bank1 = BankAccount('BCR', 100)
    bank1.withdraw(50)
    bank1.deposit(10)
    try:
        bank1.withdraw(70)
    except ValueError as ex:
        print(ex)

