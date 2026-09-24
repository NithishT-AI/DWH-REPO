# Discount Calculator

# Ask the user for inputs
price = float(input("Enter original price: "))
discount_percent = int(input("Enter discount percent: "))

# Calculate discount amount and final price
discount_amount = (price * discount_percent) / 100
final_price = price - discount_amount

# Print the results
print("Original price:", price)
print("Discount applied:", discount_amount)
print("Final payable amount:", final_price)
