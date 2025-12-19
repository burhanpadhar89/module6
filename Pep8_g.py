"""
A simple program to calculate the total cost of items in a shopping cart.

Demonstrates correct:
- Indentation (4 spaces)
- Use of comments
- Variable naming following PEP 8
"""

def calculate_total_cost(item_prices, tax_rate):
    """
    Calculate the total cost including tax.

    Args:
        item_prices (list): A list of item prices (floats).
        tax_rate (float): The tax rate as a decimal (e.g., 0.07 for 7%).

    Returns:
        float: The total cost including tax.
    """
    subtotal = sum(item_prices)         # Add up the item prices
    tax_amount = subtotal * tax_rate    # Calculate tax
    total_cost = subtotal + tax_amount  # Add tax to subtotal

    return total_cost


def main():
    """Main function to demonstrate the calculation."""
    # List of item prices in dollars
    item_prices = [19.99, 5.49, 3.50, 12.75]

    # Tax rate (7%)
    tax_rate = 0.07

    # Calculate total cost
    total_cost = calculate_total_cost(item_prices, tax_rate)

    # Display the result
    print("Shopping Cart Summary")
    print("----------------------")
    print(f"Items: {len(item_prices)}")
    print(f"Total Cost (with tax): ${total_cost:.2f}")


# Call the main function
if __name__ == "__main__":
    main()
