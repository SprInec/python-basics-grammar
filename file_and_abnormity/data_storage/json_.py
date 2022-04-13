# ---------------------------存储数据-----------------------------#
# -------------------json.dump()-----------------------#
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f:
	json.dump(numbers, f)

# -------------------json.load()------------------------#
import json

filename = 'numbers.json'
with open(filename) as f:
	numbers = json.load(f)

print(numbers)

# ----------------------------保存和读取用户生成的数据------------------------#
# remember_me.py
import json

username = input("What's your name? ")

filename = 'username.json'
with open(filename, 'w') as f:
	json.dump(username, f)
	print(f"We'll remember you when you come back, {username}!")

# greet_user.py
import json 

filename = 'username.json'

with open(filename) as f:
	username = json.load(f)
	print(f"Welcome back, {username}!")

# ----合并---- #
# remrember_me.py
import json

# 如果以前存储了用户名，就加载它
# 否则，提示用户输入用户名并存储它
filename = 'username.json'
try:
	with open(filename) as f:
		username = json.load(f)
except FileNotFoundError:
	username = input("What's your name? ")
	with open(filename, 'w') as f:
		json.dump(username, f)
		print(f"We'll remember you when you come back, {username}!")
else:
	print(f"Welcome back, {username}!")

# -----------------------------重构--------------------------------#
"""
   代码能够正确的运行，但通过将其划分为一系列完成具体工作的函数，还可以改进。
   这样的过程成为重构。重构让代码更清晰、更易于理解、更容易扩展。
"""

def greet_user():
	"""问候用户， 并指出其名字"""

	filename = 'username.json'

	try:
		with open(filename) as f:
			username = json.load(f)
	except FileNotFoundError:
		username = input("What's your name? ")
		with open(filename, 'w') as f:
			json.dump(username, f)
			print(f"We'll remember you when you come back, {username}!")
	else:
		print(f"Welcome back, {username}!")

greet_user()


# ----重构1----- #
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

def greet_user():
	"""问候用户， 并指出其名字"""

	username = get_stored_username()
	if username:
		print(f"Welcome back, {username}!")
	else:
		username = input("What's your name? ")
		with open(filename, 'w') as f:
			json.dump(username, f)
			print(f"We'll remember you when you come back, {username}!")

greet_user()

# ------重构2----- #
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
		print(f"Welcome back, {username}!")
	else:
		username = get_new_username()
		print(f"We'll remember you when you come back, {username}!")

