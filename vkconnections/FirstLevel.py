from vkconnections import VkAPI as API
from vkconnections import SecondLevel as division, Helper as h
import threading

firstPair, secondPair = {1: "", 2: ""}, {1: "", 2: ""}

class FirstDivision:
    def __init__(self, twoTokens, friends, threadName):
        self.twoTokens = twoTokens
        self.friends = friends
        self.threadName = threadName
        self.data = {}

    def makeCalculations(self):
        self.data = division.getListOfFriends(self.friends, self.twoTokens, self.threadName)

    def getData(self):
        return self.data


def calculations(fromId, friendsUserFrom, toId, friendsUserTo, keys):
    global firstPair
    global secondPair

    firstPair = {1: keys[0], 2: keys[1]}
    secondPair = {1: keys[2], 2: keys[3]}

    friendsUserFrom, friendsUserTo = h.checkForNormalLength(friendsUserFrom, friendsUserTo)
    firstHalfOfFriends, secondHalfOfFriends = getHalfOfFriends(friendsUserFrom, friendsUserTo)

    adjFrom, adjTo = makeFirstDivision(firstHalfOfFriends, secondHalfOfFriends)

    circles = getCircles(friendsUserFrom, friendsUserTo, adjFrom, adjTo, fromId, toId)

    allTheWays = getWays(fromId, toId, circles)

    outputList = API.getExecute(API.getVkScriptForUsersExecute(allTheWays), firstPair[1])
    resultList = h.makeListsNicer(outputList)
    return resultList


def getHalfOfFriends(friendsUserFrom, friendsUserTo):
    allTheFriends = friendsUserFrom + friendsUserTo
    middle = len(allTheFriends) // 2
    firstHalfOfFriends = allTheFriends[:middle]
    secondHalfOfFriends = allTheFriends[middle:]
    return firstHalfOfFriends, secondHalfOfFriends


def makeFirstDivision(firstHalfOfFriends, secondHalfOfFriends):
    firstHalfFirstDivision = FirstDivision(firstPair, firstHalfOfFriends, 'First half: ')
    secondHalfFirstDivision = FirstDivision(secondPair, secondHalfOfFriends, 'Second half: ')

    adjFrom = threading.Thread(target=firstHalfFirstDivision.makeCalculations, name='FirstDivision - 1')
    adjTo = threading.Thread(target=secondHalfFirstDivision.makeCalculations, name='FirstDivision - 2')

    adjFrom.start()
    adjTo.start()

    adjFrom.join()
    adjTo.join()

    # now adj is a dictionary where key - id of a person, value - ids of his friends
    adjFrom = firstHalfFirstDivision.getData()
    adjTo = secondHalfFirstDivision.getData()
    return adjFrom, adjTo


def getCircles(friendsUserFrom, friendsUserTo, adjFrom, adjTo, fromId, toId):
    circles = {}
    allFirstFriends = friendsUserFrom + friendsUserTo  # temp
    allAdj = adjFrom + adjTo

    for index in range(len(allAdj)):
        circles[allFirstFriends[index]] = allAdj[index]

    circles = h.clearCircles(circles)
    circles = h.getItems(circles)

    circles[fromId] = friendsUserFrom
    circles[toId] = friendsUserTo
    circles = h.fillAllTheVertices(circles)
    return circles


def getWays(fromId, toId, circles):
    allTheWays = []
    count = 1
    parents = h.BFS(s=fromId, Adj=circles)
    way = h.algorithm(parents, toId)
    allTheWays.append(way)

    while way and count < 3:
        count += 1
        way = way[1:-1]
        for item in way:
            circles.pop(item)
        parents = h.BFS(s=fromId, Adj=circles)
        way = h.algorithm(parents, toId)
        allTheWays.append(way)
    return allTheWays
