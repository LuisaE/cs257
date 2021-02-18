# Claire Williams and Luisa Escosteguy

import unittest
import games_api

class APITester(unittest.TestCase):
    def setUp(self):
        self.games_api = games_api.GamesApi() #change depending on how we code it, will it be a class?

    def tearDown(self):
        pass

    def test_games_endpoint(self):
        url = '/games'
        self.assertIsNotNone(self.games_api.get_games(url))
        #add cases

    def test_platform_endpoint(self):
        url = '/platform'
        self.assertIsNotNone(self.games_api.get_platform(url))

    def test_publisher_endpoint(self):
        url = '/publisher'
        self.assertIsNotNone(self.games_api.get_publisher(url))

    def test_genre_endpoint(self):
        url = '/genre'
        self.assertIsNotNone(self.games_api.get_genre(url))


if __name__ == '__main__':
    unittest.main()