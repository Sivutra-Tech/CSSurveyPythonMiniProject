import csv
# use function to call for the movie and store it in a variable
fileLocation = './python/data.csv'

with open(fileLocation,'r') as movieData:
    data = csv.reader(movieData)
    next(data)
    for line in data:
        print(line)
        print(type(line))

movie = ['Movie_ID', 'Movie_Genre', 'Movie_Name', 'Movie_Duration', 'Movie_Time_1', 'Movie_Time_2', 'Movie_Date_1', 'Movie_Date_2']
movie1 = ['100001', 'Horror', 'The conjuring', '120', '13:30', '15:30', '13-June-2026', '15-June-2026']
movie2 = ['100002', 'Horror', 'IT', '120', '11:30', '19:30', '13-June-2026', '15-June-2026']

movie1[0] #movieID
movie1