import functions
import movieData as movie
import seatData as seat


#Pick Genre

functions.printGenres(movie.getGenre())


functions.printSeat(seat.getSeat())

#List of 5 available movie genre
print ("Here is the list of genre")
genre= ["horror", "action", "fantasy", "romance", "scifi"]
num= 0
for movie in genre:
    num+= 1
    print(f"{num}. {movie}")

#List of 10 movies available in each genre
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

#User choose their favorite genre
Genre= str(input("Choose your genre: "))
number= 0

#User choose horror film
horror= horror_movie
if Genre.lower() == "horror":
    print("here is the list of 10 horror movie")
    for i in horror_movie:
        number += 1
        print(f"{number}. {i}")

#USer choose action movie
action= action_movie
if Genre.lower() == "action":
    print("here is the list of 10 action movie")
    for x in action_movie:
        number += 1
        print(f"{number}. {x}")
fantasy= fantasy_movie
if Genre.lower() == "fantasy":
    print("here is the list of 10 fantasy movie")
    for y in fantasy_movie:
        number += 1
        print(f"{number}. {y}")

#User choose romance movie
romance= romance_movie
if Genre.lower() == "romance":
    print("here is the list of 10 romance movie")
    for z in romance_movie:
        number += 1
        print(f"{number}. {z}")

#User choose scifi movie
scifi= sci_fi_movie
if Genre.lower() == "scifi":
    print("here is the list of 10 scifi movie")
    for v in sci_fi_movie:
        number += 1
        print(f"{number}. {v}")
