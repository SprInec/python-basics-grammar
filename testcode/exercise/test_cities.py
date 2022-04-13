import unittest
from city_function import city_country

class CityTestCase(unittest.TestCase):

	def test_city_country(self):
		res = city_country('shanghai', 'china')
		self.assertEqual(res, 'Shanghai, China')

	def test_city_country_population(self):
		res = city_country('shanghai', 'china', 5_000_000_000)
		self.assertEqual(res, 'Shanghai, China - Population 5000000000')


if __name__ == '__main__':
	unittest.main()