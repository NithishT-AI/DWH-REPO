# Temperature Checker (Multi-range classification)

temperature = float(input("Enter the current temperature (°C): "))

if temperature > 45:
    print("Very Hot")
elif temperature >= 30:
    print("Hot")
elif temperature >= 15:
    print("Normal")
elif temperature >= 5:
    print("Cool/Cold")
else:
    print("Very Cool/Cold")
