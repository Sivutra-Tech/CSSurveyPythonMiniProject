def addGenres(listOfGenres, whatToBeAdded):
  listOfGenres.append(whatToBeAdded)
    
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