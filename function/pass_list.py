# ----------------------------传递列表-----------------------------#
# greet_users.py
def greet_users(names):
	"""向列表中的每位用户发出简单的问候"""
	for name in names:
		msg = f"Hello, {name.title()}!"
		print(msg)

usernames =  ['hanhan', 'ty', 'margot']
greet_users(usernames)

# -------------------------在函数中修改列表--------------------------#
# 列表传递给函数后，函数就可对列表进行永久性修改
# printing_models.py

# 首先创建一个列表，其中包含一些要打印的设计:
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# 模拟打印每个设计，直到没有来打印的设计为止
# 打印每个设计后，都将其移到列表 completed_models 中。
while unprinted_designs:
	current_design = unprinted_designs.pop()
	print(f"Printing model: {current_design}.")
	completed_models.append(current_design)

# 显示打印好的所有模型
print("\nThe following models have been printed:")
for completed_model in completed_models:
	print(completed_model)

# ----------------可编写两个函数处理这些代码------------------#
def print_models(unprinted_designs, completed_models):
	"""
	模拟打印每个设计，直到没有来打印的设计为止。
	打印每个设计后，都将其移到列表 completed_models 中。
	"""
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print(f"Printing model: {current_design}.")
		completed_models.append(current_design)

def show_completed_models(completed_models):
	"""显示打印好的所有模型"""
	print("\nThe following models have been printed:")
	for completed_model in completed_models:
		print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# ---------------------禁止函数修改列表------------------------#
# 可将列表的副本传递给函数以保留原来列表的信息。
# 切片表示法 [:] 创建列表副本。
print_models(unprinted_designs[:], completed_models)
