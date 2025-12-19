
#string
name = input("Enter your name: ")
print("Hello,", name)

#integer
age = int(input("Enter your age: "))
print("You are", age, "years old.")

#float
height = float(input("Enter your height in meters: "))
print("Your height is", height, "meters.")

# Take input as string for a list
fruits_input = input("Enter your favorite fruits,")
fruits_list = fruits_input.split(",")  # Convert string to list
print("Your favorite fruits are:", [fruit.strip() for fruit in fruits_list])
