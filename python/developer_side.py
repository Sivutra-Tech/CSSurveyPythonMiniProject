import csv

fileLocation = "/python/movieData.csv"

with open(fileLocation,'r') as movieData:
    data = csv.reader(movieData)
    for line in data:
        print(line)