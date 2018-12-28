from API import VkAPI as API
import threading


class SecondDivision:
    def __init__(self, listOfVkScript, token):
        self.listOfVkScript = listOfVkScript
        self.token = token
        self.data = []

    def execute(self):
        listOutput = []
        for item in self.listOfVkScript:
            temp = API.getExecute(item, self.token)
            listOutput.append(temp)
        self.data = listOutput

    def getData(self):
        return self.data


# input: list of users' ids
# output: list of lists of friends
def getListOfFriends(allTheUsers, twoTokens, threadName):
    firstList, secondList = getHalfOfVkScript(allTheUsers)
    firstList, secondList = makeSecondDivision(firstList, secondList, twoTokens, threadName)
    return getFullList(firstList, secondList)


def getHalfOfVkScript(allTheUsers):
    listOfVkScript = API.getVkScriptForExecute(allTheUsers)

    middle = len(listOfVkScript) // 2
    firstList = listOfVkScript[:middle]
    secondList = listOfVkScript[middle:]
    return firstList, secondList


def makeSecondDivision(firstList, secondList, twoTokens, threadName):
    firstHalfSecondDivision = SecondDivision(firstList, twoTokens[1])
    secondHalfSecondDivision = SecondDivision(secondList, twoTokens[2])

    firstList = threading.Thread(target=firstHalfSecondDivision.execute, name=threadName + 'Second Division - 1')
    secondList = threading.Thread(target=secondHalfSecondDivision.execute, name=threadName + 'Second Division - 2')

    firstList.start()
    secondList.start()

    firstList.join()
    secondList.join()

    firstList = firstHalfSecondDivision.getData()
    secondList = secondHalfSecondDivision.getData()
    return firstList, secondList


def getFullList(firstList, secondList):
    listOutput = firstList + secondList
    returnList = []
    for item in listOutput:
        for iterator in item:
            returnList.append(iterator)
    return returnList
