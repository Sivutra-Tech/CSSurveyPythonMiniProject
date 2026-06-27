import csv
# use function to call for the movie and store it in a variable
fileLocation = './python/data.csv'

with open(fileLocation,'r') as movieData:
    data = csv.reader(movieData)
    next(data)


def addMovie(MovieID,MovieGenre,MovieName,MovieDuration,MovieTime1,MovieTime2,MovieDate1,MovieDate2):
    with open(fileLocation,"a") as movieData:
        # movie = ['Movie_ID', 'Movie_Genre', 'Movie_Name', 'Movie_Duration', 'Movie_Time_1', 'Movie_Time_2', 'Movie_Date_1', 'Movie_Date_2']

        movie = [MovieID,MovieGenre,MovieName,MovieDuration,MovieTime1,MovieTime2,MovieDate1,MovieDate2]
        data = csv.writer(movieData)

        data.writerow(movie)

def removeMovie(MovieID):
    with open(fileLocation,'r')