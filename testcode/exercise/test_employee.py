import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

	def setUp(self):
		self.july = Employee('li', 'ming', 10_000_000)

	def test_give_default_raise(self):
		self.july.give_raise(7_000_000)
		self.assertEqual(self.july.salary, 17_000_000)

	def test_give_custom_raise(self):
		money = 5000
		self.july.give_raise(money)
		self.assertTrue(money)

if __name__ == '__main__':
	unittest.main()
