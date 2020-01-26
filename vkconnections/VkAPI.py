import math
import time
import requests
from json import loads
from vkconnections import APIKeys


def get_users(users_url):
    return get_request(APIKeys.users_get.format(str(users_url), APIKeys.first_pair[1]))


def get_friends(id):
    response = get_request(APIKeys.friends_get.format(str(id), APIKeys.first_pair[1]))
    return response.get('items')


def get_execute(code, token):
    return get_request(APIKeys.execute_get.format(code, token))


def get_request(url):
    response, count = None, 0
    while response is None:
        response = requests.get(url).text
        response = loads(response)
        response = response.get('response')
        if count > 1:
            time.sleep(1)
        count += 1
        if count == 50:
            raise RuntimeError("Failed to execute get request for url: " + url)
        elif response:
            return response


def get_vk_script_for_execute(all_the_friends):
    len_friends = len(all_the_friends)
    requests_count = len_friends // 25 + math.ceil((len_friends - len_friends // 25 * 25) / 25)
    output_string = []
    start_index, end_index = 0, 25
    for number in range(0, requests_count):
        request_string = 'return [ '
        for item in range(start_index, end_index):
            if len_friends > item:
                request_string += 'API.friends.get({"user_id": ' + str(all_the_friends[item]) + ' }), '
        request_string = request_string[0:-2]
        request_string += ' ];'
        output_string.append(request_string)
        start_index += 25
        end_index += 25
    return output_string


def get_vk_script_for_users_execute(all_the_users):
    request_string = 'return [ '
    for index in range(len(all_the_users)):
        users_string = ""
        for item in all_the_users[index]:
            users_string += str(item) + ','
        users_string = users_string[0:-1]
        request_string += 'API.users.get({"user_ids": "' + users_string + '", "fields": "photo_100" }), '
    request_string = request_string[0:-1]
    request_string += ' ];'
    return request_string
