from vkconnections import main


class VkConnection:
    """
    VkConnection class - base class for making connection

    :param keys - list of 4 vk api keys, user or community access (in order to make search faster)
    """
    def __init__(self, keys):
        if len(keys) != 4:
            raise ValueError(
                "List of keys should have 4 different API keys. Read more: https://vk.com/dev/access_token"
            )
        self.keys = keys

    def get_connection(self, user_from, user_to):
        """
        Finds the shortest path between two vk users through their friends

        :param user_from: [user id or nickname] to start search
        :param user_to: [user id or nickname] to end search
        :return: list of 3 different paths between two given users
        """
        return main.get_way_between(user_from, user_to, self.keys)

    @staticmethod
    def print_connection(result, photo=False):
        """
        Prints result of `get_connection` method in a nice way

        :param result: result from `get_connection` method
        :param photo: boolean flag represents whether you should print photo url or not
        :return: Unit, prints result to standard output

        """
        for way in result:
            for person in way:
                s = "Id: " + str(person['id']) + " " + "Name: " + person['full_name']
                s += " Photo: " + person['photo'] if photo else ""
                print(s)
            print()
