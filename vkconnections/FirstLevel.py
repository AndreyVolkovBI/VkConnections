import threading

from vkconnections import SecondLevel as division, Helper as h
from vkconnections import VkAPI as API

first_pair, second_pair = {1: "", 2: ""}, {1: "", 2: ""}


class FirstDivision:
    def __init__(self, two_tokens, friends, thread_name):
        self.twoTokens = two_tokens
        self.friends = friends
        self.threadName = thread_name
        self.data = {}

    def make_calculations(self):
        self.data = division.get_list_of_friends(self.friends, self.twoTokens, self.threadName)

    def get_data(self):
        return self.data


def calculations(from_id, friends_user_from, to_id, friends_user_to, keys):
    global first_pair
    global second_pair

    first_pair = {1: keys[0], 2: keys[1]}
    second_pair = {1: keys[2], 2: keys[3]}

    friends_user_from, friends_user_to = h.check_for_normal_length(friends_user_from, friends_user_to)
    first_half_friends, second_half_friends = get_half_of_friends(friends_user_from, friends_user_to)

    adj_from, adj_to = make_first_division(first_half_friends, second_half_friends)

    circles = get_circles(friends_user_from, friends_user_to, adj_from, adj_to, from_id, to_id)

    allTheWays = get_ways(from_id, to_id, circles)

    outputList = API.get_execute(API.get_vk_script_for_users_execute(allTheWays), first_pair[1])
    resultList = h.make_lists_nicer(outputList)
    return resultList


def get_half_of_friends(friends_user_from, friends_user_to):
    all_friends = friends_user_from + friends_user_to
    middle = len(all_friends) // 2
    first_half_friends = all_friends[:middle]
    second_half_friends = all_friends[middle:]
    return first_half_friends, second_half_friends


def make_first_division(first_half_of_friends, second_half_of_friends):
    first_half_first_division = FirstDivision(first_pair, first_half_of_friends, 'First half: ')
    second_half_first_division = FirstDivision(second_pair, second_half_of_friends, 'Second half: ')

    adj_from = threading.Thread(target=first_half_first_division.make_calculations, name='FirstDivision - 1')
    adj_to = threading.Thread(target=second_half_first_division.make_calculations, name='FirstDivision - 2')

    adj_from.start()
    adj_to.start()

    adj_from.join()
    adj_to.join()

    # now adj is a dictionary where key - id of a person, value - ids of his friends
    adj_from = first_half_first_division.get_data()
    adj_to = second_half_first_division.get_data()
    return adj_from, adj_to


def get_circles(friends_user_from, friends_user_to, adj_from, adj_to, from_id, to_id):
    circles = {}
    all_first_friends = friends_user_from + friends_user_to
    all_adj = adj_from + adj_to

    for index in range(len(all_adj)):
        circles[all_first_friends[index]] = all_adj[index]

    circles = h.clear_circles(circles)
    circles = h.get_items(circles)

    circles[from_id] = friends_user_from
    circles[to_id] = friends_user_to
    circles = h.fill_all_the_vertices(circles)
    return circles


def get_ways(from_id, to_id, circles):
    all_ways, count = [], 1
    parents = h.bfs(s=from_id, adjacency=circles)
    way = h.algorithm(parents, to_id)
    all_ways.append(way)

    while way and count < 3:
        count += 1
        way = way[1:-1]
        for item in way:
            circles.pop(item)
        parents = h.bfs(s=from_id, adjacency=circles)
        way = h.algorithm(parents, to_id)
        all_ways.append(way)
    return all_ways
