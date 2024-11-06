# A function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount

# Define the function
def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        # Calculate the final price after applying the discount
        final_price = price - discount_amount
        return final_price
    else:
        # If the discount is less than 20%, return the original price
        return price

# Prompt the user for input
price = float(input("Enter the original price of the item: "))
discount_percent = int(input("Enter the discount percentage: "))

# Calculate and display the final price
final_price = calculate_discount(price, discount_percent)
print("The final price after applying the discount is:", final_price)
