from operator import truediv

import functions
import movieData
import seatData as seat

#Menu
print("Menu")
print("1. Book a Movie")
print("2. Check Booking")
print("3. Cancel Booking")
print("4. Exit")

userChoice = int(input("What would you like to do?: "))

if userChoice == 4:
    exit()
elif userChoice == 1:
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
elif userChoice == 2:
    print("Checking Booking")

elif userChoice == 3:
    print("Canceling Booking")
