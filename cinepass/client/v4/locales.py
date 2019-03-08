class LocalesManager(object):
    ENDPOINT = '/locales'

    def __init__(self, http_client):
        self.http_client = http_client

    async def all(self):
        response = await self.http_client.get(self.ENDPOINT)
        return response['locales']
