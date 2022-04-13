# ------------------- int() ----------------- #
# 让python将输入视为数值(将元素转化为整数格式)
age = input("How old are you? ")
age = int(age)
if age >= 18:
	print("OK!")

# rollercoaster.py
height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
	print("You're tall enough to ride!")
else:
	print("\nYou'll be able to ride when you're a little older.")
