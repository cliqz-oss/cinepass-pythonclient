# coding: utf-8

import json
import unittest

from cinepass.client.v4 import cities
from cinepass.client.v4 import http_client
from tests.utils import mock_session, async_test

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
    @async_test
    @mock_session(json.dumps(SERVER_RESPONSE))
    async def test_cities(self):
        manager = cities.CityManager(http_client.HttpClient("test"))
        self.assertEqual(len(await manager.get()), len(SERVER_RESPONSE['cities']))
        self.assertIn(
            cities.City(id=4, name='Frankfurt am Main', slug='frankfurt-am-main', lat=50.121212, lon=8.6365638,
                        country='DE'),
            await manager.get())
