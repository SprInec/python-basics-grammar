# 1
sandwich_orders = ['yishi sandwich', 'fashi sandwich', 'meishi sandwich']
finished_sandwichs = []

while sandwich_orders:	
	finished_sandwich = sandwich_orders.pop()
	print(f"I made your {finished_sandwich}.")
	finished_sandwichs.append(finished_sandwich)

print("All of your sandwich have been made.")
print(sorted(finished_sandwichs, reverse = True))

# 2
sandwich_orders = ['pastrami sandwich', 'yishi sandwich', 'pastrami sandwich',
	 'fashi sandwich', 'meishi sandwich', 'pastrami sandwich']

print("The pastrami sandwich has been sold out.")
while 'pastrami sandwich' in sandwich_orders:
	sandwich_orders.remove('pastrami sandwich')

print(sandwich_orders)

# 3
question1 = "\nWhat's your name? "
question2 = "\nIf you could visit one place in the world, where would you go? "

goon_active = True

while goon_active:
	name = input(question1)
	place = input(question2)
	goon_active_flag = input("if you want to go on? (yes/no) ")

	if goon_active_flag == 'no':
		goon_active = False

print(f"Hello {name.title()}, thank you.")



