class AirlineTicket:
    """Ticket operations using methods only (no attributes stored in the class)."""

    def display_ticket(self, name, age, source, destination):
        print(f" Passenger : {name} of age : {age} is travelling from : {source} to : {destination}")

    def confirm_ticket(self):
        return "Confirmed"

    def cancel_ticket(self):
        return "Cancelled"

    def update_destination(self, old_destination, new_destination):
        print(f"Destination updated from {old_destination} to {new_destination}")
        return new_destination

    def get_ticket_details(self, name, age, source, destination, status):
        return {
            "Passenger": name,
            "Age": age,
            "From": source,
            "To": destination,
            "Status": status,
        }