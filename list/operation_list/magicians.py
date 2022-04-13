
#--------------------for语句的初步使用---------------------#
magicians = ['alice', 'david', 'carolian']
for magician in magicians:
	#for语句后的冒号告诉Python下一行是循环的第一行#
	print(magician)
	#此用法会对列表所有元素执行相同操作#
	print(f"{magician.title()}, that was a great trick!")
	print(f"I can't weet to see your next trick, {magician.title()}.\n")
	#循环时会执行完一轮所有代码后在进行下一轮循环#
	#for循环只会循环其下缩进的代码#
print("Thank you, everyone. That was a great magic show!")

#---------------------Exercise pizza------------------------#
pizzas = ['Yishi pizza', 'Fashi pizza', 'Meishi pizza']
for pizza in pizzas:
	print(f"I like {pizza.title()}.")
print(f"I really love pizza!")

#---------------------Exercise animals----------------------#
animals = ['dog', 'cat', 'elephant', 'lion', 'tiger', 'cheetah', 'deer']
for animal in animals:
	print(animal)
	print(f"In any case, I think {animal} is cute.")
print("\nI think these animals are cute.")

