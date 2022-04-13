# 1 """加法计算器"""
print("Enter two number and I'll tell your their sum.")
print("Enter 'q' to quit.")

while True:	
	number1 = input("Please enter the first number: ")
	if number1 == 'q':
		break
	number2 = input("Please enter the second number: ")
	if number2 == 'q':
		break

	try:
		sum = int(number1) + int(number2)
	except ValueError:
		print("Please enter number.")
	else:
		print(sum)

# 2 """猫和狗"""
filename1 = 'cats.txt'
filename2 = 'dogs.txt'

def catanddog(filename):

	try:
		with open(filename) as f:
			contens = f.read()
	except FileNotFoundError:
		print("The file is not exit.")
	else:
		print(contens)

catanddog(filename1)
catanddog(filename2)

# 3 """静默的猫和狗"""
def catanddog(filename):

	try:
		with open(filename) as f:
			contens = f.read()
	except FileNotFoundError:
		pass
	else:
		print(contens)

# 4 """常见单词"""
# 方法 count()  可用来确定特定单词或短语在字符串中出现了多少次
line = "Row, row, row, row, row your boat."
line.count('row')
line.lower().count('row')