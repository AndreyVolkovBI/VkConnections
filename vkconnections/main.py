from vkconnections import FirstLevel as algo
from vkconnections import APIKeys, VkAPI


def get_way_between(user_from, user_to, keys):
    """
    Implements logic of getting user ids, finding its friends and friends of its friends

    :param user_from: [user id or nickname] to start search
    :param user_to: [user id or nickname] to end search
    :param keys: list of 4 keys specified in constructor of VkConnection class
    :return: list of 3 different paths between two given users
    """
    APIKeys.set_keys(keys)
    users = VkAPI.get_users(user_from + ',' + user_to)
    if users:
        user_from, user_to = users[0].get('id'), users[1].get('id')

        code = VkAPI.get_vk_script_for_execute([user_from, user_to])[0]

        friends = VkAPI.get_execute(code, keys[1])
        friends_user_from = friends[0].get('items')  # list of ids of friends of user_from
        friends_user_to = friends[1].get('items', False)  # list of ids of friends of user_to

        if not friends_user_from and friends_user_to:
            raise RuntimeError(
                "Failed to get friends for user: " + user_from + ". " +
                "Check that users has public access and account is not closed."
            )
        if len(friends_user_from) == 0 or len(friends_user_to) == 0:
            raise RuntimeError("One of the users: " + user_from + " or " + user_to + " has no friends")
        result = algo.calculations(user_from, friends_user_from, user_to, friends_user_to, keys)
        if len(result) == 0:
            raise RuntimeError("The distance between two users is too far")
        return result
    else:
        raise RuntimeError("One or both of the users were not found: [" + user_from + ", " + user_to + "]")
