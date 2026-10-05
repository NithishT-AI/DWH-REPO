# Banking Eligibility Check with Conditional (IF - ELIF - ELSE)

# Ask the user for inputs
age = int(input("Enter age: "))
income = float(input("Enter monthly income: "))

# Check eligibility based on age and income
if age < 18:
    print("Not eligible for a bank account.")
elif age >= 18 and income < 15000:
    print("Eligible for basic savings account.")
elif age >= 18 and income <= 50000:
    print("Eligible for savings + salary account.")
elif age >= 18 and income > 50000:
    print("Eligible for premium account.")
