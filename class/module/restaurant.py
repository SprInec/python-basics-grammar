"""一组可用于表示餐馆的类"""

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
