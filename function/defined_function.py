# ---------------------定义函数-----------------------#
# greeter.py
def greet_user1():
	"""显示简单的问候语"""
	print("Hello!")

greet_user1()

# ------------------向函数传递信息---------------------# 
def greet_user2(username):
	print(f"Hello, {username.title()}!")

greet_user2('jesse')

# -------------------------------实参和形参----------------------------------#
# --------------------传递实参--------------------------#
# pets.py

""" 1.位置实参 """
def describe_pet(animal_type, pet_name):
	"""显示宠物信息"""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
# 多次调用
describe_pet('dog', 'willie')

""" 2.关键字实参 """
def describe_pet(animal_type, pet_name):
	"""显示宠物信息"""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='dog', pet_name='willie')

# ----------编写函数时可给形参指定默认值------------#
"""在定义函数使用默认值时，未使用默认值的形参
   必须在使用了默认值形参的前面"""

def describe_pet(pet_name, animal_type='dog'):
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('willie')



