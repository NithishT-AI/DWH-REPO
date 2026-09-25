# Find the Greatest (or Equal) of Three Numbers - using nested logic

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Check if all three are equal
if num1 == num2 and num2 == num3:
    print(f"All three numbers are equal: {num1} = {num2} = {num3}")

# Check if num1 is the greatest (or equal to another, but still the max)
elif num1 >= num2 and num1 >= num3:
    if num2 == num3:
        print(f"{num1} is the greatest (other two, {num2} and {num3}, are equal)")
    else:
        print(f"{num1} is the greatest number")

# Check if num2 is the greatest
elif num2 >= num1 and num2 >= num3:
    if num1 == num3:
        print(f"{num2} is the greatest (other two, {num1} and {num3}, are equal)")
    else:
        print(f"{num2} is the greatest number")

# Otherwise num3 must be the greatest
else:
    if num1 == num2:
        print(f"{num3} is the greatest (other two, {num1} and {num2}, are equal)")
    else:
        print(f"{num3} is the greatest number")
