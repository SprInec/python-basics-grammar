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


class IceCreamStand(Restaurant):
	"""冰激凌小店"""

	def __init__(self, restaurant_name, cuisine_type):
		"""初始化父类属性"""
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = ['strawberry', 'pineapple', 'banana', 'orange']

	def show_icecream_flavors(self):
		print("The flavors are following:")
		for flavor in self.flavors:
			print(f"\t- {flavor}")

my_icecreamstand = IceCreamStand('Pupo', 'chinese')
my_icecreamstand.show_icecream_flavors()

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


class Admin(User):
	"""管理员"""

	def __init__(self, first_name, last_name, age, sex):
		super().__init__(first_name, last_name, age, sex)
		self.privileges = [
							"can add post",
							"can delete post",
							"can ban user",
							]

	def show_privileges(self):
		"""显示管理员权限"""
		print(f"Hello, {self.first_name.title()} {self.last_name.title()}!")
		print("You have these privileges as following:")
		for privilege in self.privileges:
			print(f"\t- {privilege}")

july = Admin('li', 'mingzhe', 18, 'male')
july.show_privileges()

# 3
class Privileges:
	"""权限"""

	def __init__(self):
		self.privileges = [
							"can add post",
							"can delete post",
							"can ban user",
							]

	def show_privileges(self):
		"""显示管理员权限"""
		print("You have these privileges as following:")
		for privilege in self.privileges:
			print(f"\t- {privilege}")


class Admin(User):
	"""管理员"""

	def __init__(self, first_name, last_name, age, sex):
		super().__init__(first_name, last_name, age, sex)
		self.privileges = Privileges()

july = Admin('li', 'mingzhe', 18, 'male')
july.privileges.show_privileges()


# 4
class Car:
	"""一次模拟汽车的简单尝试"""

	def __init__(self, make, model, year):
		"""初始化描述汽车的属性"""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""返回整洁的描述信息"""
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

	def read_odometer(self):
		"""打印一条指出汽车里程的信息"""
		print(f"This car has {self.odometer_reading} miles on it.")

	# 修改属性值的方法
	def update_odometer(self, mileage):
		"""
		将里程表读数修改为指定的值
		禁止将里程表读书往回调
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self, miles):
		""""将里程表读数增加指定的量"""

		if miles > 0:
			self.odometer_reading += miles
		else:
			print("You can't roll back an odometer!")

class Battery:
	"""一次模拟电动汽车电瓶的简单尝试"""

	def __init__(self, battery_size = 75):
		"""初始化电瓶的属性"""
		self.battery_size = battery_size

	def describe_battery(self):
		"""打印一条描述电瓶容量的消息"""
		print(f"This car has a {self.battery_size}-kwh battery.")

	def get_range(self):
		"""打印一条信息，指出电瓶的续航里程"""
		if self.battery_size == 75:
			range = 260
		elif self.battery_size == 100:
			range = 315

		print(f"This car can go about {range} miles on a full charge.")

	def upgrade_battery(self):
		"""电瓶升级"""
		if self.battery_size != 100:
			self.battery_size = 100

class ElectricCar(Car):
	'''电动汽车的独特之处'''

	def __init__(self, make, model, year):
		"""
		初始化父类的属性。
		再初始化电动汽车特有的属性。
		"""
		super().__init__(make, model, year)
		'''super()让其能够调用父类的方法'''
		self.battery = Battery() #修改点

	def fill_gas_tank(self):
		"""电动汽车没有油箱"""
		print("This car doesn't need a gas tank!")


my_e_car = ElectricCar('china', 'a4', 2021)
my_e_car.battery.get_range()
my_e_car.battery.upgrade_battery()
my_e_car.battery.get_range()