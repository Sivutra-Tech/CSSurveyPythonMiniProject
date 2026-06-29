from operator import truediv

import movieData
import seatData

def runBookAMovie():
    #List of 5 available movie genre
    print ("Here is the list of genre")
    genre= ["horror", "action", "fantasy", "romance", "scifi"]
    num= 0
    for number in genre:
        num+= 1
        print(f"{num}. {number}")
    #User choose their favorite genre
    Genre= input("Choose your genre: ")
    SomeList= []
    #User choose horror film
    if Genre == "1" :
        print ("Available Movies")
        print ("MovieID , MovieGenre , MovieName , MovieDuration , MovieTime1 , MovieTime2 , MovieDate1 , MovieDate2")
        movie = movieData.getMovie("Horror")
        HorrorMovieChoice= input("Choose your movie (1-4): ")
    if HorrorMovieChoice == "1":
        SomeList.append(movie[0][2])
        print (f"Movie Name: {movie[0][2]}")
        print (f"First Time Slot: {movie[0][4]} on {movie[0][6]}")
        print (f"Second Time Slot: {movie[0][5]} on {movie[0][7]}")
        Showtime = input("Choose your show time (1-2): ")
        if Showtime == "1":
            SomeList.append(movie[0][4])
            SomeList.append(movie[0][6])
        if Showtime == "2":
            SomeList.append(movie[0][5])
            SomeList.append(movie[0][7])
    if HorrorMovieChoice == "2":
        SomeList.append(movie[1][2])
        print(f"Movie Name: {movie[1][2]}")
        print(f"First Time Slot: {movie[1][4]} on {movie[1][6]}")
        print(f"Second Time Slot: {movie[1][5]} on {movie[1][7]}")
        Showtime = input("Choose your show time (1-2): ")
        if Showtime == "1":
            SomeList.append(movie[1][4])
            SomeList.append(movie[1][6])
        if Showtime == "2":
            SomeList.append(movie[1][5])
            SomeList.append(movie[1][7])
    if HorrorMovieChoice == "3":
        SomeList.append(movie[2][2])
        print(f"Movie Name: {movie[2][2]}")
        print(f"First Time Slot: {movie[2][4]} on {movie[2][6]}")
        print(f"Second Time Slot: {movie[2][5]} on {movie[2][7]}")
        Showtime = input("Choose your show time (1-2): ")
        if Showtime == "1":
            SomeList.append(movie[2][4])
            SomeList.append(movie[2][6])
        if Showtime == "2":
            SomeList.append(movie[2][5])
            SomeList.append(movie[2][7])
    if HorrorMovieChoice == "4":
        SomeList.append(movie[3][2])
        print(f"Movie Name: {movie[3][2]}")
        print(f"First Time Slot: {movie[3][4]} on {movie[3][6]}")
        print(f"Second Time Slot: {movie[3][5]} on {movie[3][7]}")
        Showtime = input("Choose your show time (1-2): ")
        if Showtime == "1":
            SomeList.append(movie[3][4])
            SomeList.append(movie[3][6])
        if Showtime == "2":
            SomeList.append(movie[3][5])
            SomeList.append(movie[3][7])
    #User choose action movie
    if Genre == "2":
        print ("Available Movies")
        print ("MovieID , MovieGenre , MovieName , MovieDuration , MovieTime1 , MovieTime2 , MovieDate1 , MovieDate2")
        movie = movieData.getMovie("Action")
        ActionMovieChoice = input("Choose your movie (1-4): ")
        if ActionMovieChoice == "1":
            SomeList.append(movie[0][2])
            print(f"Movie Name: {movie[0][2]}")
            print(f"First Time Slot: {movie[0][4]} on {movie[0][6]}")
            print(f"Second Time Slot: {movie[0][5]} on {movie[0][7]}")
            Showtime = input("Choose your show time (1-2): ")
            if Showtime == "1":
                SomeList.append(movie[0][4])
                SomeList.append(movie[0][6])
            if Showtime == "2":
                SomeList.append(movie[0][5])
                SomeList.append(movie[0][7])
        if ActionMovieChoice == "2":
            SomeList.append(movie[1][2])
            print(f"Movie Name: {movie[1][2]}")
            print(f"First Time Slot: {movie[1][4]} on {movie[1][6]}")
            print(f"Second Time Slot: {movie[1][5]} on {movie[1][7]}")
            Showtime = input("Choose your show time (1-2): ")
            if Showtime == "1":
                SomeList.append(movie[1][4])
                SomeList.append(movie[1][6])
            if Showtime == "2":
                SomeList.append(movie[1][5])
                SomeList.append(movie[1][7])
        if ActionMovieChoice == "3":
            SomeList.append(movie[2][2])
            print(f"Movie Name: {movie[2][2]}")
            print(f"First Time Slot: {movie[2][4]} on {movie[2][6]}")
            print(f"Second Time Slot: {movie[2][5]} on {movie[2][7]}")
            Showtime = input("Choose your show time (1-2): ")
            if Showtime == "1":
                SomeList.append(movie[2][4])
                SomeList.append(movie[2][6])
            if Showtime == "2":
                SomeList.append(movie[2][5])
                SomeList.append(movie[2][7])
        if ActionMovieChoice == "4":
            SomeList.append(movie[3][2])
            print(f"Movie Name: {movie[3][2]}")
            print(f"First Time Slot: {movie[3][4]} on {movie[3][6]}")
            print(f"Second Time Slot: {movie[3][5]} on {movie[3][7]}")
            Showtime = input("Choose your show time (1-2): ")
            if Showtime == "1":
                SomeList.append(movie[3][4])
                SomeList.append(movie[3][6])
            if Showtime == "2":
                SomeList.append(movie[3][5])
                SomeList.append(movie[3][7])

    #User choose fantasy movie
    if Genre == "3":
        print ("Available Movies")
        print ("MovieID , MovieGenre , MovieName , MovieDuration , MovieTime1 , MovieTime2 , MovieDate1 , MovieDate2")
        movie = movieData.getMovie("Fantasy")
        FantasyMovieChoice = input("Choose your movie (1-4): ")
        if FantasyMovieChoice == "1":
            SomeList.append(movie[0][2])
            print(f"Movie Name: {movie[0][2]}")
            print(f"First Time Slot: {movie[0][4]} on {movie[0][6]}")
            print(f"Second Time Slot: {movie[0][5]} on {movie[0][7]}")
            Showtime = input("Choose your show time (1-2): ")
            if Showtime == "1":
                SomeList.append(movie[0][4])
                SomeList.append(movie[0][6])
            if Showtime == "2":
                SomeList.append(movie[0][5])
                SomeList.append(movie[0][7])
        if FantasyMovieChoice == "2":
            SomeList.append(movie[1][2])
            print(f"Movie Name: {movie[1][2]}")
            print(f"First Time Slot: {movie[1][4]} on {movie[1][6]}")
            print(f"Second Time Slot: {movie[1][5]} on {movie[1][7]}")
            Showtime = input("Choose your show time (1-2): ")
            if Showtime == "1":
                SomeList.append(movie[1][4])
                SomeList.append(movie[1][6])
            if Showtime == "2":
                SomeList.append(movie[1][5])
                SomeList.append(movie[1][7])
        if FantasyMovieChoice == "3":
            SomeList.append(movie[2][2])
            print(f"Movie Name: {movie[2][2]}")
            print(f"First Time Slot: {movie[2][4]} on {movie[2][6]}")
            print(f"Second Time Slot: {movie[2][5]} on {movie[2][7]}")
            Showtime = input("Choose your show time (1-2): ")
            if Showtime == "1":
                SomeList.append(movie[2][4])
                SomeList.append(movie[2][6])
            if Showtime == "2":
                SomeList.append(movie[2][5])
                SomeList.append(movie[2][7])
        if FantasyMovieChoice == "4":
            SomeList.append(movie[3][2])
            print(f"Movie Name: {movie[3][2]}")
            print(f"First Time Slot: {movie[3][4]} on {movie[3][6]}")
            print(f"Second Time Slot: {movie[3][5]} on {movie[3][7]}")
            Showtime = input("Choose your show time (1-2): ")
            if Showtime == "1":
                SomeList.append(movie[3][4])
                SomeList.append(movie[3][6])
            if Showtime == "2":
                SomeList.append(movie[3][5])
                SomeList.append(movie[3][7])
    #User choose romance movie
    if Genre == "4":
        print ("Available Movies")
        print ("MovieID , MovieGenre , MovieName , MovieDuration , MovieTime1 , MovieTime2 , MovieDate1 , MovieDate2")
        movie = movieData.getMovie("Romance")
        RomanceMovieChoice = input("Choose your movie (1-4): ")
        if RomanceMovieChoice == "1":
            SomeList.append(movie[0][2])
            print(f"Movie Name: {movie[0][2]}")
            print(f"First Time Slot: {movie[0][4]} on {movie[0][6]}")
            print(f"Second Time Slot: {movie[0][5]} on {movie[0][7]}")
            Showtime = input("Choose your show time (1-2): ")
            if Showtime == "1":
                SomeList.append(movie[0][4])
                SomeList.append(movie[0][6])
            if Showtime == "2":
                SomeList.append(movie[0][5])
                SomeList.append(movie[0][7])
        if RomanceMovieChoice == "2":
            SomeList.append(movie[1][2])
            print(f"Movie Name: {movie[1][2]}")
            print(f"First Time Slot: {movie[1][4]} on {movie[1][6]}")
            print(f"Second Time Slot: {movie[1][5]} on {movie[1][7]}")
            Showtime = input("Choose your show time (1-2): ")
            if Showtime == "1":
                SomeList.append(movie[1][4])
                SomeList.append(movie[1][6])
            if Showtime == "2":
                SomeList.append(movie[1][5])
                SomeList.append(movie[1][7])
        if RomanceMovieChoice == "3":
            SomeList.append(movie[2][2])
            print(f"Movie Name: {movie[2][2]}")
            print(f"First Time Slot: {movie[2][4]} on {movie[2][6]}")
            print(f"Second Time Slot: {movie[2][5]} on {movie[2][7]}")
            Showtime = input("Choose your show time (1-2): ")
            if Showtime == "1":
                SomeList.append(movie[2][4])
                SomeList.append(movie[2][6])
            if Showtime == "2":
                SomeList.append(movie[2][5])
                SomeList.append(movie[2][7])
        if RomanceMovieChoice == "4":
            SomeList.append(movie[3][2])
            print(f"Movie Name: {movie[3][2]}")
            print(f"First Time Slot: {movie[3][4]} on {movie[3][6]}")
            print(f"Second Time Slot: {movie[3][5]} on {movie[3][7]}")
            Showtime = input("Choose your show time (1-2): ")
            if Showtime == "1":
                SomeList.append(movie[3][4])
                SomeList.append(movie[3][6])
            if Showtime == "2":
                SomeList.append(movie[3][5])
                SomeList.append(movie[3][7])
    #User choose scifi movie
    if Genre == "5":
        print ("Available Movies")
        print ("MovieID , MovieGenre , MovieName , MovieDuration , MovieTime1 , MovieTime2 , MovieDate1 , MovieDate2")
        movie = movieData.getMovie("SciFi")
        SciFiMovieChoice = input("Choose your movie (1-4): ")
        if SciFiMovieChoice == "1":
            SomeList.append(movie[0][2])
            print(f"Movie Name: {movie[0][2]}")
            print(f"First Time Slot: {movie[0][4]} on {movie[0][6]}")
            print(f"Second Time Slot: {movie[0][5]} on {movie[0][7]}")
            Showtime = input("Choose your show time (1-2): ")
            if Showtime == "1":
                SomeList.append(movie[0][4])
                SomeList.append(movie[0][6])
            if Showtime == "2":
                SomeList.append(movie[0][5])
                SomeList.append(movie[0][7])
        if SciFiMovieChoice == "2":
            SomeList.append(movie[1][2])
            print(f"Movie Name: {movie[1][2]}")
            print(f"First Time Slot: {movie[1][4]} on {movie[1][6]}")
            print(f"Second Time Slot: {movie[1][5]} on {movie[1][7]}")
            Showtime = input("Choose your show time (1-2): ")
            if Showtime == "1":
                SomeList.append(movie[1][4])
                SomeList.append(movie[1][6])
            if Showtime == "2":
                SomeList.append(movie[1][5])
                SomeList.append(movie[1][7])
        if SciFiMovieChoice == "3":
            SomeList.append(movie[2][2])
            print(f"Movie Name: {movie[2][2]}")
            print(f"First Time Slot: {movie[2][4]} on {movie[2][6]}")
            print(f"Second Time Slot: {movie[2][5]} on {movie[2][7]}")
            Showtime = input("Choose your show time (1-2): ")
            if Showtime == "1":
                SomeList.append(movie[2][4])
                SomeList.append(movie[2][6])
            if Showtime == "2":
                SomeList.append(movie[2][5])
                SomeList.append(movie[2][7])
        if SciFiMovieChoice == "4":
            SomeList.append(movie[3][2])
            print(f"Movie Name: {movie[3][2]}")
            print(f"First Time Slot: {movie[3][4]} on {movie[3][6]}")
            print(f"Second Time Slot: {movie[3][5]} on {movie[3][7]}")
            Showtime = input("Choose your show time (1-2): ")
            if Showtime == "1":
                SomeList.append(movie[3][4])
                SomeList.append(movie[3][6])
            if Showtime == "2":
                SomeList.append(movie[3][5])
                SomeList.append(movie[3][7])
    print(SomeList)

    print("Available Seats")
    
    seatData.printSeat(seatData.getSeat())

    userDesiredSeatRow = input("Which seat row do you prefer? (A-J) : ")
    userDesiredSeatNumber = int(input("Which seat number do you prefer? (1-10): "))

    seatData.bookSeat(userDesiredSeatRow,userDesiredSeatNumber)

    SomeList.append(userDesiredSeatRow)
    SomeList.append(userDesiredSeatNumber)

    print(SomeList)


    # DONT DELETE
    # This is making the tickiet.
    setComfirmationList(SomeList,"new")
    ticket.generateTicket()
    

import ticket


def setComfirmationList(someList,action=None):
    if action== "new" or action =="update":
        setComfirmationList.list = someList
    if action == "getList":
        return setComfirmationList.list

def getComfirmationList():
    return setComfirmationList(list(),action="getList")
    


