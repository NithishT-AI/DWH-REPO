from Airtickets_Package import AirlineTicket

def read_age():
    while True:
        try:
            age = int(input("Enter age: "))
            if age <= 0 or age > 120:
                print("Age must be between 1 and 120.")
                continue
            return age
        except ValueError:
            print("Please enter a whole number for age.")


ticket = AirlineTicket()

# ---- Read the passenger details once and keep them in variables ----
print("===== Enter Passenger Details =====")
name = input("Enter passenger name: ").strip()
age = read_age()
source = input("Enter source: ").strip()
destination = input("Enter destination: ").strip()
status = "Not confirmed"

# ---- Menu: every option works with the variables above ----
while True:
    print("\n===== Airline Ticket Management =====")
    print("1. Get ticket details")
    print("2. Display ticket details")
    print("3. Confirm ticket")
    print("4. Cancel ticket")
    print("5. Update destination")
    print("6. Exit")

    choice = input("Choose an option (1-6): ").strip()

    if choice == "2":
        ticket.display_ticket(name, age, source, destination)

    elif choice == "3":
        status = ticket.confirm_ticket()
        print("Status:", status)

    elif choice == "4":
        status = ticket.cancel_ticket()
        print("Status:", status)

    elif choice == "5":
        print("Current destination:", destination)
        new_destination = input("Enter new destination: ").strip()
        destination = ticket.update_destination(destination, new_destination)

    elif choice == "1":
        details = ticket.get_ticket_details(name, age, source, destination, status)
        print("\n--- Ticket Details ---")
        for label, value in details.items():
            print(f"{label}: {value}")

    elif choice == "6":
        print("Thank you. Goodbye!")
        break

    else:
        print("Invalid option. Please enter a number from 1 to 6.")
