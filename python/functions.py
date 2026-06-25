def addGenres(listOfGenres, whatToBeAdded):
  listOfGenres.append(whatToBeAdded)

def printGenres(listOfGenres):
  num = 1
  for genre in listOfGenres:
    print(f"{num}. {genre} ")
    num+=1
    
def printSeat(allOfTheSeat):
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