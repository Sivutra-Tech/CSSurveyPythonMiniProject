import bookAMovie
import checkBooking
import cancelBooking

def runMenu():
    print("This is menu")
    print("Menu")
    print("1. Book a Movie")
    print("2. Check Booking")
    print("3. Cancel Booking")
    print("4. Exit")

    userChoice = int(input("What would you like to do?: "))

    if userChoice == 4:
        exit()
    elif userChoice == 1:
        bookAMovie.runBookAMovie()
    elif userChoice == 2:
        checkBooking.runCheckBooking()
    elif userChoice == 3:
        cancelBooking.runCancelBooking()


        

runMenu()