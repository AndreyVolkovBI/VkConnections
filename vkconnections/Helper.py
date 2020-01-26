import random


def get_pure_link(link):
    link = link.strip().lower()
    if 'vk.com/' in link:
        link = link.split('vk.com/')[1]
    if link.startswith('/'):
        link = link.split('/')[1]
    if link.endswith('/'):
        link = link.split('/')[0]
    if link.startswith('id'):
        link = link[2:]
    return link


def check_for_normal_length(friends_user_from, friends_user_to):
    if len(friends_user_from) + len(friends_user_to) > 1500:
        if len(friends_user_from) > len(friends_user_to):
            friends_user_from = list_cut(friends_user_from)
            friends_user_from, friends_user_to = check_for_normal_length(friends_user_from, friends_user_to)
        else:
            friends_user_to = list_cut(friends_user_to)
            friends_user_from, friends_user_to = check_for_normal_length(friends_user_from, friends_user_to)
    return friends_user_from, friends_user_to


def list_cut(friends_list):
    random.shuffle(friends_list)
    cut = len(friends_list) // 2
    return friends_list[:cut]


def clear_circles(circles):
    circles = {k: v for k, v in circles.items() if v is not None}
    circles = {k: v for k, v in circles.items() if v is not False}
    return circles


def get_items(circles):
    returnDict = {}
    for key in circles:
        returnDict[key] = circles[key].get('items')
    return returnDict


def fill_all_the_vertices(circles):
    tempDict = {}
    for item in circles:
        for index in circles[item]:
            if index not in circles:
                if tempDict.get(index):
                    tempDict[index].append(item)
                else:
                    tempDict[index] = [item]
    for item in tempDict:
        circles[item] = tempDict[item]
    return circles


def make_lists_nicer(output_list):
    result_list, temp_list = [], []
    for index in output_list:
        for item in index:
            temp_list.append({
                'id': item['id'],
                'full_name': item['first_name'] + ' ' + item['last_name'],
                'photo': item['photo_100']
            })
        result_list.append(temp_list)
        temp_list = []
    return result_list


def bfs(s, adjacency):
    parent = {s: None}
    frontier = [s]
    while frontier:
        next = []
        for u in frontier:
            if u in adjacency:
                for v in adjacency[u]:
                    if v not in parent:
                        parent[v] = u
                        next.append(v)
        frontier = next
    return parent


def get_way(parents, list_final, user_to):
    for item in parents:
        if item == user_to:
            list_final.append(parents[item])
            get_way(parents, list_final, parents[item])
    return list_final


def algorithm(parents, user_to):
    listFinal = get_way(parents, [], user_to)
    if listFinal:
        listFinal.remove(None)
        listFinal.reverse()
        listFinal.append(user_to)
        return listFinal
    else:
        return []


def get_way_count(output):
    if isinstance(output, list):
        return [len(item) for item in output]
    return None
