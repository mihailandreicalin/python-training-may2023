from datetime import date
import random


class Person:
    count = 0  # class attribute
    MAX_YEAR = 1950

    def __init__(self, name, date_of_birth):
        self.name = name  # instance attribute
        self.date_of_birth = date_of_birth
        self._increment_count()

    @property
    def date_of_birth(self):  # getter
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, value: date):  # setter
        if not hasattr(value, "year") or value.year < self.MAX_YEAR:
            raise ValueError("Date of birth year should be greater than or "
                             f"equal to {self.MAX_YEAR}")
        self._date_of_birth = value

    @property
    def age(self):
        return self.compute_age(self.date_of_birth)

    def greet(self, greeting):  # instance method
        print(f"{self.name} says '{greeting}!'")

    @classmethod
    def _increment_count(cls):  # class method
        cls.count += 1

    @staticmethod
    def compute_age(date_of_birth):  # static method
        delta = date.today() - date_of_birth
        return int(delta.days / 365.25)

    def __repr__(self):
        return f"<{self.__class__.__name__} object (name={self.name})>"

    def __str__(self):
        return f"{self.__class__.__name__} (name={self.name}, age={self.age})"

    def __lt__(self, other):
        return self.age < other.age


class Student(Person):
    count = 0

    def __init__(self, name, date_of_birth, university):
        super().__init__(name, date_of_birth)
        self.university = university

    def __str__(self):
        return f"{self.__class__.__name__} (name={self.name}, age={self.age}, "\
               f"university={self.university})"

    def get_grade(self, subject):
        return random.randint(3, 10)


if __name__ == "__main__":
    p1 = Person('Anna', date(1984, 3, 21))
    p1.date_of_birth = date(1959, 1, 1)
    print(p1.name, p1.age, p1.date_of_birth)
    p1.greet("Hi")

    p2 = Person('Mark', date(2001, 12, 1))
    print(p2.name, p2.age)
    p2.greet("Good morning")

    print(Person.count, p1.count, p2.count)
    print(p1)  # print(p1.__str__())
    print(repr(p1))

    print(f"{p1.name} is younger than {p2.name}: {p1 < p2}")

    # Person._increment_count()
    # print(Person.count)

    print("Static method compute_age:", Person.compute_age(date(1999, 10, 2)))

    s1 = Student("Jane Smith", date(2001, 4, 13), "Universitatea București")
    print(s1)
    s1.greet("Good day")
    print(s1.get_grade("Math"))
    print("Students:", Student.count, "Persons:", Person.count)
