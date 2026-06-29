import bookAMovie
import random

testList = ["12-June-2026-123",]


def generateTicket():
    someList = bookAMovie.getComfirmationList()
    ticket = f"{someList[2]}-{random.randint(0,1001)}"
    someList.insert(0,ticket)

    bookAMovie.setComfirmationList(someList,action="update")


import csv
fileLocation = "./python/ticketStorage.csv"
def addTicketToStorage(comfirmationList):
    with open(fileLocation,"w") as file:
        writer = csv.writer(file)
        writer.writerow(comfirmationList)

def searchTicket(ticketID):
    with open(fileLocation,"r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == ticketID:
                print("eh?")
                print(row)
                print("eh?")
                return row
            
        return None


addTicketToStorage(["12-June-2026-213","The Avenger"])

result = searchTicket("12-June-2026-213")
if result:
    print(result)
else:
    print("Ticket Not Found")