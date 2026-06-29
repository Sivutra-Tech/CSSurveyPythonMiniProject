import movieData
import seatData
def runBookAMovie():
    # List of 5 available movie genre
    print("Here is the list of genre")
    genre = ["horror", "action", "fantasy", "romance", "scifi"]
    num = 0
    for number in genre:
        num += 1
        print(f"{num}. {number}")
    # User choose their favorite genre
    Genre = input("Choose your genre: ")
    SomeList = []
    # User choose horror film
    if Genre == "1":
        movie = movieData.getMovie("Horror")
        movieData.print_available_movie("Horror")
        HorrorMovieChoice = input("Choose your movie (1-4): ")
        if HorrorMovieChoice == "1":
            SomeList.append(movie[0][2])
            Showtime = input("Choose your show time (1-2): ")
            if Showtime == "1":
                SomeList.append(movie[0][4])
                SomeList.append(movie[0][6])
            if Showtime == "2":
                SomeList.append(movie[0][5])
                SomeList.append(movie[0][7])
        elif HorrorMovieChoice == "2":
            SomeList.append(movie[1][2])
            Showtime = input("Choose your show time (1-2): ")
            if Showtime == "1":
                SomeList.append(movie[1][4])
                SomeList.append(movie[1][6])
            if Showtime == "2":
                SomeList.append(movie[1][5])
                SomeList.append(movie[1][7])
        elif HorrorMovieChoice == "3":
            SomeList.append(movie[2][2])
            Showtime = input("Choose your show time (1-2): ")
            if Showtime == "1":
                SomeList.append(movie[2][4])
                SomeList.append(movie[2][6])
            if Showtime == "2":
                SomeList.append(movie[2][5])
                SomeList.append(movie[2][7])
        elif HorrorMovieChoice == "4":
            SomeList.append(movie[3][2])
            Showtime = input("Choose your show time (1-2): ")
            if Showtime == "1":
                SomeList.append(movie[3][4])
                SomeList.append(movie[3][6])
            if Showtime == "2":
                SomeList.append(movie[3][5])
                SomeList.append(movie[3][7])
        else:
            print("Invalid Choice")
    # User choose action movie
    elif Genre == "2":
        movieData.print_available_movie("Action")
        movie = movieData.getMovie("Action")
        ActionMovieChoice = input("Choose your movie (1-4): ")
        if ActionMovieChoice == "1":
            SomeList.append(movie[0][2])
            Showtime = input("Choose your show time (1-2): ")
            if Showtime == "1":
                SomeList.append(movie[0][4])
                SomeList.append(movie[0][6])
            if Showtime == "2":
                SomeList.append(movie[0][5])
                SomeList.append(movie[0][7])
        if ActionMovieChoice == "2":
            SomeList.append(movie[1][2])
            Showtime = input("Choose your show time (1-2): ")
            if Showtime == "1":
                SomeList.append(movie[1][4])
                SomeList.append(movie[1][6])
            if Showtime == "2":
                SomeList.append(movie[1][5])
                SomeList.append(movie[1][7])
        if ActionMovieChoice == "3":
            SomeList.append(movie[2][2])
            Showtime = input("Choose your show time (1-2): ")
            if Showtime == "1":
                SomeList.append(movie[2][4])
                SomeList.append(movie[2][6])
            if Showtime == "2":
                SomeList.append(movie[2][5])
                SomeList.append(movie[2][7])
        if ActionMovieChoice == "4":
            SomeList.append(movie[3][2])
            Showtime = input("Choose your show time (1-2): ")
            if Showtime == "1":
                SomeList.append(movie[3][4])
                SomeList.append(movie[3][6])
            if Showtime == "2":
                SomeList.append(movie[3][5])
                SomeList.append(movie[3][7])

    # User choose fantasy movie
    elif Genre == "3":
        movieData.print_available_movie("Fantasy")
        movie = movieData.getMovie("Fantasy")
        FantasyMovieChoice = input("Choose your movie (1-4): ")
        if FantasyMovieChoice == "1":
            SomeList.append(movie[0][2])
            Showtime = input("Choose your show time (1-2): ")
            if Showtime == "1":
                SomeList.append(movie[0][4])
                SomeList.append(movie[0][6])
            if Showtime == "2":
                SomeList.append(movie[0][5])
                SomeList.append(movie[0][7])
        if FantasyMovieChoice == "2":
            SomeList.append(movie[1][2])
            Showtime = input("Choose your show time (1-2): ")
            if Showtime == "1":
                SomeList.append(movie[1][4])
                SomeList.append(movie[1][6])
            if Showtime == "2":
                SomeList.append(movie[1][5])
                SomeList.append(movie[1][7])
        if FantasyMovieChoice == "3":
            SomeList.append(movie[2][2])
            Showtime = input("Choose your show time (1-2): ")
            if Showtime == "1":
                SomeList.append(movie[2][4])
                SomeList.append(movie[2][6])
            if Showtime == "2":
                SomeList.append(movie[2][5])
                SomeList.append(movie[2][7])
        if FantasyMovieChoice == "4":
            SomeList.append(movie[3][2])
            Showtime = input("Choose your show time (1-2): ")
            if Showtime == "1":
                SomeList.append(movie[3][4])
                SomeList.append(movie[3][6])
            if Showtime == "2":
                SomeList.append(movie[3][5])
                SomeList.append(movie[3][7])
    # User choose romance movie
    elif Genre == "4":
        movieData.print_available_movie("Romance")
        movie = movieData.getMovie("Romance")
        RomanceMovieChoice = input("Choose your movie (1-4): ")
        if RomanceMovieChoice == "1":
            SomeList.append(movie[0][2])
            Showtime = input("Choose your show time (1-2): ")
            if Showtime == "1":
                SomeList.append(movie[0][4])
                SomeList.append(movie[0][6])
            if Showtime == "2":
                SomeList.append(movie[0][5])
                SomeList.append(movie[0][7])
        if RomanceMovieChoice == "2":
            SomeList.append(movie[1][2])
            Showtime = input("Choose your show time (1-2): ")
            if Showtime == "1":
                SomeList.append(movie[1][4])
                SomeList.append(movie[1][6])
            if Showtime == "2":
                SomeList.append(movie[1][5])
                SomeList.append(movie[1][7])
        if RomanceMovieChoice == "3":
            SomeList.append(movie[2][2])
            Showtime = input("Choose your show time (1-2): ")
            if Showtime == "1":
                SomeList.append(movie[2][4])
                SomeList.append(movie[2][6])
            if Showtime == "2":
                SomeList.append(movie[2][5])
                SomeList.append(movie[2][7])
        if RomanceMovieChoice == "4":
            SomeList.append(movie[3][2])
            Showtime = input("Choose your show time (1-2): ")
            if Showtime == "1":
                SomeList.append(movie[3][4])
                SomeList.append(movie[3][6])
            if Showtime == "2":
                SomeList.append(movie[3][5])
                SomeList.append(movie[3][7])
    # User choose scifi movie
    elif Genre == "5":
        movieData.print_available_movie("Sci_Fi")
        movie = movieData.getMovie("Sci_Fi")
        SciFiMovieChoice = input("Choose your movie (1-4): ")
        if SciFiMovieChoice == "1":
            SomeList.append(movie[0][2])
            Showtime = input("Choose your show time (1-2): ")
            if Showtime == "1":
                SomeList.append(movie[0][4])
                SomeList.append(movie[0][6])
            elif Showtime == "2":
                SomeList.append(movie[0][5])
                SomeList.append(movie[0][7])
            else:
                print("Invalid Choice")
        elif SciFiMovieChoice == "2":
            SomeList.append(movie[1][2])
            Showtime = input("Choose your show time (1-2): ")
            if Showtime == "1":
                SomeList.append(movie[1][4])
                SomeList.append(movie[1][6])
            elif Showtime == "2":
                SomeList.append(movie[1][5])
                SomeList.append(movie[1][7])
            else:
                print("Invalid Choice")
        elif SciFiMovieChoice == "3":
            SomeList.append(movie[2][2])
            Showtime = input("Choose your show time (1-2): ")
            if Showtime == "1":
                SomeList.append(movie[2][4])
                SomeList.append(movie[2][6])
            elif Showtime == "2":
                SomeList.append(movie[2][5])
                SomeList.append(movie[2][7])
            else:
                print("Invalid Choice")
        elif SciFiMovieChoice == "4":
            SomeList.append(movie[3][2])
            Showtime = input("Choose your show time (1-2): ")
            if Showtime == "1":
                SomeList.append(movie[3][4])
                SomeList.append(movie[3][6])
            elif Showtime == "2":
                SomeList.append(movie[3][5])
                SomeList.append(movie[3][7])
            else:
                print("Invalid Choice")
        else:
            print("Invalid Choice")
    else:
        print("Invalid Choice")

    print(SomeList)

    print("Available Seats")

    seatData.printSeat(seatData.getSeat())

    userDesiredSeatRow = input("Which seat row do you prefer? (A-J) : ")
    userDesiredSeatNumber = int(input("Which seat number do you prefer? (1-10): "))

    seatData.bookSeat(userDesiredSeatRow, userDesiredSeatNumber)

    SomeList.append(userDesiredSeatRow)
    SomeList.append(userDesiredSeatNumber)

    print(SomeList)


runBookAMovie()




