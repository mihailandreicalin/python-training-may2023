# Andrei Calin

print("Lists 1")
# Given the following list:
#
# l = [4, 6, 1, 7, 8, 2, 8, 2, 4, 6, 8, 9]
# Add elements from [5, 7, 8] to the end of the list and print the new list
# Print the length of the list
# Check if 8 is in the list
# Print the first position of 7 in the list
# Count how many times 8 is in the list
# Reverse the list and print the new list
# Sort the list and print the new list
# Remove items on last two positions and print the new list
l = [4, 6, 1, 7, 8, 2, 8, 2, 4, 6, 8, 9]
l += [5, 7, 8]
print(f"New list = {l}")
print(f"List length = {len(l)}")
print(f"8 is in the list = {8 in l}")
print(f"first position of 7 in the list = {l.index(7) + 1}")
print(f"how many times 8 is in the list = {l.count(8)}")
l.reverse()
print(f"list reversed = {l}")
l.sort()
print(f"list sorted = {l}")
l.pop()
l.pop()
print(f"list sorted = {l}")

print("\nLists 2")
# Write a program to create a list of the squares of the first 10 odd numbers by iterating through a range object.
j = 0
l = []
for i in range(1, 100):
    if i % 2 == 1:
        l.append(i * i)
        j += 1
    if j == 10:
        break
print(l)

print("\nLists 3")
# Write a Python program to convert a list of characters into a string.
#
# words = ['a', 'b', 'c', 'd']
# # output: 'abcd'
words = ['a', 'b', 'c', 'd']
s = ''.join(words)
print(s)

print("\nLists 4")
# Create a list called my_list that contains the following items: 5, 4, 2, 3, 7, 1, 8, 9, 1, 2.
#
# Create a new list called new_list that contains only the even numbers from my_list.
# Print the entire new_list to the console.
# Create another new list called squared_list that contains the squares of all the numbers in my_list.
# Print the entire squared_list to the console.
# Create a third new list called modified_list that contains each item in my_list multiplied by 2,
# but only if the original number is greater than 2. Print the entire modified_list to the console.
my_list = [5, 4, 2, 3, 7, 1, 8, 9, 1, 2]
new_list = []
for x in my_list:
    if x % 2 == 0:
        new_list.append(x)
print(f"new_list = {new_list}")

squared_list = []
for x in my_list:
    squared_list.append(x * x)
print(f"squared_list = {squared_list}")

modified_list = []
for x in my_list:
    if x > 2:
        modified_list.append(x * 2)
print(f"modified_list = {modified_list}")

print("\nLists 5")
# Write a program to join together three existing lists. E.g.:
#
# list1 = [3, 2, 5]
# list2 = [4, 2]
# list3 = [6, 2, 6, 1]
# # output: [3, 2, 5, 4, 2, 6, 2, 6, 1]
list1 = [3, 2, 5]
list2 = [4, 2]
list3 = [6, 2, 6, 1]
list_join = list1 + list2 + list3
print(list_join)

print("\nLists 6")
# Write a Python program to find the second-smallest number in a list.
list_join.append(1)
list_join.sort()
smallest_number = list_join[0]
i = 1
second_smallest_number_found = False
while i < len(list_join):
    if smallest_number < list_join[i]:
        smallest_number = list_join[i]
        second_smallest_number_found = True
        break
    i += 1
if second_smallest_number_found:
    print(smallest_number)
else:
    print("second-smallest number not found")
