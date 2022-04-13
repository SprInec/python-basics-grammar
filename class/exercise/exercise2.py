# 1
class Restaurant:
	"""餐馆"""
	def __init__(self, restaurant_name, cuisine_type):
		"""初始化属性 restaurant_name 和 cuisine_type"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print(f"The restaurant's name is {self.restaurant_name}.")
		print(f"The restaurant's cuisine type is {self.cuisine_type}.")
		if self.number_served:
			print(f"The restaurant has {self.number_served} guests right now.")

	def open_restaurant(self):
		print(f"The restaurant {self.restaurant_name} is open.")

	def set_number_served(self, numbers):
		"""设置就餐人数"""
		self.number_served = numbers

	def increament_number_served(self, numbers):
		self.number_served += numbers

mixi = Restaurant('huaxi', 'chinese')
mixi.number_served  = 10
mixi.describe_restaurant()

mixi.set_number_served(100)
mixi.describe_restaurant()

mixi.increament_number_served(1000)
mixi.describe_restaurant()

# 2
class User:
	"""用户"""
	def __init__(self, first_name, last_name, age, sex):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.sex = sex
		self.login_attempts = 0 #尝试登录次数

	def describe_user(self):
		print(f"\nThe user's name is {self.first_name.title()}"
				f" {self.last_name.title()}.")
		if self.sex == 'female':
			print(f'she is {self.age} years old.')
		else:
			print(f"he is {self.age} years old.")
		print(f"This user has logined {self.login_attempts} times.")

	def greet_user(self):
		print(f"Hello, {self.first_name.title()} {self.last_name.title()}!")

	def increament_login_attempts(self):
		"""login_attempts值加一"""
		self.login_attempts += 1

	def reset_login_attempts(self):
		"""将属性login_attempts的值重置为0"""
		self.login_attempts = 0

july = User('liu', 'xiping', 18, 'male')
july.increament_login_attempts()
july.increament_login_attempts()
july.describe_user()
july.reset_login_attempts()
july.describe_user()
		