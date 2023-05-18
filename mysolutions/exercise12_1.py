# Andrei Calin
from examples.exercise10_1 import BankAccount
from examples.exercise10_3 import Employee
import unittest


class TestEmployeeRaiseSalary(unittest.TestCase):
    def setUp(self):
        self.initial_amount = 1000
        bank_account = BankAccount('BCR', 100)
        self.employee = Employee('Ion', bank_account, self.initial_amount)

    def test_raise_salary_valid_percent(self):
        self.employee.raise_salary(5)
        self.assertEqual(self.initial_amount * 105 / 100, self.employee.salary)

    def test_raise_salary_invalid_percent(self):
        with self.assertRaises(ValueError) as cm:
            self.employee.raise_salary(7)
        the_exception: ValueError = cm.exception
        self.assertEqual("Percent should have one of the values: 5, 10, 20", str(the_exception))
        self.assertEqual(self.initial_amount, self.employee.salary)
