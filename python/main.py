import functions
import movieData as movie
import seatData as seat


#Pick Genre

functions.printGenres(movie.getGenre())


functions.printSeat(seat.getSeat())

horror_movie= [
    "The conjuring","IT","The Exorcist", "The shining", "Halloween",
    "The ring", "Insidious", "Sinister", "The Texas chainsaw man", "Evil Dead"
]
action_movie= [
    "Avenger infinity war", "Avenger Endgame", "Terminator 2: Judgement day", "Mission Impossible: Fallout",
    "Die Hard", "The Matrix", "Inception", "John Wick 1", "The Rock", "Gladiator"
]
romance_movie= [
    "Titanic", "Passengers", "Forrest Gump", "Before Sunset", "The Notebook",
    "The Kissing Booth", "Casablanca", "Notting Hill", "Roman Holiday", "Pride & Prejudice"
]
fantasy_movie= [
    "The Lord of the Rings", "Spirit Away", "Princess Mononoke", "Harry Potter", "The Wizard of OZ",
    "Avatar", "Your Name", "My Neighbour Totoro", "Stardust", "The Hobbit"
]
sci_fi_movie= [
    "Interstellar", "Blade Runner 2049", "The Thing", "Real Steel", "The Doctor",
    "Space Odyssey", "Planet of the Apes", "Alien", "Back to the Future", "Star Wars: The Empire Strikes Back"
]

Genre= str(input("Choose your genre: "))
horror= horror_movie
number= 0
if Genre == "horror":
    print("here is the list of horror movie")
    for i in horror_movie:
        number += 1
        print(f"{number}. {i}")
action= action_movie
if Genre == "action":
    print("here is the list of action movie")
    for x in action_movie:
        number += 1
        print(f"{number}. {x}")
fantasy= fantasy_movie
if Genre == "fantasy":
    print("here is the list of fantasy movie")
    for y in fantasy_movie:
        number += 1
        print(f"{number}. {y}")
romance= romance_movie
if Genre == "romance":
    print("here is the list of romance movie")
    for z in romance_movie:
        number += 1
        print(f"{number}. {z}")
scifi= sci_fi_movie
if Genre == "scifi":
    print("here is the list of scifi movie")
    for v in sci_fi_movie:
        number += 1
        print(f"{number}. {v}")