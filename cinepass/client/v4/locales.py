class LocalesManager(object):
    ENDPOINT = '/locales'

    def __init__(self, http_client):
        self.http_client = http_client

    def all(self):
        response = self.http_client.get(self.ENDPOINT)
        return response['locales']
