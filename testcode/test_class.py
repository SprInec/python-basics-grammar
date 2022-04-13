# ----------------------------测试类--------------------------------#
"""
                     unittest 模块中的断言方法
     | ---------------------------------------------------------- |
     |                                                            |  
     |   assertEqual(a, b)                 核实 a == b            |
     |                                                            |
     |   assertNotEqual(a, b)              核实 a != b            |
     |                                                            |
     |   assertTrue(x)                     核实 x 为 True         |
     |                                                            |
     |   assertFalse(x)                    核实 x 为 False        |
     |                                                            |
     |   assertIn(item, list)              核实 item 在 list 中   |
     |                                                            |
     |   assertNotIn(item, list)           核实 item 不在 list 中 |
     | ---------------------------------------------------------- |

"""
# ----------------------一个要测试的类------------------------------#
# survey.py
class AnonymousSurvey:
	"""收集匿名调查问卷的答案"""

	def __init__(self, question):
		"""存储一个问题，并为存储答案做准备"""
		self.question = question
		self.responses = []

	def show_question(self):
		"""显示调查问卷"""
		print(self.question)

	def store_responses(self, new_response):
		"""存储单份调查答卷"""
		self.responses.append(new_response)

	def show_results(self):
		"""显示收集到的所有答卷"""
		print("Survey results: ")
		for response in responses:
			print(f"- {response}")