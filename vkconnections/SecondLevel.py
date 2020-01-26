import threading

from vkconnections import VkAPI as API


class SecondDivision:
    def __init__(self, list_of_vk_script, token):
        self.listOfVkScript = list_of_vk_script
        self.token = token
        self.data = []

    def execute(self):
        listOutput = []
        for item in self.listOfVkScript:
            temp = API.get_execute(item, self.token)
            listOutput.append(temp)
        self.data = listOutput

    def get_data(self):
        return self.data


# input: list of users' ids
# output: list of lists of friends
def get_list_of_friends(all_the_users, two_tokens, thread_name):
    firstList, secondList = get_half_of_vk_script(all_the_users)
    firstList, secondList = make_second_division(firstList, secondList, two_tokens, thread_name)
    return get_full_list(firstList, secondList)


def get_half_of_vk_script(all_the_users):
    list_of_vk_script = API.get_vk_script_for_execute(all_the_users)

    middle = len(list_of_vk_script) // 2
    first_list = list_of_vk_script[:middle]
    second_list = list_of_vk_script[middle:]
    return first_list, second_list


def make_second_division(first_list, second_list, two_tokens, thread_name):
    first_half_second_division = SecondDivision(first_list, two_tokens[1])
    second_half_second_division = SecondDivision(second_list, two_tokens[2])

    first_list = threading.Thread(target=first_half_second_division.execute, name=thread_name + 'Second Division - 1')
    second_list = threading.Thread(target=second_half_second_division.execute, name=thread_name + 'Second Division - 2')

    first_list.start()
    second_list.start()

    first_list.join()
    second_list.join()

    first_list = first_half_second_division.get_data()
    second_list = second_half_second_division.get_data()
    return first_list, second_list


def get_full_list(first_list, second_list):
    list_output = first_list + second_list
    return_list = []
    for item in list_output:
        for iterator in item:
            return_list.append(iterator)
    return return_list
