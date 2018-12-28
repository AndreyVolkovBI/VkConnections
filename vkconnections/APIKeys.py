firstPair = {1: "", 2: ""}
secondPair = {1: "", 2: ""}

def setKeys(keys):
	global firstPair
	global secondPair
	firstPair = {1: keys[0], 2: keys[1]}
	secondPair = {1: keys[2], 2: keys[3]}


# Vk API Constants
api_url = 'https://api.vk.com/method/'
method_name_friends = 'friends.get?'
method_name_user = 'users.get?'
method_name_execute = 'execute?'
access_token = 'access_token='
version = 'v=5.92'

# users.get
usersGet = api_url + method_name_user + 'user_ids=' + '{0}' + '&fields=photo_100' + '&' + access_token + '{1}' + '&' + version

# friends.get
friendsGet = api_url + method_name_friends + 'user_id=' + '{0}' + '&' + access_token + '{1}' + '&' + version

# execute
executeGet = api_url + method_name_execute + 'code={}&' + access_token + '{}' + '&' + version

# errors
noSuchUser = {'error': {'code': '001', 'message': 'The user is not found'}}
noFriends = {'error': {'code': '002', 'message': 'The user either does not have or has hidden friends'}}
tooFar = {'error': {'code': '002', 'message': 'The distance between two users is too far'}}