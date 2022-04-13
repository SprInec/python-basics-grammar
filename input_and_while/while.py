# ----------------------------while 循环-----------------------------#
# 区别于 for 循环针对集合中每个元素都执行一个代码块
# while 循环则不断运行，直到指定的条件不满足为止
current_number = 1
while current_number <= 5:
	print(current_number)
	current_number += 1
	#current_number += 1 为 current_number = current_number + 1 的简写

# ------------- 如何退出 --------------#
# parrot.py
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program."
message = ""

while message != 'quit':
	message = input(prompt)
	if message != 'quit':
		print(message)

# -------------- 使用标志 ---------------#
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program."
message = ""

active = True
while active:
	message = input(prompt)

	if message == 'quit':
		active = False
	else:
		print(message)

# -------------- 使用brake退出循环 --------------- #
# break 用于退出循环
prompt = "\nPlease enter the name of a city you have visited."
prompt += "\n(Enter 'quit' when you are finished.): "

while True:
	city = input(prompt)

	if city == 'quit':
		break
	else:
		print(f"I'd love to go to {city.title()}!")

# ------------- 在循环中使用continue ---------------#
# 跳过该次循环直接进入下一次循环
# counting.py
current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue

	print(current_number)
