from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Using reduce() with a lambda function to multiply all numbers
product = reduce(lambda x, y: x * y, numbers)

# Print the result
print("List of numbers:", numbers)
print("Product of all numbers:", product)
