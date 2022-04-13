name = 'July '
strlen = 'is nice'
print(f"{name}{strlen}")
print(f"{name.rstrip()}{strlen}")

name = name.rstrip()
print(name)

name = ' July'
name = name.lstrip()

name = ' july '
name = name.strip().title()
print(name)
