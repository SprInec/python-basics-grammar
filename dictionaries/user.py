#------------------------遍历字典---------------------------#
#-------------遍历所有键值对------------#
user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi',
	}

# 方法 .items() 用于返回一个键值对列表
for key, value in user_0.items():
	print(f"\nKey: {key}")
	print(f'Value: {value}')

#------------遍历字典中所有键-------------#
# 方法 keys()
for key in user_0.keys():
	print(key)


favorite_language = {
	'jen': 'Python',
	'sarah': 'C',
	'edward': 'ruby',
	'phil': 'Python',
	}
friends = ['phil', 'sarah']
for name in favorite_language.keys():
	print(f"Hi {name.title()}.")
	
	if name in friends:
		language = favorite_language[name].title()
		print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favorite_language.keys():
	print("Erin, please take our poll!")

# ---------------按特定顺序遍历字典中所有键-----------------#
# 可使用函数 sorted() 来获得按特定顺序排列的键列表的副本
favorite_language = {
	'jen': 'Python',
	'sarah': 'C',
	'edward': 'ruby',
	'phil': 'Python',
	}

for name in sorted(favorite_language.keys()):
	print(f"{name.title()}, thank you for taking the poll!")

# -----------------遍历字典中的所有值-------------------#
#方法 values() 
#该方法不会考虑值是否重复
print("The following language have been mentioned:")

for language in favorite_language.values():
	print(language.title())

#为避免值重复，可使用集合 set()
#集合中的每个元素必须是独一无二的
print("The following language have been mentioned:")

for language in set(favorite_language.values()):
	print(language.title())

# -----------------------集合--------------------------#
# 可使用一对花括号直接创建集合，并在其中用逗号分隔
# 集合区分大小写
language = {'Python', "C", "ruby", 'Python'}
print(language)