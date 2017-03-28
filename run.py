import vk
import time
from functools import reduce
from config import password


session = vk.AuthSession('5947572', 'everemeenko@gmail.com', password)
api = vk.API(session)

# список моих друзей
my_friends = api.friends.get(user_id='313338073')

# список друзей моих друзей
d = {}
for friend in my_friends:
    try:
        d[friend] = api.friends.get(user_id=str(friend))
    except vk.exceptions.VkAPIError:
        continue
    time.sleep(1)


# поиск общих друзей
friends_sets = map(set, d.values())
mutual_friends = reduce(lambda set1, set2: set1 & set2, friends_sets)


print(mutual_friends)
