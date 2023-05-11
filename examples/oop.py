class Person:
    count = 0  # class attribute

    def __init__(self, name, age=0):
        self.name = name  # instance attribute
        self.age = age
        Person.count += 1

    def greet(self, greeting):  # instance method
        print(f"{self.name} says '{greeting}!'")


if __name__ == "__main__":
    p1 = Person('Anna', 20)
    print(p1.name, p1.age)
    p1.greet("Hi")

    p2 = Person('Mark')
    print(p2.name, p2.age)
    p2.greet("Good morning")

    print(Person.count, p1.count, p2.count)
