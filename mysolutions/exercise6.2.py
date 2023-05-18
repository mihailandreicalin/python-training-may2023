# Andrei Calin

print("Tuple 1")
# Create a tuple called my_tuple that contains the following items: "apple", 2, True, "banana", 3.14
#
# Print the entire tuple to the console.
# Print the third item in the tuple (True) to the console.
# Print the length of the tuple to the console.
# Try to change the second item in the tuple to "pear". What happens?
# Create a new tuple called my_slice that contains only the first three items from my_tuple.
# Print the entire my_slice tuple to the console.
# Use a for loop to print each item in my_tuple on a new line.
# Try to add a new item to my_tuple. What happens?
my_tuple = ("apple", 2, True, "banana", 3.14)
print(f"my_tuple = {my_tuple}")
print(f"third item in the tuple = {my_tuple[2]}")
print(f"length of the tuple = {len(my_tuple)}")
try:
    my_tuple[1] = 'pear'
except TypeError as ex:
    print(f"Exception: {ex}")

my_slice = my_tuple[0:3]
print(f"my_slice = {my_slice}")

for item in my_tuple:
    print(item)

try:
    my_tuple += 'pear'
except TypeError as ex:
    print(f"Exception: {ex}")

print("\nTuple 2")
# Create two tuples called tuple1 and tuple2 that each contain three items of your choice.
# Combine the two tuples into a new tuple called combined_tuple. Print the entire combined_tuple to the console.
tuple1 = (1, 'a', 23)
tuple2 = (2, 'b', 24)
combined_tuple = tuple1 + tuple2
print(f"combined_tuple = {combined_tuple}")

print("\nTuple 3")
# Given two lists, create a list of tuples where element on position n is a tuple of elements on position n from each list.
# If one list is longer than the other, ignore extra elements.
#
# E.g. ["Anna", "John", "Marie"], [12, 15, 22, 13] -> [("Anna", 12), ("John", 15), ("Marie", 22)]
list1 = ["Anna", "John", "Marie", "Ion", "Ana"]
list2 = [12, 15, 22, 13]
my_list = []

length = min(len(list1), len(list2))
i = 0
while i < length:
    my_list.append((list1[i], list2[i]))
    i += 1
print(f"my_tuple = {my_list}")
