# Andrei Calin

print("Set 1")
# Exercises
# Given the following set:
#
# s = set()
# Add elements from [1, 2, 3] to the set and print the new set
# Print the length of the set
# Check if 4 is in the set
# Remove and print an arbitrary element from the set; print the new set
# Remove all remaining items in the set and print the new set
s = set()
s.update([1, 2, 3])
print(f"s = {s}")
print(f"s length = {len(s)}")
print(f"4 is in the set = {4 in s}")
print(f"s element = {s.pop()}")
print(f"s = {s}")
s.clear()
print(f"s = {s}")

print("\nSet 2")
# Create a set called fruit_set that contains the names of five different fruits.
# Add a new fruit to the fruit_set. Remove one of the fruits from the fruit_set. Print the new fruit_set to the console.
fruit_set = {"apple", "banana", "lucuma", "pear", "coconut"}
fruit_set.add("mango")
fruit_set.remove("pear")
print(f"fruit_set = {fruit_set}")

print("\nSet 3")
# Create a set called visited_cities that contains the names of five cities you have visited in the past.
# Create a second set called bucket_list that contains the names of three cities you want absolutely want to visit.
# Create the set bucket_list_completed which contains cities that are in both visited_cities and bucket_list (intersection).
# Create the set all_cities which contains cities that are in either visited_cities or bucket_list (union).
# Create the set must_visit which contains cities that are in bucket_list, but not in visited_cities (difference).
visited_cities = {"Bucharest", "Berlin", "London", "Paris", "Lisbon"}
bucket_list = {"Stockholm", "Berlin", "Cape Town"}
bucket_list_completed = bucket_list & visited_cities
print(f"bucket_list_completed = {bucket_list_completed}")

all_cities = bucket_list | visited_cities
print(f"all_cities = {all_cities}")

must_visit = bucket_list - visited_cities
print(f"must_visit = {must_visit}")

print("\nSet 4")
# Write a Python program that counts the number of distinct words from a string.
# A word=a sequence of characters that is not whitespace (space, newline, tab).
#
# E.g.
#
# my_str = """beautiful is better than ugly
# explicit is better than implicit
# simple is better than complex
# complex is better than complicated
# flat is better than nested
# sparse is better than dense"""
# # Should print: 14 distinct words
my_str = """beautiful is better than ugly
explicit is better than implicit
simple is better than complex
complex is better than complicated
flat is better than nested
sparse is better than dense"""
s = set(my_str.split())
print(s)
print(len(s))
