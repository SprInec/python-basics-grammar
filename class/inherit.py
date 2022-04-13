# -----------------------------------继承------------------------------------ #
"""
	编写类时，并非总是要从空白开始。
	如果要编写的类是另一个现成类的特殊版本，可使用继承。
	一个类继承另一个类时，将自动获得另一个类的所有属性和方法。
	原有的类成为'父类'，而新类称为'子类'。
	子类继承了父类的所有属性和方法，同时还可以定义自己的属性和方法。
"""
# -----------子类的方法 __init__() ------------ #
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

class ElectricCar(Car):
	'''电动汽车的独特之处'''

	def __init__(self, make, model, year):
		"""初始化父类的属性"""
		super().__init__(make, model, year)
		'''super()让其能够调用父类的方法'''

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())

# ----------------------给子类定义属性和方法--------------------- #
class ElectricCar(Car):
	'''电动汽车的独特之处'''

	def __init__(self, make, model, year):
		"""
		初始化父类的属性。
		再初始化电动汽车特有的属性。
		"""
		super().__init__(make, model, year)
		'''super()让其能够调用父类的方法'''
		self.battery_size = 75

	def describe_battery(self):
		"""打印一条描述电瓶容量的消息"""
		print(f"This car has a {self.battery_size}-kwh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

# --------------------重写父类的方法------------------------ #
"""
	对于父类的方法，只要它不符合子类模拟的实物的行为
	都可以进行重写，可在子类中定义一个与要重写父类方
	法同名的方法，这样Python将不会考虑父类的方法，而
	只关注你在子类中定义的相应方法。
"""
class ElectricCar(Car):
	'''电动汽车的独特之处'''

	def __init__(self, make, model, year):
		"""
		初始化父类的属性。
		再初始化电动汽车特有的属性。
		"""
		super().__init__(make, model, year)
		'''super()让其能够调用父类的方法'''
		self.battery_size = 75

	def describe_battery(self):
		"""打印一条描述电瓶容量的消息"""
		print(f"This car has a {self.battery_size}-kwh battery.")

	def fill_gas_tank(self):
		"""电动汽车没有油箱"""
		print("This car doesn't need a gas tank!")

# --------------------将实例用作属性---------------------- #
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

my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

my_tesla.battery.get_range()

