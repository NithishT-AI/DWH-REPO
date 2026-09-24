# Data Usage validations

# Ask the user for inputs
total_limit = float(input("Enter total monthly data limit (in GB): "))
data_used = float(input("Enter data used so far (in GB): "))

# Calculate remaining data and usage percentage
remaining_data = total_limit - data_used
usage_percentage = (data_used / total_limit) * 100

# Print the results
print("Remaining data:", remaining_data, "GB")
print("Usage percentage:", round(usage_percentage, 2), "%")
a
# Check for high usage warning
if usage_percentage >= 80:
    print("Warning: High usage, consider upgrading your plan.")
elif usage_percentage <= 25:
    print("Very low usage, you're well within your data limit.")
else:
    print("You're well within your data limit.")
