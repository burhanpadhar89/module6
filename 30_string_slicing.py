# String for slicing
title = "tops technologies"

# Demonstrating various slicing operations
print("Original String:", title)

# 1. Slice from index 0 to 4
print("title[0:5]:", title[0:5])

# 2. Slice from index 6 to the end
print("title[6:]:", title[6:])

# 3. Slice from start to index 4
print("title[:5]:", title[:5])

# 4. Slice the whole string
print("title[:]:", title[:])

# 5. Slice with step (every 2nd character)
print("title[::2]:", title[::2])

# 6. Reverse the string
print("title[::-1]:", title[::-1])

# 7. Negative indexing slice
print("title[-5:]:", title[-5:])
