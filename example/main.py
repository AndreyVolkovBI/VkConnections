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
