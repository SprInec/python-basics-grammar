# -------------------------单元测试和测试用例-----------------------#
"""
      Python 标准库中的模块 unittest 提供了代码测试工具

      单元测试用于核实函数某个方面没有问题
      测试用例是一组单元测试，他们一道核实函数在各种情形下的行为都符合要求

"""
# ---------可通过的测试-----------#
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
	"""测试 name_function.py """

	def test_first_last_name(self):
		"""能够正确地处理像 Janis Joplin 这样的姓名吗？"""
		formatted_name = get_formatted_name('janis', 'joplin')
		self.assertEqual(formatted_name, 'Janis Joplin') #断言方法：核实与期望结果是否一致

if __name__ == '__main__':
	unittest.main()

# -----------未通过的测试------------#
import unittest
from name_new_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
	"""测试 name_function.py """

	def test_first_last_name(self):
		"""能够正确地处理像 Janis Joplin 这样的姓名吗？"""
		formatted_name = get_formatted_name('janis', 'joplin')
		self.assertEqual(formatted_name, 'Janis Joplin') #断言方法：核实与期望结果是否一致

if __name__ == '__main__':
	unittest.main()

# ------------------------添加新测试------------------------#
import unittest
from name_new_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
	"""测试 name_function.py """

	def test_first_last_name(self):
		"""能够正确地处理像 Janis Joplin 这样的姓名吗？"""
		formatted_name = get_formatted_name('janis', 'joplin')
		self.assertEqual(formatted_name, 'Janis Joplin') #断言方法：核实与期望结果是否一致

	def test_first_last_middle_name(self):
		"""能够正确的处理像 Wolfgang Amadeus Mozart 这样的姓名吗？ """
		formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
		self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
	unittest.main()