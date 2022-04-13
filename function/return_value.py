# ---------------------------返回值----------------------------- # 
# formatted_name.py
def get_formatted_name(first_name, last_name):
	"""返回整洁的姓名"""
	full_name = f"{first_name} {last_name}"
	return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# -----------------------让实参变成可选的------------------------- #
def get_formatted_name2(first_name, middle_name, last_name):
	full_name = f"{first_name} {middle_name} {last_name}"
	return full_name.title()

musician = get_formatted_name2('jimi', 'lee', 'hendrix')
print(musician)

# 有的人没有中间名
# 可将形参 middle_name 的默认值设为空字符串，并移至列表末尾
def get_formatted_name3(first_name, last_name, middle_name=''):
	if middle_name:
		# Python 将非空字符串检测为 True
		full_name = f"{first_name} {middle_name} {last_name}"
	else:
		full_name = f"{first_name} {last_name}"
	return full_name.title()

musician = get_formatted_name3('jimi', 'lee')
print(musician)

musician = get_formatted_name3('jimi', "lee", "hendrix")
print(musician)

# -------------------------返回字典-------------------------#
# 函数可返回任何类型的值
# person.py
def build_person(first_name, last_name):
	"""返回一个字典，其中包含关于一个人的信息"""
	person = {'first': first_name, 'last': last_name}
	return person

musician = build_person('jimi', 'hendrix')
print(musician)

def build_person1(first_name, last_name, age=None):
	person = {'first': first_name, 'last': last_name}
	if age:
		person['age'] = age
	return person

musician = build_person1('jimi', 'hendrix', age=27)
print(musician)

# -------------------结合使用函数和while循环------------------ #
# greeter.py
def get_formatted_name(first_name, last_name):
	"""返回整洁的名字"""
	full_name = f"{first_name} {last_name}"
	return full_name.title()

# 这是一个无限循环
while True:
	print("\nPlease tell me your name:")
	print("(Enter 'q' at any time to quit)")

	f_name = input("First_name: ")
	if f_name == 'q':
		break
	l_name = input("Last_name: ")
	if l_name == 'q':
		break

	formatted_name = get_formatted_name(f_name, l_name)
	print(f"\nHello, {formatted_name}!")