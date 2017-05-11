import unittest
import mock

from cinepass.client.v4 import countries

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
    def test_countries(self):
        http_mock = mock.MagicMock()
        http_mock.get.return_value = SERVER_RESPONSE
        manager = countries.CountriesManager(http_mock)
        self.assertEqual(len(manager.all()), len(SERVER_RESPONSE['countries']))
        self.assertIn(countries.Country('GB', True), manager.all(access_granted=True))
