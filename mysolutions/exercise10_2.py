# Andrei Calin

print("Dunder 1")
# Create class Dish - instance attributes: id (int), name (str), price (int)


class Dish:
    def __init__(self, id: int, name: str, price: int):
        self.id = id
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Dish (id = {self.id}, name={self.name}, price={self.price})"

print("\nDunder 2")
# Create class Menu - instance attributes: dishes (list of Dish objects).
# Implement appropriate methods so that Menu objects support the following operations:
# d = Dish(0, 'Lasagna', 20)
# m = Menu()
# m += d  # dish appended to m.dishes
# m[0]  # implement getitem on Menu
# d in m  # implement membership test operators
# len(m)  # return length of m.dishes


class Menu:
    def __init__(self, dishes = None):
        self.dishes = dishes or []

    def __iadd__(self, dish: Dish):
        self.dishes.append(dish)
        return self

    def __getitem__(self, item):
        return self.dishes[item]

    def __contains__(self, item):
        return item in self.dishes

    def __len__(self):
        return len(self.dishes)


if __name__ == "__main__":
    d = Dish(0, 'Lasagna', 20)
    m = Menu()
    print(m.dishes)
    m += d  # dish appended to m.dishes
    print(m[0])  # implement getitem on Menu
    print(d in m)  # implement membership test operators
    print(len(m))  # return length of m.dishes
