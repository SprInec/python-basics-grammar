# ---------------------------使用多个文件---------------------------#
def count_words(filename):
	"""计算一个文件大概包含多少个单词"""
	try:
		with open(filename, encoding='utf-8') as f:
			contents = f.read()
	except FileNotFoundError:
		print(f"Sorry, the file {filename} does not exist.")
	else:
		# 计算该文件大致包含多少单词
		words = contents.split()
		num_words = len(words)
		print(f"The file {filename} has about {num_words} words.")

filename = 'alice.txt'
count_words(filename)

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
	count_words(filename)

# --------------------------------静默失败-------------------------------#
# 语句 pass
# 可让Python在代码块中什么都不要做
def count_words(filename):
	"""计算一个文件大概包含多少个单词"""
	try:
		with open(filename, encoding='utf-8') as f:
			contents = f.read()
	except FileNotFoundError:
		pass
	else:
		# 计算该文件大致包含多少单词
		words = contents.split()
		num_words = len(words)
		print(f"The file {filename} has about {num_words} words.")

filename = 'alice.txt'
count_words(filename)

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
	count_words(filename)

