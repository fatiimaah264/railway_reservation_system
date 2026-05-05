# Railway Reservation System - Challenge 25
total_seats = 50
seats = {} # Dictionary for data storage
print("Railway System Initialized")

next_booking_id = 1001

def book_ticket():
    global next_booking_id
    name = input("Name: ")
    age = int(input("Age: "))
    for seat_no in range(1, 51):
        if seat_no not in [v['seat_no'] for v in seats.values()]:
            seats[next_booking_id] = {"name": name, "age": age, "seat_no": seat_no}
            print(f"Booked! ID: {next_booking_id}, Seat: {seat_no}")
            next_booking_id += 1
            return
    print("No seats available")

def cancel_ticket():
    try:
        booking_id = int(input("Booking ID: "))
        if booking_id in seats:
            del seats[booking_id]
            print("Ticket cancelled")
        else:
            print("Booking ID not found")
    except:
        print("Invalid input")
