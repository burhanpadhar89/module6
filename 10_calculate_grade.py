

# Take input from the user
percentage = float(input("Enter your percentage: "))

# Determine grade using if-elif-else ladder
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

# Display the result
print(f"Your grade is: {grade}")

