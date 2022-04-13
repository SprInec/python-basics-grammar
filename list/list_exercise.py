#------------------------------------------------设宴请客------------------------------------------------------#

Participants_List = ['Li Lei', 'Wang Ming', 'Ge Zhu']
print(f"Dear {Participants_List[0]}, I would like to invite you to dinner at Hexing Building on July 7th at 3 PM.")
print(f"Dear {Participants_List[1]}, I would like to invite you to dinner at Hexing Building on July 7th at 3 PM.")
print(f"Dear {Participants_List[2]}, I would like to invite you to dinner at Hexing Building on July 7th at 3 PM.")
print('\n')

print(f"I am very sorry that {Participants_List[1]} is unable to attend for some reason.")
Participants_List[1] = 'Kai Ran'
print(f"Dear {Participants_List[0]}, I would like to invite you to dinner at Hexing Building on July 7th at 3 PM.")
print(f"Dear {Participants_List[1]}, I would like to invite you to dinner at Hexing Building on July 7th at 3 PM.")
print(f"Dear {Participants_List[2]}, I would like to invite you to dinner at Hexing Building on July 7th at 3 PM.")


print('\n')
print("Dear friends, I have found a bigger table, and we have three new friends for dinner!")

Participants_List.insert(0, 'Yang Guangming')
Participants_List.insert(3, 'Huang Wan')
Participants_List.append('Tang Tang')
print(f"Dear {Participants_List[0]}, I would like to invite you to dinner at Hexing Building on July 7th at 3 PM.")
print(f"Dear {Participants_List[1]}, I would like to invite you to dinner at Hexing Building on July 7th at 3 PM.")
print(f"Dear {Participants_List[2]}, I would like to invite you to dinner at Hexing Building on July 7th at 3 PM.")
print(f"Dear {Participants_List[3]}, I would like to invite you to dinner at Hexing Building on July 7th at 3 PM.")
print(f"Dear {Participants_List[4]}, I would like to invite you to dinner at Hexing Building on July 7th at 3 PM.")
print(f"Dear {Participants_List[5]}, I would like to invite you to dinner at Hexing Building on July 7th at 3 PM.")

print('\n')
print("Dear friends, I'm sorry, but as the newly purchased table will not arrive in time, only two people can be invited to dinner.")

person = Participants_List.pop(-1)
print(f"I'm sorry {person.title()}, the dinner's been canceled")
person = Participants_List.pop(-2)
print(f"I'm sorry {person.title()}, the dinner's been canceled")
person = Participants_List.pop(0)
print(f"I'm sorry {person.title()}, the dinner's been canceled")
person = Participants_List.pop(1)
print(f"I'm sorry {person.title()}, the dinner's been canceled")

print(f"Dear {Participants_List[0]}, I would like to invite you to dinner at Hexing Building on July 7th at 3 PM.")
print(f"Dear {Participants_List[1]}, I would like to invite you to dinner at Hexing Building on July 7th at 3 PM.")

del Participants_List[1]
del Participants_List[0]

print(Participants_List)


