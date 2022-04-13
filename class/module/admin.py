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