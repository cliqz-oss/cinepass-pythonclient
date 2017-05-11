# coding: utf-8

import unittest
import mock

from cinepass.client.v4 import cities

SERVER_RESPONSE = {
    "cities": [
        {
            "id": "1",
            "name": "Berlin",
            "slug": "berlin",
            "lat": 52.50735,
            "lon": 13.42855,
            "country": "DE"
        },
        {
            "id": "2",
            "name": "Köln",
            "slug": "koeln",
            "lat": 50.92695,
            "lon": 7.00021,
            "country": "DE"
        },
        {
            "id": "3",
            "name": "Hamburg",
            "slug": "hamburg",
            "lat": 53.5543,
            "lon": 10.0454,
            "country": "DE"
        },
        {
            "id": "4",
            "name": "Frankfurt am Main",
            "slug": "frankfurt-am-main",
            "lat": 50.121212,
            "lon": 8.6365638,
            "country": "DE"
        }
    ]
}


class TestCities(unittest.TestCase):
    def test_cities(self):
        http_mock = mock.MagicMock()
        http_mock.get.return_value = SERVER_RESPONSE
        manager = cities.CityManager(http_mock)
        self.assertEqual(len(manager.get()), len(SERVER_RESPONSE['cities']))
        self.assertIn(
            cities.City(id=4, name='Frankfurt am Main', slug='frankfurt-am-main', lat=50.121212, lon=8.6365638,
                        country='DE'),
            manager.get())
