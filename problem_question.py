class BookingNode:
    def __init__(self, name, tickets):
        self.name = name
        self.tickets = tickets
        self.next = None


class BookingSystem:
    def __init__(self):
        self.head = None

    def add_booking(self, name, tickets):
        new_node = BookingNode(name, tickets)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        print(f"Booking added: {name} - {tickets} tickets")

    def cancel_booking(self, name):
        if not self.head:
            print("No bookings found.")
            return
        
        if self.head.name == name:
            self.head = self.head.next
            print(f"Booking for {name} has been cancelled.\n")
            return

        temp = self.head
        while temp.next and temp.next.name != name:
            temp = temp.next

        if temp.next:
            temp.next = temp.next.next
            print(f"Booking for {name} has been cancelled.\n")
        else:
            print(f"No booking found for {name}.\n")

    def view_bookings(self):
        if not self.head:
            print("No bookings available.")
            return
        temp = self.head
        print("Current bookings:\n")
        while temp:
            print(f"Name: {temp.name}, Tickets: {temp.tickets}")
            temp = temp.next
        print()  
theater = BookingSystem()
theater.add_booking("Brhama", 3)
theater.add_booking("Vishnu", 2)
theater.add_booking("Maheswara", 5)
print()  
theater.view_bookings()
print("Cancelling booking...\n")
theater.cancel_booking("Brhama")
print("Bookings after cancellation:\n")
theater.view_bookings()