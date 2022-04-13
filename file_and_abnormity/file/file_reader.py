# ------------------------------读取整个文件----------------------------#
# open() 打开文件
# close() 关闭文件
# with open(): 不需要手动 close() 关闭文件,Python会自动识别程序结束并关闭文件
# .read() 读取文件的全部内容，并将其作为一个长长的字符赋给所需变量，且在到达
#         文件末尾时返回一个空字符串，可在print()中使用rstrip()删除

with open('pi_digits.txt') as file_object:
	contents = file_object.read()
print(contents.rstrip())

# --------------------------------文件路径------------------------------- #
# 使用 / 斜杠
# 如果一定要使用 \ 反斜杠，必须对反斜杠进行转义 \\ 才可使用

"""相对路径"""
with open('text_files/filename.txt') as file_object:

"""绝对路径"""
# 绝对路径通常比相对路径长，因此将其赋给一个变量，再将变量传递给open()更简洁
file_open = '/home/ehmatthes/other_files/text_files/filename.txt'
with open(file_open) as file_object:

# ------------------------------- 逐行读取 ------------------------------- #
# 要以每次一行的方式检查文件，可对文件对象使用 for 循环:
filename = 'pi_digits.txt'

with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())

# --------------------- 创建一个包含文件各行内容的列表 -------------------- #
filename = 'pi_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())

# ----------------------------- 使用文件的内容 ----------------------------- #
filename = 'pi_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	# pi_string += line.rstrip()
	pi_string += line.strip()

print(pi_string)
print(len(pi_string))

# -------------------------- 包含一百万位的大型文件 ------------------------- #
# 和前面操作一样
# 对于可处理的数据量，Python没有任何限制。只要系统的内存足够多，
# 想处理多少数据都可以
filename = 'pi_million_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))

# ---------------------- 圆周率值中包含你的生日吗 --------------------------- #
filename = 'pi_million_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))

birthday = input("Enter your birthday, in the form mmddy: ")
if birthday in pi_string:
	print("Your birthday appears in the first million digits of pi!")
else:
	print("Your birthday does not appear in the first million digits of pi.")
	
