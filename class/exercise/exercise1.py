# 1
class Restaurant:
	"""餐馆"""
	def __init__(self, restaurant_name, cuisine_type):
		"""初始化属性 restaurant_name 和 cuisine_type"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(f"The restaurant's name is {self.restaurant_name}.")
		print(f"The restaurant's cuisine type is {self.cuisine_type}.")

	def open_restaurant(self):
		print(f"The restaurant {self.restaurant_name} is open.")

mixi = Restaurant('niubi', 'chinese')
mixi.describe_restaurant()
mixi.open_restaurant()

print(f"the restaurant's name is {mixi.restaurant_name.title()}.")
print(f"the cuisine type is {mixi.cuisine_type}.")

# 2
class User:
	"""用户"""
	def __init__(self, first_name, last_name, age, sex):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.sex = sex

	def describe_user(self):
		print(f"\nThe user's name is {self.first_name.title()}"
				f" {self.last_name.title()}.")
		if self.sex == 'female':
			print(f'she is {self.age} years old.')
		else:
			print(f"he is {self.age} years old.")

	def greet_user(self):
		print(f"Hello, {self.first_name.title()} {self.last_name.title()}!")

july = User('liu', 'xiping', 18, 'male')
july.describe_user()
july.greet_user()

