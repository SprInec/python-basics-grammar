# -------------------------- 处理ZeroDivisionError异常-----------------------#
# -------------使用 try-except 代码块 ----------- #
try:
	print(5/0)
except ZeroDivisionError:
	print("You can't divide by zero!")

# ------------使用异常避免崩溃------------ #
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		break
	second_number = input("Second number: ")
	if second_number == 'q':
		break
	try:
		answer = int(first_number) / int(second_number)
	except ZeroDivisionError:
		print("You can't divide by zero!")
		break
	print(answer)

# --------------------else代码块---------------------- #
# 依赖 try 代码块成功执行的代码都应放到 else 代码块中
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		break
	second_number = input("Second number: ")
	if second_number == 'q':
		break
	try:
		answer = int(first_number) / int(second_number)
	except ZeroDivisionError:
		print("You can't divide by zero!")
	else:
		print(answer)
