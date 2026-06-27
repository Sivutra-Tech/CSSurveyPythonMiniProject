from operator import truediv

import functions
import movieData
import seatData as seat


#Making a Menu (Test)


#Pick Genre
print("something")

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
Genre= input("Choose your genre: ")

#User choose horror film
if Genre == "1" :
   print ("Available Movies")
   print ("MovieID , MovieGenre , MovieName , MovieDuration , MovieTime1 , MovieTime2 , MovieDate1 , MovieDate2")
   movie = movieData.getMovie("Horror")
   HorrorMovieChoice= input("Choose your movie (1-4): ")
   if HorrorMovieChoice == "1":
       print (f"Movie Name: {movie[0][2]}")
       print (f"First Time Slot: {movie[0][4]} on {movie[0][6]}")
       print (f"Second Time Slot: {movie[0][5]} on {movie[0][7]}")
   if HorrorMovieChoice == "2":
       print(f"Movie Name: {movie[1][2]}")
       print(f"First Time Slot: {movie[1][4]} on {movie[1][6]}")
       print(f"Second Time Slot: {movie[1][5]} on {movie[1][7]}")
   if HorrorMovieChoice == "3":
       print(f"Movie Name: {movie[2][2]}")
       print(f"First Time Slot: {movie[2][4]} on {movie[2][6]}")
       print(f"Second Time Slot: {movie[2][5]} on {movie[2][7]}")
   if HorrorMovieChoice == "4":
       print(f"Movie Name: {movie[3][2]}")
       print(f"First Time Slot: {movie[3][4]} on {movie[3][6]}")
       print(f"Second Time Slot: {movie[3][5]} on {movie[3][7]}")

#User choose action movie
if Genre == "2":
    print ("Available Movies")
    print ("MovieID , MovieGenre , MovieName , MovieDuration , MovieTime1 , MovieTime2 , MovieDate1 , MovieDate2")
    movie = movieData.getMovie("Action")
    ActionMovieChoice = input("Choose your movie (1-4): ")
    if ActionMovieChoice == "1":
        print(f"Movie Name: {movie[0][2]}")
        print(f"First Time Slot: {movie[0][4]} on {movie[0][6]}")
        print(f"Second Time Slot: {movie[0][5]} on {movie[0][7]}")
    if ActionMovieChoice == "2":
        print(f"Movie Name: {movie[1][2]}")
        print(f"First Time Slot: {movie[1][4]} on {movie[1][6]}")
        print(f"Second Time Slot: {movie[1][5]} on {movie[1][7]}")
    if ActionMovieChoice == "3":
        print(f"Movie Name: {movie[2][2]}")
        print(f"First Time Slot: {movie[2][4]} on {movie[2][6]}")
        print(f"Second Time Slot: {movie[2][5]} on {movie[2][7]}")
    if ActionMovieChoice == "4":
        print(f"Movie Name: {movie[3][2]}")
        print(f"First Time Slot: {movie[3][4]} on {movie[3][6]}")
        print(f"Second Time Slot: {movie[3][5]} on {movie[3][7]}")

#User choose fantasy movie
if Genre == "3":
    print ("Available Movies")
    print ("MovieID , MovieGenre , MovieName , MovieDuration , MovieTime1 , MovieTime2 , MovieDate1 , MovieDate2")
    movie = movieData.getMovie("Fantasy")
    FantasyMovieChoice = input("Choose your movie (1-4): ")
    if FantasyMovieChoice == "1":
        print(f"Movie Name: {movie[0][2]}")
        print(f"First Time Slot: {movie[0][4]} on {movie[0][6]}")
        print(f"Second Time Slot: {movie[0][5]} on {movie[0][7]}")
    if FantasyMovieChoice == "2":
        print(f"Movie Name: {movie[1][2]}")
        print(f"First Time Slot: {movie[1][4]} on {movie[1][6]}")
        print(f"Second Time Slot: {movie[1][5]} on {movie[1][7]}")
    if FantasyMovieChoice == "3":
        print(f"Movie Name: {movie[2][2]}")
        print(f"First Time Slot: {movie[2][4]} on {movie[2][6]}")
        print(f"Second Time Slot: {movie[2][5]} on {movie[2][7]}")
    if FantasyMovieChoice == "4":
        print(f"Movie Name: {movie[3][2]}")
        print(f"First Time Slot: {movie[3][4]} on {movie[3][6]}")
        print(f"Second Time Slot: {movie[3][5]} on {movie[3][7]}")

#User choose romance movie
if Genre == "4":
    print ("Available Movies")
    print ("MovieID , MovieGenre , MovieName , MovieDuration , MovieTime1 , MovieTime2 , MovieDate1 , MovieDate2")
    movie = movieData.getMovie("Romance")
    RomanceMovieChoice = input("Choose your movie (1-4): ")
    if RomanceMovieChoice == "1":
        print(f"Movie Name: {movie[0][2]}")
        print(f"First Time Slot: {movie[0][4]} on {movie[0][6]}")
        print(f"Second Time Slot: {movie[0][5]} on {movie[0][7]}")
    if RomanceMovieChoice == "2":
        print(f"Movie Name: {movie[1][2]}")
        print(f"First Time Slot: {movie[1][4]} on {movie[1][6]}")
        print(f"Second Time Slot: {movie[1][5]} on {movie[1][7]}")
    if RomanceMovieChoice == "3":
        print(f"Movie Name: {movie[2][2]}")
        print(f"First Time Slot: {movie[2][4]} on {movie[2][6]}")
        print(f"Second Time Slot: {movie[2][5]} on {movie[2][7]}")
    if RomanceMovieChoice == "4":
        print(f"Movie Name: {movie[3][2]}")
        print(f"First Time Slot: {movie[3][4]} on {movie[3][6]}")
        print(f"Second Time Slot: {movie[3][5]} on {movie[3][7]}")

#User choose scifi movie
if Genre == "5":
    print ("Available Movies")
    print ("MovieID , MovieGenre , MovieName , MovieDuration , MovieTime1 , MovieTime2 , MovieDate1 , MovieDate2")
    movie = movieData.getMovie("SciFi")
    SciFiMovieChoice = input("Choose your movie (1-4): ")
    if SciFiMovieChoice == "1":
        print(f"Movie Name: {movie[0][2]}")
        print(f"First Time Slot: {movie[0][4]} on {movie[0][6]}")
        print(f"Second Time Slot: {movie[0][5]} on {movie[0][7]}")
    if SciFiMovieChoice == "2":
        print(f"Movie Name: {movie[1][2]}")
        print(f"First Time Slot: {movie[1][4]} on {movie[1][6]}")
        print(f"Second Time Slot: {movie[1][5]} on {movie[1][7]}")
    if SciFiMovieChoice == "3":
        print(f"Movie Name: {movie[2][2]}")
        print(f"First Time Slot: {movie[2][4]} on {movie[2][6]}")
        print(f"Second Time Slot: {movie[2][5]} on {movie[2][7]}")
    if SciFiMovieChoice == "4":
        print(f"Movie Name: {movie[3][2]}")
        print(f"First Time Slot: {movie[3][4]} on {movie[3][6]}")
        print(f"Second Time Slot: {movie[3][5]} on {movie[3][7]}")

Showtime= input("Choose your show time: ")
###########################
##########################
