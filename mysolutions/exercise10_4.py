# Andrei Calin

from examples.exercise10_1 import BankAccount
from examples.exercise10_3 import Employee

print("Inheritance 1")
# Create a CreditBankAccount class that inherits BankAccount and receives one extra argument at initialisation
# which allows for the balance to go below zero (but not under -overdraft):


class CreditBankAccount(BankAccount):

    def __init__(self, bank_name: str, balance: int, overdraft: int):
        super().__init__(bank_name, balance)
        self.overdraft = overdraft

    def withdraw(self, amount: int):
        remaining_amount = self.balance - amount
        if remaining_amount < -self.overdraft:
            error_message = f"Remaining amount ({remaining_amount}) < overdraft value ({-self.overdraft})"
            raise ValueError(error_message)
        self.balance -= amount
        print(f"funds = {self.balance} after withdraw {amount}")


# overdraft (int)
# Override parent withdraw method so that the new rule is implemented.

print("Inheritance 2")
# Create an Employee instance that has a CreditBankAccount as its bank_account.
# Try calling raise_salary and receive_salary on it. Does it behave differently than the first instance?

print("Inheritance 3")
# Place the two bank account classes in a Python module and the employee class in another Python module.
# Create a third module that uses the first two modules.

if __name__ == "__main__":
    bank1 = CreditBankAccount('BCR', 100, 20)
    bank1.withdraw(50)
    bank1.deposit(10)
    bank1.withdraw(70)
    try:
        bank1.withdraw(20)
    except ValueError as ex:
        print(ex)

    employee = Employee('Ion', bank1, 1000)
    employee.raise_salary(10)
    employee.receive_salary()
