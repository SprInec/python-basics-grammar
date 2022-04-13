# 1 """喜欢的数"""
import json

filename = 'like_number.json'

number = input("Which number you best like? ")
with open(filename, 'w') as f:
	json.dump(number, f)

with open(filename) as f:
	number = json.load(f)
	print(f"I know you best like {number}!")

# 2  """记住喜欢的数"""
import json

filename = 'like_number.json'

try:
	with open(filename) as f:
		number = json.load(f)
		print(f"I know you best like {number}!")
except FileNotFoundError:
	number = input("Which number you best like? ")
	json.dump(number, f)

# 3 """验证用户"""
import json

def get_stored_username():
	"""如果存储了用户名，就获取它"""
	filename = 'username.json'

	try:
		with open(filename) as f:
			username = json.load(f)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username():
	"""提示用户输入用户名"""

	username = input("What's your name? ")
	filename = 'username.json'
	with open(filename, 'w') as f:
			json.dump(username, f)
	return username

def greet_user():
	"""问候用户， 并指出其名字"""

	username = get_stored_username()
	if username:
		res = input("Is this your name? (yes/no)")
		if res == 'yes':
			print(f"Welcome back, {username}!")
		else:
			username = get_new_username()
	else:
		username = get_new_username()
		print(f"We'll remember you when you come back, {username}!")
