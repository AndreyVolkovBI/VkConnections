from API import VkAPI as API, APIKeys as k
from SearchLogic import FirstLevel as algo


# works for get way between users only
def getWayBetween(fromId, toId, keys):
    API.setKeys(keys)
    users = API.getUsers(fromId + ',' + toId)
    if users:
        fromId = users[0].get('id')  # id userFrom
        toId = users[1].get('id')  # id of userTo

        code = API.getVkScriptForExecute([fromId, toId])[0]
        friends = API.getExecute(code, keys[1])
        friendsUserFrom = friends[0].get('items')  # list of ids of friends of userFrom
        friendsUserTo = friends[1].get('items', False)  # list of ids of friends of userTo
        if not friendsUserFrom and friendsUserTo:
            return k.noSuchUser
        if len(friendsUserFrom) == 0 or len(friendsUserTo) == 0:
            return k.noFriends
        result = algo.calculations(fromId, friendsUserFrom, toId, friendsUserTo, keys)
        if len(result) == 0:
            return k.tooFar
        return result
    return k.noSuchUser