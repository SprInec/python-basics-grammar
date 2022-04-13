# 1  """访客"""
filename = 'guest.txt'

user_name = input("Please enter your name: ")
with open(filename, 'w') as file_object:
	file_object.write(user_name.rstrip() + '\n')

# 2  """访客名单"""
filename = 'guest_list.txt'

print("(Enter 'q' to quit.)")
while True:
	user_name = input("Please enter your name: ")
	if user_name == 'q':
		break
	with open(filename, 'a') as file_object:
		file_object.write(user_name.rstrip() + '\n')

# 3  """调查"""
filename = 'survey_result.txt'

print("(Enter 'q' to quit.)")
while True:
	result = input("Could you tell me why you like programming? ")
	if result == 'q':
		break
	with open(filename, 'a') as file_object:
		file_object.write(result.rstrip() + '\n')
