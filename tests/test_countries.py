import json
import unittest

from cinepass.client.v4 import countries
from cinepass.client.v4 import http_client
from tests.utils import mock_session, async_test

SERVER_RESPONSE = {
    "countries": [
        {
            "iso_code": "DE",
            "is_access_granted": True
        },
        {
            "iso_code": "AT",
            "is_access_granted": True
        },
        {
            "iso_code": "CH",
            "is_access_granted": True
        },
        {
            "iso_code": "GB",
            "is_access_granted": True
        },
        {
            "iso_code": "IE",
            "is_access_granted": False
        },
        {
            "iso_code": "US",
            "is_access_granted": False
        },
        {
            "iso_code": "CA",
            "is_access_granted": False
        }
    ]
}


class TestCountries(unittest.TestCase):
    @async_test
    @mock_session(json.dumps(SERVER_RESPONSE))
    async def test_countries(self):
        manager = countries.CountriesManager(http_client.HttpClient("test"))
        self.assertEqual(len(await manager.all()), len(SERVER_RESPONSE['countries']))
        self.assertIn(countries.Country('GB', True), await manager.all(access_granted=True))
