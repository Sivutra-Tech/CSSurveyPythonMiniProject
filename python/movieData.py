
def getGenre():
    listOfGenres = ["Romantic","Action","Horror","Sci-Fi","Fantasy"]
    return listOfGenres

def getMovie(genre):
    with open(fileLocation,"r") as movieData:
        data = csv.reader(movieData)
        resultMovieList = []
        for row in data:
            if row[1] == genre:
                print(row)
                resultMovieList.append(row)
        
    return resultMovieList
                

# Adding and Removing Movies
import csv

fileLocation = './python/data.csv'

def addMovie(MovieID,MovieGenre,MovieName,MovieDuration,MovieTime1,MovieTime2,MovieDate1,MovieDate2):
    with open(fileLocation,"a") as movieData:
        # movie = ['Movie_ID', 'Movie_Genre', 'Movie_Name', 'Movie_Duration', 'Movie_Time_1', 'Movie_Time_2', 'Movie_Date_1', 'Movie_Date_2']

        movie = [MovieID,MovieGenre,MovieName,MovieDuration,MovieTime1,MovieTime2,MovieDate1,MovieDate2]
        data = csv.writer(movieData)

        data.writerow(movie)

def removeMovie(movieID):
    with open(fileLocation,'r',newline='') as movieData:
        reader = csv.reader(movieData)
        bigAllMovie = []
        for row in reader:
            if row[0] == movieID:
                continue
            bigAllMovie.append(row)

    with open(fileLocation,"w") as movieData:
        writer = csv.writer(movieData)
        for row in bigAllMovie:
            writer.writerow(row)
    
def addGenres(listOfGenres, whatToBeAdded):
  listOfGenres.append(whatToBeAdded)

def printGenres(listOfGenres):
  num = 1
  for genre in listOfGenres:
    print(f"{num}. {genre} ")
    num+=1