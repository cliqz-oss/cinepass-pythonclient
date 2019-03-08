import json
import unittest

from cinepass.client.v4 import http_client
from cinepass.client.v4 import locales
from tests.utils import mock_session, async_test

SERVER_RESPONSE = {
    "locales": [
        "de",
        "de-CH",
        "en",
        "fr",
        "fr-CH",
        "es",
        "nl",
        "it",
        "da",
        "sv",
        "fi",
        "ru"
    ]
}


class TestLocales(unittest.TestCase):
    @async_test
    @mock_session(json.dumps(SERVER_RESPONSE))
    async def test_locales(self):
        manager = locales.LocalesManager(http_client.HttpClient("test"))
        self.assertEqual(len(await manager.all()), len(SERVER_RESPONSE['locales']))
        self.assertIn('de', await manager.all())
