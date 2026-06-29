import bookAMovie
import random


def generateTicket():
    someList = bookAMovie.getComfirmationList()
    ticket = f"{someList[2]}-{random.randint(0,1001)}"
    someList.insert(0,ticket)

    bookAMovie.setComfirmationList(someList,action="update")

