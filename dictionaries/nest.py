# -------------------------嵌套---------------------------#
#将一系列字典储存在列表中，或将列表作为值存储在字典中。

# -------------------在列表中存储字典------------------ #
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print(alien)

# 创建一个用于存储外星人的空列表。
aliens = []

# 创建30个绿色的外星人。
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

# 将前三个外星人修改为黄色、速度中等且分值为10。
for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['points'] = 10
		alien['speed'] = 'medium'
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['points'] = 15
		alien['speed'] = 'fast'

# 显示前五个外星人。
for alien in aliens[:5]:
	print(alien)
print("...")

# 显示创建了多少个外星人。
print(f"Total number of aliens: {len(aliens)}")

# --------------------在字典中存储列表------------------- #
# 存储所点披萨的信息。
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
	}

# 概述所点的披萨。
print(f"You ordered a {pizza['crust']}-crust pizza"
	"with the following toppings:")

for topping in pizza['toppings']:
	print("\t" + topping)

#
favorite_language = {
	'jen': ['python', 'ruby'],
	'sarah': ['C'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
	}

for name, languages in favorite_language.items():
	if len(languages) == 1:
		print(f"\n{name.title()}'s favorite language is:")
	else:
		print(f"\n{name.title()}'s favorite language are:")
	for language in languages:
		print(f"\t{language.title()}")

# ----------------------在字典中存储字典----------------------#
users = {
	'aeinstein': {
		'first': 'albert',
		'last': 'einstein',
		'location': 'princeton',
		},

	'mcurie': {
		'first': 'marie',
		'last': 'curie',
		'location': 'paris',
		}

	}

for username, user_info in users.items():
	print(f'\nUsername: {username}')
	full_name = f"{user_info['first'].title()} {user_info['last'].title()}"
	location = user_info['location'].title()

	print(f"\tFull name: {full_name}")
	print(F"\tlocation: {location}")
