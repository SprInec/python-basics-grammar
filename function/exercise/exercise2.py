# 1
def city_country(city_name, belong_country):
	print(f"{city_name.title()}, {belong_country.title()}")

city_country('santiago', 'chile')
city_country('shanghai', 'china')
city_country('new york', 'amercia')

# 2
def make_album(singer_name, album_name, number = None):
	album = {'name': singer_name.title(), 'album_name': album_name.title()}
	if number:
		album['number'] = number
	return album

album1 = make_album('jouji', 'huahua')
album2 = make_album('zhizhuang', 'lila', 23)
print(album1)
print(album2)

# 3
while True:
	print("(Enter 'q' for any time to quit.)")
	name = input("\nWho is your favorite singer? ")
	if name == 'q':
		break
	album = input("A name of his/her album you best like? ")
	if album == 'q':
		break
		
	final_album = make_album(name, album)
	print(final_album)
