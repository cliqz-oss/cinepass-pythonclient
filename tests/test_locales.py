import unittest
import mock

from cinepass.client.v4 import locales

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
    def test_locales(self):
        http_mock = mock.MagicMock()
        http_mock.get.return_value = SERVER_RESPONSE
        manager = locales.LocalesManager(http_mock)
        self.assertEqual(len(manager.all()), len(SERVER_RESPONSE['locales']))
        self.assertIn('de', manager.all())
