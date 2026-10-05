#Input Number from user
Input = int(input("Enter a Number : "))

# Initialize sum accumulators
sum_even = 0
sum_odd = 0

# Loop through numbers from 1 to n (inclusive)
for num in range(1, Input + 1):
    # Check if the number is even
    if num % 2 == 0:
        sum_even += num
    # If the number is not even, it must be odd
    else:
        sum_odd += num

# Print the final calculated sums
print(f"Sum of all even numbers from 1 to {Input}: {sum_even}")
print(f"Sum of all odd numbers from 1 to {Input}: {sum_odd}")
