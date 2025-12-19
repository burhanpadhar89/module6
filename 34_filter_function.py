# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using filter() with a lambda function to get even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Print the result
print("Original list:", numbers)
print("Even numbers:", even_numbers)
