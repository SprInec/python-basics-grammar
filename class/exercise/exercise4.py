# 1  """骰子"""

from random import randint

class Die:
	"""骰子"""

	def __init__(self, sides = 6):
		self.sides = sides

	def roll_die(self):
		print(randint(1, self.sides))

die1 = Die()

die1.roll_die()
die1.roll_die()
die1.roll_die()
die1.roll_die()
die1.roll_die()

die1.roll_die()
die1.roll_die()
die1.roll_die()
die1.roll_die()
die1.roll_die()

die2 = Die(10)
die3 = Die(20)

die2.roll_die()
die2.roll_die()
die2.roll_die()
die2.roll_die()
die2.roll_die()

die3.roll_die()
die3.roll_die()
die3.roll_die()
die3.roll_die()
die3.roll_die()


# 2   """彩票"""

from random import choice

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
char = ['a', 'b', 'c', 'd']

print("If your str is following, you hit the jackpot!")
print(f"{choice(number)} {choice(char)} {choice(number)} {choice(char)}")

# 3   """彩票分析"""
the_jackpot = "6 a 6 a"
my_ticket = ""
times = 0

while my_ticket != the_jackpot:
	times += 1
	my_ticket = f"{choice(number)} {choice(char)} {choice(number)} {choice(char)}"

print(times)