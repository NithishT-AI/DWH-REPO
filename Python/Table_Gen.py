# Multiplication Table Generator

#Input Table Number from user
Table = int(input("Enter Number for the Table: "))

for Loop in range(1,11):
    print(Table, "*", Loop, "=", Table * Loop)
