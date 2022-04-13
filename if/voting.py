age = 19
if age > 18:
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")

# ------------ if else --------------#
age = 17
if age >= 18:
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")
else:
	print("Sorry, you are too young to vote.")
	print("Please register to vote as soon as you turn 18.")

#----------- if elif else -----------# 
age = 12
if age < 4:
	print("Your admission cost is $0.")
elif age < 18:
	print("Your admission cost is $25.")
else:
	print("Your admission cost is $40.")

if age < 4:
	price = 0
elif age < 18:
	price = 25
else:
	price = 40
print(f"Your admission cost is ${price}.")

#-----------使用多个 elif ------------#
if age < 4:
	price = 0;
elif age < 18:
	price = 25
elif age > 65:
	price = 40 * 0.6
else:
	price = 40
print(f"Your admission cost is ${price}.")

#------------省略 else ---------------#
if age < 4:
	price = 0;
elif age < 18:
	price = 25
elif age < 60:
	price = 40
elif age >= 60:
	price = 20

#------------------------------测试多个条件-----------------------------#
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
	print("Adding mushrooms")
if 'pepperoni' in requested_toppings:
	print("Adding pepperoni")
if 'extra cheese' in requested_toppings:
	print("Adding extra cheese")

print("\nFinished making your pizza.")

#---------------------------------Exercise------------------------------------#
#---------- The color of Alien ---------#
alien_colors = ['green', 'yellow', 'red']
alien_color = alien_colors[0]

if alien_color == 'green':
	print("You have got 5 points.")

print('\n')
if alien_color == 'green':
	print("You have got 5 points.")
else:
	print("You have got 10 points.")

print('\n')
if alien_color == 'green':
	print("You have got 5 points.")
elif alien_color == 'yellow':
	print("You have got 10 points.")
elif alien_color == 'red':
	print("You have got 15 points.")

#----------The different stage of life --------#
age = 10

if age < 2:
	print("You are baby.")
elif age >= 2 and age < 4:
	print("You are toddler.")
elif age >= 4 and age < 13:
	print("You are child.")
elif age >= 13 and age < 20:
	print("You are teenager.")
elif age >= 20 and age < 65:
	print("You are adult.")
elif age >= 65:
	print("You are old man.")

#------------the favorite fruit------------#
favorite_fruit = ['apple', 'banana', 'bear', 'pear', 'strawberry']

if 'apple' in favorite_fruit:
	print("You really like apple!")
if 'banana' in favorite_fruit:
	print("You really like banana!")