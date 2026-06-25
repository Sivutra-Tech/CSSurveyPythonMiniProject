#Pick Genre
def addGenres(listOfGenres, whatToBeAdded):
  listOfGenres.append(whatToBeAdded)

def printGenres(listOfGenres):
  num = 1
  for genre in listOfGenres:
    print(f"{num}. {genre} ")
    num+=1

listOfGenres = ["Romantic","Action","Horror","Sci-Fi","Fantasy"]
printGenres(listOfGenres)

# Printing Seats
allOfTheSeat = [
    [1,2,3,4,5,6,7,8,9,10], #A (1.Num) (1.9 = A9)
    [1,2,3,4,5,6,7,8,9,10], #B
    [1,2,3,4,5,6,7,8,9,10], #C
    [1,2,3,4,5,6,7,8,9,10], #D
    [1,2,3,4,5,6,7,8,9,10], #E
    [1,2,3,4,5,6,7,8,9,10], #F
    [1,2,3,4,5,6,7,8,9,10], #G
    [1,2,3,4,5,6,7,8,9,10], #H
    [1,2,3,4,5,6,7,8,9,10], #I
    [1,2,3,4,5,6,7,8,9,10], #J
]

def printSeat():
  letter = ["A","B","C","D","E","F","G","H","I","J"]
  tempNumLetter = 0
  for row in allOfTheSeat:
    print(f"{letter[tempNumLetter]}: ", end="")
    for colum in row:
      print(f"[{colum}]", end=" ")
    print("\n")
    tempNumLetter+=1
def pickSeat(row,colum):
    pass

printSeat()