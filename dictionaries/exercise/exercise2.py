# 1
term_list = {
	'upper()': '将列表中所有字母大写',
	'lower()': '将列表中所有字母小写',
	'title()': '将列表中单词首字母大写',
	'strip()': '去除首尾空格',
	'get()': '用于访问字典值',
	}

for term, function in term_list.items():
	print(f"{term}: {function}")

# 2
river_list = {
	'ganges River': 'india',
	'Yellow River': 'china',
	'Egypt': 'nile',
	}

for river, country in river_list.items():
	print(f"the {river.title()} runs through {country.title()}.")

for river in river_list.keys():
	print(river.title())

for country in river_list.values():
	print(country.title())

# 3
survey_list = ['Alen', 'pini', 'keik', 'Faker']
surveyed_list = {
	'alen': 'yes',
	'Keik': 'no',
	}

# ------------------- 将列表字母全部(大)小写的方法示例 --------------------#

#新建一个用于存储原列表小(大)写后元素的空列表
surveyed_keys_lower_list = []

#通过循环一次提取原列表的每个元素
for value in surveyed_list.keys():
	#用方法 lower() 将提取出的元素小写后 在用方法 appen() 追加到空列表末尾
	surveyed_keys_lower_list.append(value.lower())

#---------------------------------------------------------------------------#

for person in survey_list:
	if person.lower() in surveyed_keys_lower_list:
		print(f"{person.title()}, thank you for taking the survey!")
	else:
		print(f"{person.title()}, We invite you to participate in a questionnaire.")