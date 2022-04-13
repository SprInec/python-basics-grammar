number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

# 求模运算符（%） 
# 将两数相除并返回余数
if number % 2 == 0:
	print(f"\nThe number {number} is even.")
else:
	print(f"\nThe number {number} is odd.")