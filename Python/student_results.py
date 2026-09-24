# Marks Classification Program

# a. Take marks as input (initially as a string)
marks = input("Enter marks: ")

# b. Check if the value can be converted to float
try:
    marks = float(marks)
    print("Conversion successful! Marks:", marks)

    results = "Outstanding" if marks >= 90 else "Excellent" if marks >= 75 else "Pass" if marks >= 50 else "Fail"
    print("Classification based on marks:", results)
    """
    # c. Classify based on marks
    if marks >= 90:
        print("Outstanding")
    elif marks >= 75:
        print("Excellent")
    elif marks >= 50:
        print("Pass")
    else:
        print("Fail")
    """
except ValueError:
    print("Invalid input! Please enter a numeric value for marks.")
