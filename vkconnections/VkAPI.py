import requests
import math
import time
from json import loads
from vkconnections import APIKeys as c

keys = {}

def setKeys(vkKeys):
    global keys
    keys = vkKeys


def getUsers(usersUrl):
    global keys
    temp = None
    count = 0
    while temp is None:
        response = requests.get(c.usersGet.format(str(usersUrl), keys[0])).text
        response = loads(response)
        temp = response.get('response')
        if count > 1:
            time.sleep(1)
        count += 1
        if count == 50:
            return None
    return response.get('response')


def getFriends(id):
    temp = None
    count = 0
    while temp is None:
        response = requests.get(c.friendsGet.format(str(id), keys[0])).text
        response = loads(response)
        temp = response.get('response')
        if count > 1:
            time.sleep(1)
        count += 1
        if count == 50:
            return None
    return response.get('response').get('items')


def getExecute(code, token):
    temp = None
    count = 0
    while temp is None:
        myString = c.executeGet.format(code, token)
        execute = requests.get(myString).text
        execute = loads(execute)
        temp = execute.get('response')
        if count > 1:
            time.sleep(1)
        count += 1
        if count == 50:
            return None
    return execute.get('response')


def getVkScriptForExecute(allTheFriends):
    lenFriends = len(allTheFriends)
    requestsCount = lenFriends // 25 + math.ceil((lenFriends - lenFriends // 25 * 25) / 25)
    outputString = []
    startIndex = 0
    endIndex = 25
    for number in range(0, requestsCount):
        requestString = 'return [ '
        for item in range(startIndex, endIndex):
            if lenFriends > item:
                requestString += 'API.friends.get({"user_id": ' + str(allTheFriends[item]) + ' }), '
        requestString = requestString[0:-2]
        requestString += ' ];'
        outputString.append(requestString)
        startIndex += 25
        endIndex += 25
    return outputString

def getVkScriptForUsersExecute(allTheUsers):
    requestString = 'return [ '
    for index in range(len(allTheUsers)):
        stringOfUsers = ""
        for item in allTheUsers[index]:
            stringOfUsers += str(item) + ','
        stringOfUsers = stringOfUsers[0:-1]
        requestString += 'API.users.get({"user_ids": "' + stringOfUsers + '", "fields": "photo_100" }), '
    requestString = requestString[0:-1]
    requestString += ' ];'
    return requestString
