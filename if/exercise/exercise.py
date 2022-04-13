#-----------------------------------1-------------------------------------#
users_name = [] #['alan', 'faker', 'sunshine', 'hulun']

if users_name:
	for user_name in users_name:
		if user_name == 'alan':
			print(f"Hello {user_name.title()}, would you like to see a status report?")
		else:
			print(f"Hello {user_name.title()}, thanks for logging in again.")
else:
	print("We need to find some users!")

#-----------------------------------2--------------------------------------#
current_users = ['amOi', 'Hunb', 'KUA', 'bOp', 'Faker']
new_users = ['amoi', 'kua', 'huhun', 'popi', 'youim']

current_lower_users = []
for current_user in current_users:
	current_lower_users.append(current_user.lower())

for new_user in new_users:
	if new_user.lower() in current_lower_users:
		print("The user name is already in use.")
	else:
		print("The user name is available.")

#-----------------------------------3--------------------------------------#
numbers = list(range(1, 10))

for number in numbers:
	#print(number)
	if number == 1:
		print(f"{number}st")
	elif number == 2:
		print(f"{number}nd")
	elif number == 3:
		print(f"{number}rd")
	else:
		print(f"{number}th")


