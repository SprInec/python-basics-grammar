#----------------------------------创建数值列表--------------------------------#
#--------------------函数 range() ---------------------#
#效果：从指定的第一个值开始数，并在达到指定的第二个值前停止(不包括指定的第二个值)
for value in range(1, 5):
	print(value)

for value in range(1, 6):
	print(value)

#也可只指定一个参数，这样将从0开始(包括0)
for value in range(10):
	print(value)

#--------------------函数 list()------------------------#
#效果1：将 range() 生成的数组转换为列表
numbers = list(range(1, 6))
print(numbers)

#效果2：可在 range() 第三个参数指定步长，Python讲以步长生成数
#------生成10以内偶数------#
numbers = list(range(2, 11, 2))
print(numbers)

#------将前10个整数的平方加入一个列表中--------#
#法1
squares = []
for value in range(1, 11):
	square = value ** 2
	squares.append(square)
print(squares)
#法2
squares = []
for value in range(1, 11):
	squares.append(value ** 2)
print(squares)

#------------------------对数字列表执行简单的统计计算----------------------------#
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
floats = [1.1, 231.2, 0.222, 33, 10.2, 90]
#------------- min() -------------#
#作用：求数字列表中最小值
min(digits)
res = min(floats)
print(f'res = {res}')
#------------- max() -------------#
#作用：求数字列表中最大值
max(digits)

#------------- sun() -------------#
#作用：求数字列表的总和
sum(digits)

#-----------------------------------列表解析--------------------------------------#
#将 for 循环和创建新元素的代码合并成一行，并自动附加新元素
squares = [value ** 2 for value in range(1, 11)]
print(squares)

#--------------------------------Exercise1------------------------------#
for number in range(1, 21):
	print(number)
#--------------------------------Exercise2------------------------------#
#for number in range(1, 1_000_000):
#	print(number)
#--------------------------------Exercise3------------------------------#
numbers = list(range(1, 1_000_000))
sum_numbers = sum(numbers)
print(sum_numbers)
#--------------------------------Exercise4------------------------------#
numbers = list(range(1, 21, 2))
print(numbers)
#--------------------------------Exercise5------------------------------#
numbers = list(range(3, 31, 3))
for number in numbers:
	print(number)
#--------------------------------Exercise6------------------------------#
numbers = [number ** 3 for number in range(1, 11)]
for number in numbers:
	print(number)
#--------------------------------Exercise7------------------------------#
numbers = []
for value in range(1, 11):
	numbers.append(value ** 3)
print(numbers)