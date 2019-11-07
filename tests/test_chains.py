# coding: utf-8

import json
import unittest

from cinepass.client.v4 import chains
from cinepass.client.v4 import http_client
from tests.utils import mock_session, async_test

SERVER_RESPONSE = {
    "meta_info": {
        "range_from": 0,
        "range_to": 3,
        "total_count": 4
    },
    "chains": [
        {
            "id": "1",
            "name": "CinemaxX",
            "websites": [
                "https://cinemaxx.de",
                "https://cinemaxx.dk"
            ],
            "countries": [
                "DE",
                "DK"
            ]
        },
        {
            "id": "2",
            "name": "CineMotion",
            "websites": [
                "http://www.cinemotion-kino.de/"
            ],
            "countries": [
                "DE"
            ]
        },
        {
            "id": "3",
            "name": "Cineplex",
            "websites": [
                "http://www.cineplex.de"
            ],
            "countries": [
                "DE"
            ]
        },
        {
            "id": "4",
            "name": "CineStar",
            "websites": [
                "http://www.cinestar.de"
            ],
            "countries": [
                "DE"
            ]
        },
        {
            "id": "4",
            "name": "CineStar",
            "websites": [
                "http://www.cinestar.de"
            ],
            "countries": [
                "DE"
            ],
            "new_key": "test"
        }
    ]
}


class TestCinemas(unittest.TestCase):
    @async_test
    @mock_session(json.dumps(SERVER_RESPONSE))
    async def test_cinemas(self):
        manager = chains.ChainManager(http_client.HttpClient("test"))
        response = await manager.all('DE')
        self.assertEqual(len(response), 5)
        self.assertEqual(response[0].id, '1')
