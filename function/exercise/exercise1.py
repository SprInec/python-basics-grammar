# 1
def make_shirt(size, style):
	print(f"The size of T-shirt is {size}.")
	print(f"And the style of it is {style}.")

make_shirt('xl', 'Young')
make_shirt(style = 'Blue Bob', size = 'l')

# 2
def make_shirt(size = 'big', style = 'I love Python'):
	print(f"The size of T-shirt is {size}.")
	print(f"And the style of it is {style}.")

make_shirt(size = 'midum')
make_shirt(style = 'Ha ha')
make_shirt('small', 'Guanss ss sss')