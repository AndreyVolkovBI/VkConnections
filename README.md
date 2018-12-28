# Vk Connections: the shortest path from one vk user to another
Library that finds the shortest path from one vk user to another through friends.
## VkConnection classes
`class Create(keys)`

Parametrs:
- keys - list of 4 Vk api keys (user or community access)

Note that keys is a list with exactly 4 api keys, this requires fast work of library (each request being processed under 30 sec)

## Methods of Create class

`getConnection(userFrom, userTo)`

Parameters:
- userFrom – id/nickname/link to user A
- userTo – id/nickname/link to user B

Result:
A list of lists of dictionaries {id: person_id, full_name: person_full_name, photo: person_photo}

`printResult(result)` - prints the result from main method

## Installation
`pip install vkconnections`

## Example
```python
import vkconnections

# Vk API Keys
firstKey = 'XXX'
secondKey = 'XXX'
thirdKey = 'XXX'
fourthKey = 'XXX'

keys = [firstKey, secondKey, thirdKey, fourthKey]  # all the keys in one list

vk = vkconnections.Create(keys)  # creating an instance of a class

# users for making a way
userFrom = "alsu"
userTo = "dm"

result = vk.getConnection(userFrom, userTo)  # receiving a result
vk.printConnection(result)  # printing result
```
Output:
```


```
