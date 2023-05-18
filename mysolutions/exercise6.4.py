# Andrei Calin

print("Mapping types 1")
# Create a dictionary called my_dict that contains the following key-value pairs:
# "name": "John"
# "age": 30
# "occupation": "developer"
# "city": "New York"
# Print the entire my_dict to the console.
# Use the get() method to print the value associated with the key "occupation" to the console.
# Add a new key-value pair to my_dict that represents John's salary. Set the salary to 75000.
# Modify the value associated with the key "city" to be "San Francisco".
# Print the entire my_dict to the console again to see the changes.
# Use the pop() method to remove the key-value pair associated with the key "occupation" from my_dict.
# Create a new dictionary called new_dict that contains the following key-value pairs:
# "occupation": "teacher"
# "city": "Los Angeles"
# "is_active": False
# Use the update() method to add all the key-value pairs from new_dict to my_dict.
# Print the entire my_dict to the console again to see the changes.
# Use a for loop to iterate over the items in my_dict and print each key and its associated value to the console.
my_dict = {"name": "John", "age": 30, "occupation": "developer", "city": "New York"}
print(f"my_dict = {my_dict}")
print(f"occupation = {my_dict.get('occupation')}")
my_dict["salary"] = 75000
my_dict["city"] = "San Francisco"
print(f"my_dict = {my_dict}")

my_dict.pop("occupation")
new_dict = {"occupation": "teacher", "city": "Los Angeles", "is_active": False}
my_dict.update(new_dict)
print(f"my_dict = {my_dict}\n")

for key, value in my_dict.items():
    print(f"{key} = {value}")

print("\nMapping types 2")
# Given the following dictionary:
#
# d = {
#   'times': 100,
#   'name': 'George',
#   'hobbies': ['fishing', 'hiking'],
# }
# add key 'friends' to d with ['Andrei', 'Mihai', 'Alina'] as value
# sort value for key 'friends'
# remove 'hiking' from hobbies list
# remove 'times' key from d
d = {
  'times': 100,
  'name': 'George',
  'hobbies': ['fishing', 'hiking'],
}
d['friends'] = ['Andrei', 'Mihai', 'Alina']
d['friends'].sort()
d['hobbies'].remove("hiking")
d.pop("times")
print(f"d = {d}\n")

print("\nMapping types 3")
# Given a list of strings build a dictionary that has each unique string as a key and the number of appearances as a value.
#
# E.g. ['hello', 'hello', 'is', 'there', 'anybody', 'in', 'there'] -> {'hello': 2, 'is': 1, 'there': 2, 'anybody': 1, 'in': 1}

l = ['hello', 'hello', 'is', 'there', 'anybody', 'in', 'there']
d = {}
for key in l:
    if key not in d:
        d[key] = 1
    else:
        d[key] += 1
print(f"d = {d}")

print("\nMapping types 4")
# Create a dictionary of dictionaries to store the following data:
#
# id	Interface	IP	status
# 1	Ethernet0	1.1.1.1	up
# 2	Ethernet1	2.2.2.2	down
# 3	Serial0	3.3.3.3	up
# 4	Serial1	4.4.4.4	up
# {
#     1: {"interface": "Ethernet0", "ip": "1.1.1.1", "status": "up"},
#     # 2: {...}
# }
# Write a python program to find the status of a given id
# Write a python program to find interface and IP of all interfaces which are up
# Write a python program to count how many ethernet interfaces there are
# Write a python program to add a new entry to the dictionary (auto-increment the id)
d = {
    1: {"interface": "Ethernet0", "ip": "1.1.1.1", "status": "up"},
    2: {"interface": "Ethernet1", "ip": "2.2.2.2", "status": "down"},
    3: {"interface": "Serial0", "ip": "3.3.3.3", "status": "up"},
    4: {"interface": "Serial1", "ip": "4.4.4.4", "status": "up"},
}


def get_status(identifier):
    print(f'status = "{d[identifier]["status"]}" for id = {identifier}')


def get_up_interface_and_id():
    print("\nInterfaces which are up:")
    for item in d.values():
        if item["status"] == "up":
            print(f"interface = {item['interface']}, ip = {item['ip']}")


def count_ethernet_interfaces():
    count = 0
    for item in d.values():
        if item["interface"].lower().startswith("ethernet"):
            count += 1
    print(f"\nNo of ethernet interfaces = {count}")


def add_element(item):
    max_id = max(list(d))
    max_id += 1
    d[max_id] = item


get_status(1)
get_status(2)
get_up_interface_and_id()
count_ethernet_interfaces()
add_element({"interface": "Serial3", "ip": "5.5.5.5", "status": "down"})
last_id = max(list(d))
print(f"\nd[{last_id}] = {d[last_id]}")
