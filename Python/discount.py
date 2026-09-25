# Discount Calculator (Min cart 600, 10% discount, max cap ₹100)

# Variables (fixed rules)
min_cart_amt = 600
disc_pct_whole = 10
max_disc_amt = 100

# Input (runtime)
cart_value = float(input("Enter your cart value: ₹ "))

# First check: minimum cart value
if cart_value >= min_cart_amt:

    # Calculate discount percentage as a fraction
    disc_pct = disc_pct_whole / 100

    # Calculate discount amount
    disc_amt = cart_value * disc_pct

    # Compare with max discount cap
    if disc_amt >= max_disc_amt:
        final_amt = cart_value - max_disc_amt
        print(f"Discount capped at ₹{max_disc_amt}")
    else:
        final_amt = cart_value - disc_amt
        print(f"Discount applied: ₹{disc_amt}")

    print(f"Final payable amount: ₹{final_amt}")

else:
    shortfall = min_cart_amt - cart_value
    print(f"Add ₹{shortfall} more to your cart to avail the offer.")
