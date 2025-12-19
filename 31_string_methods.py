# String for manipulation
title = "tops technologies"

print("Original String:", repr(title))

# 1. Convert to uppercase
print("After upper():", title.upper())

# 2. Convert to lowercase
print("After lower():", title.lower())

# 3. Capitalize first character only
print("After capitalize():", title.capitalize())

# 4. Title case (each word starts with uppercase)
print("After title():", title.title())

# 5. Replace a substring
print("After replace():", title.replace("technologies", "TECH"))

# 6. Count occurrences of 'o'
print("Count of 'o':", title.count("o"))

# 7. Find position of substring
print("Position of 'tech':", title.find("tech"))

# 8. Check start and end
print("Starts with 'tops'? ->", title.startswith("tops"))
print("Ends with 'gies'? ->", title.endswith("gies"))

# 9. Splitting into list
words = title.split()
print("After split():", words)

# 10. Joining back with '-'
joined = "-".join(words)
print("After join():", joined)
