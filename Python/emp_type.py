# Ask for employee's age
age = input("Enter employee's age: ")

# 1. Check that the type is string
print(type(age))

# 2. Convert it to int
age = int(age)
print(type(age))

# 3. Print the years pending for retirement (retirement age = 60)
retirement_age = 60
years_pending = retirement_age - age

if years_pending > 0:
    print("Years pending for retirement:", years_pending)
elif years_pending == 0:
    print("Employee is retiring this year!")
else:
    print("Employee has already crossed the retirement age by", -years_pending, "years")
