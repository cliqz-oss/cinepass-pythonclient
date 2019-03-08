import json
import unittest

from cinepass.client.v4 import http_client
from cinepass.client.v4 import movies
from tests.utils import mock_session, async_test

SERVER_RESPONSE = {
    "movie": {
        "age_limits": {
            "DE": 6,
            "FR": "U",
            "GB": "PG",
            "IE": "G",
            "NL": "6",
            "RU": "6+",
            "US": "PG"
        },
        "cast": [
            {
                "character": "Boss Baaby (voice)",
                "id": "cad24260b95747d647525a4d9fca089e",
                "name": "Alec Baldwin"
            },
            {
                "character": "Tim Templeton (voice)",
                "id": "52fd0178ede8ffaa1e9eda59d77f7035",
                "name": "Miles Bakshi"
            },
            {
                "character": "Ted Templeton (voice)",
                "id": "267fdad22bf8011076b3b54144e6c5e7",
                "name": "Jimmy Kimmel"
            },
            {
                "character": "Janice Templeton (voice)",
                "id": "d3069cc90b4e0aff42e90d1eac1995e5",
                "name": "Lisa Kudrow"
            },
            {
                "character": "Francis E. Francis (voice)",
                "id": "e1e319af3a73e91d9345a9320130fb52",
                "name": "Steve Buscemi"
            },
            {
                "character": "Eugene Francis",
                "id": "2671396daf7adb6fcbf12ca5d0d3c793",
                "name": "Conrad Vernon"
            },
            {
                "character": "Narrator (voice)",
                "id": "9646d50a04931cd1356d504de79e4bdc",
                "name": "Tobey Maguire"
            },
            {
                "character": "Staci (voice)",
                "id": "ffa25fbb5efb388fe0b6b8d6466e8f82",
                "name": "ViviAnn Yee"
            },
            {
                "character": "Triplets (voice)",
                "id": "939f71f21d901d7e9ada0288c03635bb",
                "name": "Eric Bell Jr."
            },
            {
                "character": "Hazmat Baby (voice)",
                "id": "05ba96784b449f20a0d40be20d32fc57",
                "name": "Chloe Albrecht"
            },
            {
                "character": "Flight Attendant (voice) (as Andrea Knoll)",
                "id": "64ba76735b0a93caabe55fd9bd92f083",
                "name": "Andrea Montana Knoll"
            },
            {
                "character": "Captain Ross (voice)",
                "id": "d8d9a12bb2bbb2d4bafe45c1cd0fea0d",
                "name": "Chris Miller"
            },
            {
                "character": "Elvis Impersonators (voice)",
                "id": "8f5320b1b9f8849a709b3229567add0c",
                "name": "Joseph Izzo"
            },
            {
                "character": "Airport Announcer (voice)",
                "id": "e82ed22508894f309becce7bba2117d7",
                "name": "Glenn Harmon"
            },
            {
                "character": "Airport Security Guard (voice)",
                "id": "d325ca28e9070065617caddcd4ac4800",
                "name": "Brian Hopkins"
            },
            {
                "character": "TV Chef (voice)",
                "id": "4959b155eb419f7a7c252bd80c27ba54",
                "name": "Tom McGrath"
            },
            {
                "character": "Tim's Daughter / Girl / Little Girl (voice) (as Nina Bakshi)",
                "id": "b154b936b3c94d2fd0501d71a918e0f3",
                "name": "Nina Zoe Bakshi"
            },
            {
                "character": "Crying Boy / Little Boy / Boy (voice)",
                "id": "2d0872659be42dbeffbc232389814ba4",
                "name": "Jules Winter"
            },
            {
                "character": "Photographer (voice)",
                "id": "395f45d3b3ac3ecbc0dfe2e11a4b8e5e",
                "name": "Walt Dohrn"
            },
            {
                "character": "Story Bear (voice)",
                "id": "cd7c39dfc3858a12c256f0a42464bb71",
                "name": "James Ryan"
            },
            {
                "character": "Big Boss Baby (voice)",
                "id": "4ee747dd301efa0df74c0c66e59975a3",
                "name": "Edie Mirman"
            },
            {
                "character": "Jimbo (voice)",
                "id": "f11df07ac9d97525e34e1390630a69d0",
                "name": "David Soren"
            },
            {
                "character": "Wizzie / Elvis Impersonator (voice)",
                "id": "09bb52d70bf129e152a0fbbb3fa47159",
                "name": "James McGrath"
            }
        ],
        "crew": [
            {
                "id": "408bac4d1d2188b0f6d6b52c83c1343b",
                "job": "writer",
                "name": "Marla Frazee"
            },
            {
                "id": "4959b155eb419f7a7c252bd80c27ba54",
                "job": "director",
                "name": "Tom McGrath"
            }
        ],
        "genres": [
            {
                "id": "2",
                "name": "Animation"
            },
            {
                "id": "3",
                "name": "Comedy"
            },
            {
                "id": "7",
                "name": "Family"
            }
        ],
        "id": "12163",
        "imdb_id": "tt3874544",
        "keywords": None,
        "original_language": "en",
        "original_title": "The Boss Baby",
        "poster_image": {
            "image_files": [
                {
                    "size": {
                        "height": 138,
                        "width": 92
                    },
                    "url": "http://image.tmdb.org/t/p/w92/pQC2N8eaO3haCZ887nxdFtaY4AM.jpg"
                },
                {
                    "size": {
                        "height": 231,
                        "width": 154
                    },
                    "url": "http://image.tmdb.org/t/p/w154/pQC2N8eaO3haCZ887nxdFtaY4AM.jpg"
                },
                {
                    "size": {
                        "height": 277,
                        "width": 185
                    },
                    "url": "http://image.tmdb.org/t/p/w185/pQC2N8eaO3haCZ887nxdFtaY4AM.jpg"
                },
                {
                    "size": {
                        "height": 513,
                        "width": 342
                    },
                    "url": "http://image.tmdb.org/t/p/w342/pQC2N8eaO3haCZ887nxdFtaY4AM.jpg"
                },
                {
                    "size": {
                        "height": 750,
                        "width": 500
                    },
                    "url": "http://image.tmdb.org/t/p/w500/pQC2N8eaO3haCZ887nxdFtaY4AM.jpg"
                },
                {
                    "size": {
                        "height": 1170,
                        "width": 780
                    },
                    "url": "http://image.tmdb.org/t/p/w780/pQC2N8eaO3haCZ887nxdFtaY4AM.jpg"
                },
                {
                    "size": {
                        "height": 2880,
                        "width": 1920
                    },
                    "url": "http://image.tmdb.org/t/p/original/pQC2N8eaO3haCZ887nxdFtaY4AM.jpg"
                }
            ]
        },
        "poster_image_thumbnail": "http://image.tmdb.org/t/p/w154/pQC2N8eaO3haCZ887nxdFtaY4AM.jpg",
        "production_companies": None,
        "ratings": {
            "imdb": {
                "value": 6.5,
                "vote_count": 10901
            },
            "tmdb": {
                "value": 5.6,
                "vote_count": 817
            }
        },
        "release_dates": {
            "BR": [
                {
                    "date": "2017-03-30",
                    "locale": "pt-BR",
                    "region": None
                }
            ],
            "DE": [
                {
                    "date": "2017-03-30",
                    "locale": "de-DE",
                    "region": None
                }
            ],
            "ES": [
                {
                    "date": "2017-04-14",
                    "locale": "es-ES",
                    "region": None
                }
            ],
            "FR": [
                {
                    "date": "2017-03-29",
                    "locale": "fr-FR",
                    "region": None
                }
            ],
            "GB": [
                {
                    "date": "2017-04-01",
                    "locale": "en-GB",
                    "region": None
                }
            ],
            "IE": [
                {
                    "date": "2017-04-01",
                    "locale": "en-IE",
                    "region": None
                }
            ],
            "IN": [
                {
                    "date": "2017-03-31",
                    "locale": "hi-IN",
                    "region": None
                }
            ],
            "IT": [
                {
                    "date": "2017-04-20",
                    "locale": "it-IT",
                    "region": None
                }
            ],
            "NL": [
                {
                    "date": "2017-04-19",
                    "locale": "nl-NL",
                    "region": None
                }
            ],
            "RU": [
                {
                    "date": "2017-03-23",
                    "locale": "ru-RU",
                    "region": None
                }
            ],
            "UA": [
                {
                    "date": "2017-03-23",
                    "locale": "uk-UA",
                    "region": None
                }
            ],
            "US": [
                {
                    "date": "2017-03-31",
                    "locale": "en-US",
                    "region": None
                }
            ]
        },
        "rentrak_film_id": 75634,
        "runtime": 97,
        "scene_images": [
            {
                "image_files": [
                    {
                        "size": {
                            "height": 169,
                            "width": 300
                        },
                        "url": "http://image.tmdb.org/t/p/w300/bTFeSwh07oX99ofpDI4O2WkiFJ.jpg"
                    },
                    {
                        "size": {
                            "height": 439,
                            "width": 780
                        },
                        "url": "http://image.tmdb.org/t/p/w780/bTFeSwh07oX99ofpDI4O2WkiFJ.jpg"
                    },
                    {
                        "size": {
                            "height": 562,
                            "width": 1000
                        },
                        "url": "http://image.tmdb.org/t/p/w1000/bTFeSwh07oX99ofpDI4O2WkiFJ.jpg"
                    },
                    {
                        "size": {
                            "height": 720,
                            "width": 1280
                        },
                        "url": "http://image.tmdb.org/t/p/w1280/bTFeSwh07oX99ofpDI4O2WkiFJ.jpg"
                    },
                    {
                        "size": {
                            "height": 1080,
                            "width": 1920
                        },
                        "url": "http://image.tmdb.org/t/p/w1920/bTFeSwh07oX99ofpDI4O2WkiFJ.jpg"
                    },
                    {
                        "size": {
                            "height": 2160,
                            "width": 3840
                        },
                        "url": "http://image.tmdb.org/t/p/original/bTFeSwh07oX99ofpDI4O2WkiFJ.jpg"
                    }
                ]
            },
            {
                "image_files": [
                    {
                        "size": {
                            "height": 169,
                            "width": 300
                        },
                        "url": "http://image.tmdb.org/t/p/w300/8keMlLuzB9XIUBnbdEq5DCqZdHQ.jpg"
                    },
                    {
                        "size": {
                            "height": 439,
                            "width": 780
                        },
                        "url": "http://image.tmdb.org/t/p/w780/8keMlLuzB9XIUBnbdEq5DCqZdHQ.jpg"
                    },
                    {
                        "size": {
                            "height": 563,
                            "width": 1000
                        },
                        "url": "http://image.tmdb.org/t/p/w1000/8keMlLuzB9XIUBnbdEq5DCqZdHQ.jpg"
                    },
                    {
                        "size": {
                            "height": 720,
                            "width": 1280
                        },
                        "url": "http://image.tmdb.org/t/p/w1280/8keMlLuzB9XIUBnbdEq5DCqZdHQ.jpg"
                    },
                    {
                        "size": {
                            "height": 1080,
                            "width": 1920
                        },
                        "url": "http://image.tmdb.org/t/p/w1920/8keMlLuzB9XIUBnbdEq5DCqZdHQ.jpg"
                    },
                    {
                        "size": {
                            "height": 1866,
                            "width": 3317
                        },
                        "url": "http://image.tmdb.org/t/p/original/8keMlLuzB9XIUBnbdEq5DCqZdHQ.jpg"
                    }
                ]
            },
            {
                "image_files": [
                    {
                        "size": {
                            "height": 169,
                            "width": 300
                        },
                        "url": "http://image.tmdb.org/t/p/w300/frlfy7RFqx5J4jrcMo25PqyasL3.jpg"
                    },
                    {
                        "size": {
                            "height": 439,
                            "width": 780
                        },
                        "url": "http://image.tmdb.org/t/p/w780/frlfy7RFqx5J4jrcMo25PqyasL3.jpg"
                    },
                    {
                        "size": {
                            "height": 563,
                            "width": 1000
                        },
                        "url": "http://image.tmdb.org/t/p/w1000/frlfy7RFqx5J4jrcMo25PqyasL3.jpg"
                    },
                    {
                        "size": {
                            "height": 720,
                            "width": 1280
                        },
                        "url": "http://image.tmdb.org/t/p/w1280/frlfy7RFqx5J4jrcMo25PqyasL3.jpg"
                    },
                    {
                        "size": {
                            "height": 1080,
                            "width": 1920
                        },
                        "url": "http://image.tmdb.org/t/p/w1920/frlfy7RFqx5J4jrcMo25PqyasL3.jpg"
                    },
                    {
                        "size": {
                            "height": 2010,
                            "width": 3573
                        },
                        "url": "http://image.tmdb.org/t/p/original/frlfy7RFqx5J4jrcMo25PqyasL3.jpg"
                    }
                ]
            },
            {
                "image_files": [
                    {
                        "size": {
                            "height": 169,
                            "width": 300
                        },
                        "url": "http://image.tmdb.org/t/p/w300/5izAuyw3Pjb3Axms7rTTRxe8rsC.jpg"
                    },
                    {
                        "size": {
                            "height": 439,
                            "width": 780
                        },
                        "url": "http://image.tmdb.org/t/p/w780/5izAuyw3Pjb3Axms7rTTRxe8rsC.jpg"
                    },
                    {
                        "size": {
                            "height": 562,
                            "width": 1000
                        },
                        "url": "http://image.tmdb.org/t/p/w1000/5izAuyw3Pjb3Axms7rTTRxe8rsC.jpg"
                    },
                    {
                        "size": {
                            "height": 720,
                            "width": 1280
                        },
                        "url": "http://image.tmdb.org/t/p/w1280/5izAuyw3Pjb3Axms7rTTRxe8rsC.jpg"
                    },
                    {
                        "size": {
                            "height": 1080,
                            "width": 1920
                        },
                        "url": "http://image.tmdb.org/t/p/w1920/5izAuyw3Pjb3Axms7rTTRxe8rsC.jpg"
                    },
                    {
                        "size": {
                            "height": 1632,
                            "width": 2902
                        },
                        "url": "http://image.tmdb.org/t/p/original/5izAuyw3Pjb3Axms7rTTRxe8rsC.jpg"
                    }
                ]
            },
            {
                "image_files": [
                    {
                        "size": {
                            "height": 169,
                            "width": 300
                        },
                        "url": "http://image.tmdb.org/t/p/w300/4IrZC1uuaDpGScO4TDyEe4E4bq2.jpg"
                    },
                    {
                        "size": {
                            "height": 439,
                            "width": 780
                        },
                        "url": "http://image.tmdb.org/t/p/w780/4IrZC1uuaDpGScO4TDyEe4E4bq2.jpg"
                    },
                    {
                        "size": {
                            "height": 563,
                            "width": 1000
                        },
                        "url": "http://image.tmdb.org/t/p/w1000/4IrZC1uuaDpGScO4TDyEe4E4bq2.jpg"
                    },
                    {
                        "size": {
                            "height": 720,
                            "width": 1280
                        },
                        "url": "http://image.tmdb.org/t/p/w1280/4IrZC1uuaDpGScO4TDyEe4E4bq2.jpg"
                    },
                    {
                        "size": {
                            "height": 1080,
                            "width": 1920
                        },
                        "url": "http://image.tmdb.org/t/p/w1920/4IrZC1uuaDpGScO4TDyEe4E4bq2.jpg"
                    },
                    {
                        "size": {
                            "height": 816,
                            "width": 1450
                        },
                        "url": "http://image.tmdb.org/t/p/original/4IrZC1uuaDpGScO4TDyEe4E4bq2.jpg"
                    }
                ]
            },
            {
                "image_files": [
                    {
                        "size": {
                            "height": 169,
                            "width": 300
                        },
                        "url": "http://image.tmdb.org/t/p/w300/95KrNsjQtoL4hxeGztZo1L8rhZC.jpg"
                    },
                    {
                        "size": {
                            "height": 439,
                            "width": 780
                        },
                        "url": "http://image.tmdb.org/t/p/w780/95KrNsjQtoL4hxeGztZo1L8rhZC.jpg"
                    },
                    {
                        "size": {
                            "height": 562,
                            "width": 1000
                        },
                        "url": "http://image.tmdb.org/t/p/w1000/95KrNsjQtoL4hxeGztZo1L8rhZC.jpg"
                    },
                    {
                        "size": {
                            "height": 720,
                            "width": 1280
                        },
                        "url": "http://image.tmdb.org/t/p/w1280/95KrNsjQtoL4hxeGztZo1L8rhZC.jpg"
                    },
                    {
                        "size": {
                            "height": 1080,
                            "width": 1920
                        },
                        "url": "http://image.tmdb.org/t/p/w1920/95KrNsjQtoL4hxeGztZo1L8rhZC.jpg"
                    },
                    {
                        "size": {
                            "height": 1440,
                            "width": 2560
                        },
                        "url": "http://image.tmdb.org/t/p/original/95KrNsjQtoL4hxeGztZo1L8rhZC.jpg"
                    }
                ]
            },
            {
                "image_files": [
                    {
                        "size": {
                            "height": 169,
                            "width": 300
                        },
                        "url": "http://image.tmdb.org/t/p/w300/s8z7uIFOGQD6GpWgWgsWINNlFBr.jpg"
                    },
                    {
                        "size": {
                            "height": 439,
                            "width": 780
                        },
                        "url": "http://image.tmdb.org/t/p/w780/s8z7uIFOGQD6GpWgWgsWINNlFBr.jpg"
                    },
                    {
                        "size": {
                            "height": 562,
                            "width": 1000
                        },
                        "url": "http://image.tmdb.org/t/p/w1000/s8z7uIFOGQD6GpWgWgsWINNlFBr.jpg"
                    },
                    {
                        "size": {
                            "height": 720,
                            "width": 1280
                        },
                        "url": "http://image.tmdb.org/t/p/w1280/s8z7uIFOGQD6GpWgWgsWINNlFBr.jpg"
                    },
                    {
                        "size": {
                            "height": 1080,
                            "width": 1920
                        },
                        "url": "http://image.tmdb.org/t/p/w1920/s8z7uIFOGQD6GpWgWgsWINNlFBr.jpg"
                    },
                    {
                        "size": {
                            "height": 720,
                            "width": 1280
                        },
                        "url": "http://image.tmdb.org/t/p/original/s8z7uIFOGQD6GpWgWgsWINNlFBr.jpg"
                    }
                ]
            },
            {
                "image_files": [
                    {
                        "size": {
                            "height": 169,
                            "width": 300
                        },
                        "url": "http://image.tmdb.org/t/p/w300/7hr2n1a6SxXIEjkOZ2grKn1aHae.jpg"
                    },
                    {
                        "size": {
                            "height": 439,
                            "width": 780
                        },
                        "url": "http://image.tmdb.org/t/p/w780/7hr2n1a6SxXIEjkOZ2grKn1aHae.jpg"
                    },
                    {
                        "size": {
                            "height": 562,
                            "width": 1000
                        },
                        "url": "http://image.tmdb.org/t/p/w1000/7hr2n1a6SxXIEjkOZ2grKn1aHae.jpg"
                    },
                    {
                        "size": {
                            "height": 720,
                            "width": 1280
                        },
                        "url": "http://image.tmdb.org/t/p/w1280/7hr2n1a6SxXIEjkOZ2grKn1aHae.jpg"
                    },
                    {
                        "size": {
                            "height": 1080,
                            "width": 1920
                        },
                        "url": "http://image.tmdb.org/t/p/w1920/7hr2n1a6SxXIEjkOZ2grKn1aHae.jpg"
                    },
                    {
                        "size": {
                            "height": 1866,
                            "width": 3318
                        },
                        "url": "http://image.tmdb.org/t/p/original/7hr2n1a6SxXIEjkOZ2grKn1aHae.jpg"
                    }
                ]
            },
            {
                "image_files": [
                    {
                        "size": {
                            "height": 169,
                            "width": 300
                        },
                        "url": "http://image.tmdb.org/t/p/w300/hd2AqgppDdtLncOx9NImhlXIBb2.jpg"
                    },
                    {
                        "size": {
                            "height": 439,
                            "width": 780
                        },
                        "url": "http://image.tmdb.org/t/p/w780/hd2AqgppDdtLncOx9NImhlXIBb2.jpg"
                    },
                    {
                        "size": {
                            "height": 562,
                            "width": 1000
                        },
                        "url": "http://image.tmdb.org/t/p/w1000/hd2AqgppDdtLncOx9NImhlXIBb2.jpg"
                    },
                    {
                        "size": {
                            "height": 720,
                            "width": 1280
                        },
                        "url": "http://image.tmdb.org/t/p/w1280/hd2AqgppDdtLncOx9NImhlXIBb2.jpg"
                    },
                    {
                        "size": {
                            "height": 1080,
                            "width": 1920
                        },
                        "url": "http://image.tmdb.org/t/p/w1920/hd2AqgppDdtLncOx9NImhlXIBb2.jpg"
                    },
                    {
                        "size": {
                            "height": 1866,
                            "width": 3318
                        },
                        "url": "http://image.tmdb.org/t/p/original/hd2AqgppDdtLncOx9NImhlXIBb2.jpg"
                    }
                ]
            },
            {
                "image_files": [
                    {
                        "size": {
                            "height": 169,
                            "width": 300
                        },
                        "url": "http://image.tmdb.org/t/p/w300/nQXv1HkJwIFsO7hWjb3UHHbOq4K.jpg"
                    },
                    {
                        "size": {
                            "height": 439,
                            "width": 780
                        },
                        "url": "http://image.tmdb.org/t/p/w780/nQXv1HkJwIFsO7hWjb3UHHbOq4K.jpg"
                    },
                    {
                        "size": {
                            "height": 563,
                            "width": 1000
                        },
                        "url": "http://image.tmdb.org/t/p/w1000/nQXv1HkJwIFsO7hWjb3UHHbOq4K.jpg"
                    },
                    {
                        "size": {
                            "height": 720,
                            "width": 1280
                        },
                        "url": "http://image.tmdb.org/t/p/w1280/nQXv1HkJwIFsO7hWjb3UHHbOq4K.jpg"
                    },
                    {
                        "size": {
                            "height": 1080,
                            "width": 1920
                        },
                        "url": "http://image.tmdb.org/t/p/w1920/nQXv1HkJwIFsO7hWjb3UHHbOq4K.jpg"
                    },
                    {
                        "size": {
                            "height": 1632,
                            "width": 2901
                        },
                        "url": "http://image.tmdb.org/t/p/original/nQXv1HkJwIFsO7hWjb3UHHbOq4K.jpg"
                    }
                ]
            },
            {
                "image_files": [
                    {
                        "size": {
                            "height": 169,
                            "width": 300
                        },
                        "url": "http://image.tmdb.org/t/p/w300/nXX4es10U1dO7Knw5RsoE0BLAbu.jpg"
                    },
                    {
                        "size": {
                            "height": 439,
                            "width": 780
                        },
                        "url": "http://image.tmdb.org/t/p/w780/nXX4es10U1dO7Knw5RsoE0BLAbu.jpg"
                    },
                    {
                        "size": {
                            "height": 562,
                            "width": 1000
                        },
                        "url": "http://image.tmdb.org/t/p/w1000/nXX4es10U1dO7Knw5RsoE0BLAbu.jpg"
                    },
                    {
                        "size": {
                            "height": 720,
                            "width": 1280
                        },
                        "url": "http://image.tmdb.org/t/p/w1280/nXX4es10U1dO7Knw5RsoE0BLAbu.jpg"
                    },
                    {
                        "size": {
                            "height": 1080,
                            "width": 1920
                        },
                        "url": "http://image.tmdb.org/t/p/w1920/nXX4es10U1dO7Knw5RsoE0BLAbu.jpg"
                    },
                    {
                        "size": {
                            "height": 1632,
                            "width": 2902
                        },
                        "url": "http://image.tmdb.org/t/p/original/nXX4es10U1dO7Knw5RsoE0BLAbu.jpg"
                    }
                ]
            },
            {
                "image_files": [
                    {
                        "size": {
                            "height": 169,
                            "width": 300
                        },
                        "url": "http://image.tmdb.org/t/p/w300/opB1KJU2j4GZUGAE5OT5rfMPfba.jpg"
                    },
                    {
                        "size": {
                            "height": 439,
                            "width": 780
                        },
                        "url": "http://image.tmdb.org/t/p/w780/opB1KJU2j4GZUGAE5OT5rfMPfba.jpg"
                    },
                    {
                        "size": {
                            "height": 562,
                            "width": 1000
                        },
                        "url": "http://image.tmdb.org/t/p/w1000/opB1KJU2j4GZUGAE5OT5rfMPfba.jpg"
                    },
                    {
                        "size": {
                            "height": 720,
                            "width": 1280
                        },
                        "url": "http://image.tmdb.org/t/p/w1280/opB1KJU2j4GZUGAE5OT5rfMPfba.jpg"
                    },
                    {
                        "size": {
                            "height": 1080,
                            "width": 1920
                        },
                        "url": "http://image.tmdb.org/t/p/w1920/opB1KJU2j4GZUGAE5OT5rfMPfba.jpg"
                    },
                    {
                        "size": {
                            "height": 1632,
                            "width": 2902
                        },
                        "url": "http://image.tmdb.org/t/p/original/opB1KJU2j4GZUGAE5OT5rfMPfba.jpg"
                    }
                ]
            },
            {
                "image_files": [
                    {
                        "size": {
                            "height": 169,
                            "width": 300
                        },
                        "url": "http://image.tmdb.org/t/p/w300/fsLdVN4Ak9Fyz6eJc69dgOcaYt8.jpg"
                    },
                    {
                        "size": {
                            "height": 439,
                            "width": 780
                        },
                        "url": "http://image.tmdb.org/t/p/w780/fsLdVN4Ak9Fyz6eJc69dgOcaYt8.jpg"
                    },
                    {
                        "size": {
                            "height": 563,
                            "width": 1000
                        },
                        "url": "http://image.tmdb.org/t/p/w1000/fsLdVN4Ak9Fyz6eJc69dgOcaYt8.jpg"
                    },
                    {
                        "size": {
                            "height": 720,
                            "width": 1280
                        },
                        "url": "http://image.tmdb.org/t/p/w1280/fsLdVN4Ak9Fyz6eJc69dgOcaYt8.jpg"
                    },
                    {
                        "size": {
                            "height": 1080,
                            "width": 1920
                        },
                        "url": "http://image.tmdb.org/t/p/w1920/fsLdVN4Ak9Fyz6eJc69dgOcaYt8.jpg"
                    },
                    {
                        "size": {
                            "height": 816,
                            "width": 1450
                        },
                        "url": "http://image.tmdb.org/t/p/original/fsLdVN4Ak9Fyz6eJc69dgOcaYt8.jpg"
                    }
                ]
            }
        ],
        "slug": "boss-baby",
        "synopsis": "A story about how a new baby's arrival impacts a family, told from the point of view of a "
                    "delightfully unreliable narrator, a wildly imaginative 7 year old named Tim.",
        "title": "The Boss Baby",
        "tmdb_id": "295693",
        "trailers": [
            {
                "is_official": False,
                "language": "en",
                "trailer_files": [
                    {
                        "format": "youtube",
                        "transfert": "1920x1080",
                        "url": "https://www.youtube.com/watch?v=Ud8j5GaqH3c"
                    }
                ]
            },
            {
                "is_official": False,
                "language": "en",
                "trailer_files": [
                    {
                        "format": "youtube",
                        "transfert": "1920x1080",
                        "url": "https://www.youtube.com/watch?v=tquIfapGVqs"
                    }
                ]
            }
        ],
        "website": "http://www.dreamworks.com/thebossbaby/"
    }
}


class TestCinemas(unittest.TestCase):
    @async_test
    @mock_session(json.dumps(SERVER_RESPONSE))
    async def test_cinemas(self):
        manager = movies.MoviesManager(http_client.HttpClient("test"))
        cinema = await manager.get(101)
        self.assertEqual(len(cinema.cast), len(SERVER_RESPONSE['movie']['cast']))
        self.assertIn("Alec Baldwin", [x.name for x in cinema.cast])
        self.assertEqual(cinema.ratings['imdb'].value, 6.5)
        self.assertEqual(cinema.trailers[0].language, 'en')
        self.assertIn("http://image.tmdb.org/t/p/w342/pQC2N8eaO3haCZ887nxdFtaY4AM.jpg",
                      [x.url for x in cinema.poster_image])
