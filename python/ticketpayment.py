import ticket
import bookAMovie

someList = bookAMovie.getComfirmationList()
print(f"You have book {someList[1]} at {someList[2]} on {someList[3]} with seat row {someList[4]} and seat number {someList[5]} ")
print(f"Here is your Ticket ID: {someList[0]}")


theater = "KonKhmerMovie"
total = 5

print(" PAYMENT ")
print("1. Visa / Mastercard")
print("2. Cash")
print("3. Bakong QR Code")
print("4. ABA Pay")
print("5. Wing Money")

choice = input("\nChoose payment method: ")

if choice == "1":
    card = input("Enter 16-digit card number: ")
    exp  = input("Expiration date (MM/YY): ")
    cvv  = input("CVV: ")
    print("\nPayment Successful!")
    ticket.addTicketToStorage(bookAMovie.getComfirmationList())

elif choice == "2":
    print("\nPayment Successful!")
    print("Please pay $" + str(total) + " at the cashier.")
    ticket.addTicketToStorage(bookAMovie.getComfirmationList())

elif choice == "3":
    print("\n+------------------+")
    print("       ┌──────────────────────┐")
    print("       │  ▄▄▄  █▄█  ▄  ▄▄▄  │")
    print("       │  █ █  █ █  █  █ █  │")
    print("       │  ▀▀▀  ▀▀▀  ▀  ▀▀▀  │")
    print("       │    [CINEMA]      │")
    print("       │  ▄▄▄  █ █  ▄  ▄▄▄  │")
    print("       │  █ █  █▄█  █  █ █  │")
    print("       │  ▀▀▀  ▀▀▀  ▀  ▀▀▀  │")
    print("       └──────────────────────┘")
    print("+------------------+")
    confirm = input("\nAre you sure you want to pay $" + str(total) + " to " + theater + "? (Y/N): ")
    if confirm.upper() == "Y":
        print("Payment Successful!")
        ticket.addTicketToStorage(bookAMovie.getComfirmationList())
    else:
        print("Payment cancelled.")

elif choice == "4":
    confirm = input("Are you sure you want to pay $" + str(total) + " to " + theater + "? (Y/N): ")
    if confirm.upper() == "Y":
        print("Payment Successful!")
        ticket.addTicketToStorage(bookAMovie.getComfirmationList())
    else:
        print("Payment cancelled.")

elif choice == "5":
    confirm = input("Are you sure you want to pay $" + str(total) + " to " + theater + "? (Y/N): ")
    if confirm.upper() == "Y":
        print("Payment Successful!")
        
        ticket.addTicketToStorage(bookAMovie.getComfirmationList())
    else:
        print("Payment cancelled.")

else:
    print("Invalid choice.")
