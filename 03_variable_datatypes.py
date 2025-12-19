"""
Program: Demonstrate the creation of variables and different data types in Python.
Author: ChatGPT (Example)
Description:
    This program shows how to create variables of various data types such as:
    integers, floats, strings, lists, tuples, dictionaries, and sets.
"""

# Integer variable (whole number)
age = 25

# Float variable (decimal number)
height = 5.9

# String variable (text)
name = "Alice"

# Boolean variable (True or False)
is_student = True

# List (ordered, mutable collection)
fruits = ["apple", "banana", "cherry"]

# Tuple (ordered, immutable collection)
coordinates = (10.5, 20.3)

# Dictionary (key-value pairs)
person = {
    "name": name,
    "age": age,
    "height": height
}

# Set (unordered collection of unique items)
unique_numbers = {1, 2, 3, 3, 4}

# Display all variables and their data types
print("=== Python Variables and Data Types ===\n")

print("Name:", name, "→", type(name))
print("Age:", age, "→", type(age))
print("Height:", height, "→", type(height))
print("Is Student:", is_student, "→", type(is_student))
print("Fruits:", fruits, "→", type(fruits))
print("Coordinates:", coordinates, "→", type(coordinates))
print("Person Info:", person, "→", type(person))
print("Unique Numbers:", unique_numbers, "→", type(unique_numbers))
