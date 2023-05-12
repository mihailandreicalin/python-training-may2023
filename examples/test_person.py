from datetime import date
import unittest

from oop import Person


class TestDateOfBirth(unittest.TestCase):
    def setUp(self):
        self.valid_date = date(1999, 4, 5)
        self.invalid_date = date(1949, 4, 5)

    def test_initialize_person_with_valid_date(self):
        person = Person('Anna', self.valid_date)
        self.assertEqual(self.valid_date, person.date_of_birth)

    def test_initialize_person_with_invalid_date(self):
        with self.assertRaises(ValueError):
            Person('Anna', self.invalid_date)

    def test_set_date_of_birth_to_valid_date(self):
        person = Person('Anna', date(2000, 1, 1))
        person.date_of_birth = self.valid_date
        self.assertEqual(self.valid_date, person.date_of_birth)

    def test_set_date_of_birth_to_invalid_date(self):
        person = Person('Anna', self.valid_date)
        with self.assertRaises(ValueError):
            person.date_of_birth = self.invalid_date
        self.assertEqual(self.valid_date, person.date_of_birth)
