# --------------------------使用if语句处理列表------------------------------- #
# -------------检查特殊元素------------#
requested_toppings = ['mushroom', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print("Sorry, we are out of green peppers right now.")
	else:
		print(f"Adding {requested_topping}.")

print("\nFinish making your pizza.")

#------------检查列表是否为空-------------#
requested_toppings = []

if requested_toppings: #若列表不为空其值为 True
	for requested_topping in requested_toppings:
		if requested_topping == 'green peppers':
			print("Sorry, we are out of green peppers right now.")
		else:
			print(f"Adding {requested_topping}.")
else:
	print("Are you sure you want a plain pizza?")

print("\n Finish making your pizza.")

#---------------使用多个列表----------------#
available_toppings = ['mushrooms', 'olives', 'green peppers', 
						'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"Adding {requested_topping}.")
	else:
		print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza.")

