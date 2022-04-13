# -------------------------创建和使用类-------------------------- #
# -------------创建 Dog 类------------ #
class Dog:
	"""一次模拟小狗的简单尝试"""

	def __init__(self, name, age):
		"""初始化属性 name 和 age"""
		self.name = name
		self.age = age

	def sit(self):
		"""模拟小狗收到命令时蹲下"""
		print(f"{self.name} is now sitting.")

	def roll_over(self):
		"""模拟小狗收到命令时打滚"""
		print(f"{slef.name} rolled over!")


# -----------根据类创建实例--------------- #
my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)
my_dog.sit()

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")