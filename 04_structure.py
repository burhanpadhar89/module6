"""
Program: Example of Python Code Structure
Author: ChatGPT (Example)
Description:
    This program demonstrates how a typical Python script is structured,
    including functions, variables, and the main execution block.
"""

# 1️⃣ Import statements
import math

# 2️⃣ Global variables / constants
PI = math.pi

# 3️⃣ Function definitions
def calculate_area_of_circle(radius):
    """Return the area of a circle given its radius."""
    area = PI * (radius ** 2)
    return area


def display_result(radius, area):
    """Print the formatted area of a circle."""
    print(f"The area of a circle with radius {radius} is {area:.2f}")


# 4️⃣ Main function (main program logic)
def main():
    """Main function to execute the program."""
    # Input
    radius = float(input("Enter the radius of the circle: "))

    # Process
    area = calculate_area_of_circle(radius)

    # Output
    display_result(radius, area)


# 5️⃣ Execution starts here
if __name__ == "__main__":
    main()


