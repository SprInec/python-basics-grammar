def city_country(city, country, population=0):
	if population:
		res = f"{city.title()}, {country.title()} - Population {population}"
	else:
		res = f"{city.title()}, {country.title()}"
	return res