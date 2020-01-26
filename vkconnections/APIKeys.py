first_pair = {1: "", 2: ""}
second_pair = {1: "", 2: ""}


def set_keys(keys):
    global first_pair
    global second_pair
    first_pair = {1: keys[0], 2: keys[1]}
    second_pair = {1: keys[2], 2: keys[3]}


# Vk API Constants
api_url = 'https://api.vk.com/method/'
method_name_friends = 'friends.get?'
method_name_user = 'users.get?'
method_name_execute = 'execute?'
access_token = 'access_token='
version = 'v=5.92'

# users.get
users_get = api_url + method_name_user + 'user_ids=' + '{0}' + '&fields=photo_100' + '&' + access_token + '{1}' + '&' + version

# friends.get
friends_get = api_url + method_name_friends + 'user_id=' + '{0}' + '&' + access_token + '{1}' + '&' + version

# execute
execute_get = api_url + method_name_execute + 'code={}&' + access_token + '{}' + '&' + version
