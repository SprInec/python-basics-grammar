import unittest
from test_class import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
	"""针对AnonymousSurvey 类的测试"""

	def test_store_single_response(self):
		"""测试单个答案会被妥善存储"""
		question = "What language did you first learn to speak?"
		my_survey = AnonymousSurvey(question)
		my_survey.store_responses('English')
		self.assertIn('English', my_survey.responses)

	def test_store_three_responses(self):
		"""测试三个答案会被妥善存储"""
		question = "What language did you first learn to speak?"
		my_survey = AnonymousSurvey(question)
		responses = ['English', 'Chinese', 'Spanish']
		for response in responses:
			my_survey.store_responses(response)

		for response in responses:
			self.assertIn(response, my_survey.responses)

if __name__ == '__main__':
	unittest.main()

# 方法 setUp()
# 使得我们只需创建这些对象的实例一次就可以在每个测试方法中使用
class TestAnonymousSurvey(unittest.TestCase):
	"""针对AnonymousSurvey 类的测试"""

	def setUp(self):
		"""
		创建一个调查对象和一组答案，供使用的测试方法使用。
		"""
		question = "What language did you first learn to speak?"
		self.my_survey = AnonymousSurvey(question)
		self.responses = ['English', 'Chinese', 'Spanish']

	def test_store_single_response(self):
		"""测试单个答案会被妥善存储"""
		self.my_survey.store_responses(self.responses[0])
		self.assertIn(self.responses[0], self.my_survey.responses)

	def test_store_three_responses(self):
		"""测试三个答案会被妥善存储"""
		
		for response in self.responses:
			self.my_survey.store_responses(self.response)

		for response in self.responses:
			self.assertIn(self.response, my_survey.responses)

if __name__ == '__main__':
	unittest.main()