#----------------------------分析文本------------------------------#
# 方法 .split()
# 能根据一个字符串创建一个单词列表
title = "Alice in Wonderland"
res = title.split()
print(res)

filename = 'alice.txt'

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