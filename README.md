# Vk Connections
![version](https://img.shields.io/badge/version-0.0.9-blue) 
![rating](https://img.shields.io/badge/rating-★★★★☆-brightgreen)
![rating](https://img.shields.io/badge/contributing-welcome-yellow)

Library that finds the shortest path from one vk user to another through friends.
## VkConnection class
`class VkConnections(keys)`

Parameters:
- keys - list of 4 Vk api keys (user or community access)

Note that keys is a list with exactly 4 api keys, this requires fast work of library (each request being processed under 30 sec)

## Methods of VkConnection class

`get_connection(user_from, user_to)`

Parameters:
- user_from – id/nickname/link to user A
- user_to – id/nickname/link to user B

Result:
A list of lists of dictionaries {id: person_id, full_name: person_full_name, photo: person_photo}

`print_result(result)` - prints the result from main method

## Installation
`pip install vkconnections`

## Example
```python
import vkconnections as vc

# vk api keys
keys = ["xxx1", "xxx2", "xxx3", "xxx4"]

user_from = "alsu"
user_to = "dm"

# creating object VkConnection with keys
vk = vc.VkConnection(keys)

# getting path between users
result = vk.get_connection(user_from, user_to)

# printing result
vk.print_connection(result)
```
Output:
```
Id: 75791 Name: Алсу Гарифуллина
Id: 238471470 Name: Анна Разумова
Id: 42348347 Name: Владимир Бурматов
Id: 53083705 Name: Дмитрий Медведев

Id: 75791 Name: Алсу Гарифуллина
Id: 15081069 Name: Lana Windsor
Id: 4502282 Name: Елена Бочерова
Id: 53083705 Name: Дмитрий Медведев

Id: 75791 Name: Алсу Гарифуллина
Id: 442049258 Name: Дмитрий Андрущенко
Id: 16350900 Name: Иван Засурский
Id: 53083705 Name: Дмитрий Медведев
```
