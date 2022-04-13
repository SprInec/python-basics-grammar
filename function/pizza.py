def make_pizza(size, *toppings):
	"""概述要制作的披萨"""
	print(f"\nMaking a {size}-ich pizza whth the following toppings:")
	for topping in toppings:
		print(f"- {topping}")