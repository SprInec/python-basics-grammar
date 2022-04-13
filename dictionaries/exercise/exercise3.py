# 1
Alan = {
	'first': 'pin',
	'last': 'huaxi',
	'location': 'paris',
	}
Alice = {
	'first': 'xxi',
	'lst': 'swsx',
	'location': 'london',
	}
Caesar = {
	'first': 'hubu',
	'last': 'buxh',
	'location': 'New York',
	}

people = [Alan, Alice, Caesar]

for person in people:
	print(person)

# 2
favorite_please = {
	'alan': ['paris', 'beijing', 'yuncheng'],
	'alice': ['london', 'tianjin', 'new york'],
	'caesar': ['new york', 'tokyo', 'shanghai'],
	}

for name, place_info in favorite_please.items():
	print(name.title() + ':')
	for place in place_info:
		print('\t' + place.title())

# 3
cities = {
	'beijing': {
		'population': 3_000_000_000,
		'country': 'china',
		'fact': 'xxxxx',
		},

	'shanghai': {
		'population': 4_000_000_000,
		'country': 'china',
		'fact': 'hhhhhhh'
		},

	'new york': {
		'population': 1_000_000_000,
		'country': 'america',
		'fact': 'gggggggg',
		},
	}

for city, information_info in cities.items():
	print(f"{city.title()}:")
	for information, count in information_info.items():
		print(f"\t{information.title()}:")
		print(f"\t\t{count}")

