class Person:
    count = 0  # class attribute

    def __init__(self, name, age=0):
        self.name = name  # instance attribute
        self.age = age
        Person.count += 1

    def greet(self, greeting):  # instance method
        print(f"{self.name} says '{greeting}!'")

    def __repr__(self):
        return f"<{self.__class__.__name__} object (name={self.name})>"

    def __str__(self):
        return f"{self.__class__.__name__} (name={self.name}, age={self.age})"

    def __lt__(self, other):
        return self.age < other.age


if __name__ == "__main__":
    p1 = Person('Anna', 20)
    print(p1.name, p1.age)
    p1.greet("Hi")

    p2 = Person('Mark')
    print(p2.name, p2.age)
    p2.greet("Good morning")

    print(Person.count, p1.count, p2.count)
    print(p1)  # print(p1.__str__())
    print(repr(p1))

    print(f"{p1.name} is younger than {p2.name}: {p1 < p2}")
