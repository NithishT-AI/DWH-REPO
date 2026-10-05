# Temperature Checker (Multi-range classification)

temp = float(input("Enter body temperature in Celsius: "))
###temp = float(temp)  # Convert string input to a number bef7ore comparing

if temp < 37:
    print("Normal temperature")
elif temp > 37 and temp < 39:
    print("Fever")
else:
    print("High fever")
