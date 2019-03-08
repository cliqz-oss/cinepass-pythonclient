import aiohttp


class CIAPIException(Exception):
    def __init__(self, *args, **kwargs):
        super(self, CIAPIException).__init__(*args, **kwargs)


class HttpClient(object):
    BASE_ENDPOINT = "https://api.internationalshowtimes.com/v4"

    def __init__(self, api_key):
        self.api_key = api_key

    @staticmethod
    def check_retcode(response):
        response.raise_for_status()
        if response.status in [10000, 40000]:
            raise CIAPIException(
                "cinepass Exception with code %s returned"
                % response.status
            )

    async def get(self, url: str, **params) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    self.BASE_ENDPOINT + url,
                    headers={'X-Api-Key': self.api_key},
                    params=params
            ) as response:
                self.check_retcode(response)
                return await response.json()
