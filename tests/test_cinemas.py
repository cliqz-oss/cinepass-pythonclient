# coding: utf-8

import unittest
import mock

from cinepass.client.v4 import cinemas

SERVER_RESPONSE = {
    "cinema": {
        "booking_type": None,
        "chain_id": "6",
        "id": "50",
        "location": {
            "address": {
                "city": "Darmstadt",
                "country": "Germany",
                "country_code": "DE",
                "display_text": "Luisenstra\u00dfe 10, 64283, ",
                "house": "10",
                "state": None,
                "state_abbr": None,
                "street": "Luisenstra\u00dfe",
                "zipcode": "64283"
            },
            "lat": 49.8734,
            "lon": 8.65141
        },
        "name": "Citydome - Pali Kino",
        "slug": "pali-kino-darmstadt",
        "telephone": "0 61 51/2 97 89",
        "website": "http://www.helia-kinos.de"
    }
}


class TestCinemas(unittest.TestCase):
    def test_cinemas(self):
        http_mock = mock.MagicMock()
        http_mock.get.return_value = SERVER_RESPONSE
        manager = cinemas.CinemasManager(http_mock)
        cinema = manager.get(101)
        self.assertEqual(cinema.location.address.street, "Luisenstra\u00dfe")
