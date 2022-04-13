# 1
def make_sandwich(*toppings):
	"""概述制作一个三明治所加配料"""
	print("\nMaking a sandwich with following toppings:")
	for topping in toppings:
		print(f"-{topping}")

make_sandwich('onion', 'pepper', 'toofo')

# 2 
def build_profile(first, last, **user_info):
	"""创建一个字典，其中包含我们知道的有关用户的一切
		** 让Python创建一个空字典，并将收到的所有名称
		值对都放到这个字典中"""
	user_info['first_name'] = first.title()
	user_info['last_name'] = last.title()
	return user_info

messageofme = build_profile('li', 'miingzhe',
				height=176,
				weight=132)
print(messageofme)

