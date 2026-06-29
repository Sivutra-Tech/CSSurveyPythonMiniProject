import ticket

def runCheckBooking():
    print("Checking your Booked Movie!")
    userTicketID= input("Please Enter the Ticket ID you recieved on the Reciept: ")

    result = ticket.searchTicket(userTicketID)
    if result:
        print(f"with ticket ID: {userTicketID}")
        print(f"You book {result[0][1]} at {result[0][2]} on {result[0][3]} with seat row {result[0][4]} and seat number {result[0][5]}")
    else:
        print("Ticket Not Found")