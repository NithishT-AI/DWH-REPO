# Employee Salary Breakdown

# a. Ask the user for inputs
employee_name = input("Enter employee name: ")
base_salary = input("Enter base salary: ")
hra_percent = input("Enter HRA percent: ")
bonus_amount = input("Enter bonus amount: ")

# b. Convert inputs to the correct datatype
base_salary = float(base_salary)
hra_percent = int(hra_percent)
bonus_amount = float(bonus_amount)

# Calculate HRA and Total Salary
hra = base_salary * (hra_percent / 100)
total_salary = base_salary + hra + bonus_amount

# c. Print the output
print("Employee:", employee_name)
print("Base Salary:", base_salary)
print(f"HRA @ {hra_percent}%:", hra)
print("Bonus:", bonus_amount)
print("Total Salary Payable: ₹" + str(total_salary))
