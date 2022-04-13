# 雇员
class Employee():

	def __init__(self, first, last, salary):
		"""名、姓、年薪"""
		self.first = first
		self.last = last
		self.salary = salary

	def give_raise(self, raise_num = 5000):
		self.salary += raise_num

	

