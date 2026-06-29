import bookAMovie
import checkBooking


def runMenu():
    print("This is menu")
    print("Menu")
    print("1. Book a Movie")
    print("2. Check Booking")
    print("3. Exit")

    userChoice = int(input("What would you like to do?: "))

    if userChoice == 3:
        exit()
    elif userChoice == 1:
        bookAMovie.runBookAMovie()
        import ticketpayment
    elif userChoice == 2:
        checkBooking.runCheckBooking()
    


        

