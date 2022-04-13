# ------------------------传递任意数量的实参--------------------------#
# pizza.py
# *toppings   
""" * 让Python创建一个名为 toppings 的空元组
		并将所有接收到的值封装到这个元组中"""

def  make_pizza(*toppings):
	"""打印顾客点的所有配料"""
	print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

""" 可将函数调用的 print() 替换为一个循环
		遍历配料表对顾客点的配料进行描述   """
def make_pizza(*toppings):
	"""概述要制作的披萨"""
	print("\nMaking a pizza with the following toppings:")
	for topping in toppings:
		print(f"-{topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# -----------------结合使用位置实参和任意数量实参------------------ #

""" *args 用于收集任意数量的位置实参 """

def make_pizza(size, *toppings):
	print(f"\nMaking a {size} pizza with the following toppings:")
	for topping in toppings:
		print(f"-{topping}")

make_pizza( 'big', 'pepperoni')
make_pizza('small', 'mushrooms', 'green peppers', 'extra cheese')

# ------------------使用任意数量的关键字形参-----------------------#
# user_profile.py

""" **kwargs 用于收集任意数量的关键字实参 """

def build_profile(first, last, **user_info):
	"""创建一个字典，其中包含我们知道的有关用户的一切
		** 让Python创建一个空字典，并将收到的所有名称
		值对都放到这个字典中"""
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info

user_profile = build_profile('albert', 'einstein',
								location = 'princeton',
								field = 'physics')
print(user_profile)



