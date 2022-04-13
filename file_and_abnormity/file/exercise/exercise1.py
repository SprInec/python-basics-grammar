# 1
filename = 'python_studay_notes.txt'

with open(filename) as file_object:
	contine = file_object.read()
print(contine.rstrip())

with open(filename) as file_object:
	lines = file_object.readlines()
	for line in lines:
		print(line.strip())

with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.strip())

# 2
"""
 方法 .replace()
 可将字符串中的特定单词都替换为另一个单词
 """
message = 'I really like Python!'
message1 = message.replace('Python', 'C')
print(message1)

with open(filename) as file_object:
	contine = file_object.read()

contine1 = contine.replace('Python', 'C')
print(contine1)
