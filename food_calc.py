# Get the charge for the food
food_charge = float(input("Enter the charge for the food: $"))

# Calculate an 18% tip
tip = food_charge * 0.18

# Calculate a 7% sales tax
sales_tax = food_charge * 0.07

# Calculate the total price
total_price = food_charge + tip + sales_tax

# Print the amounts
print(f"\nFood Charge: ${food_charge:.2f}")
print(f"Tip: ${tip:.2f}")
print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Total Price: ${total_price:.2f}")