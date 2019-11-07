class Chain(object):
    def __init__(self, id, name, websites, countries, **kwargs):
        self.id = id
        self.name = name
        self.websites = websites
        self.countries = countries

    @classmethod
    def from_dict(cls, obj):
        return cls(**obj)


class ChainManager(object):
    ENDPOINT = '/chains'

    def __init__(self, http_client):
        self.http_client = http_client

    async def all(self, countries):
        """
        countries: Filters the chains by country based on a single or
        a list of ISO 3166-1 alpha-2 codes.
        :type countries: [str]
        """
        response = await self.http_client.get(
            self.ENDPOINT,
            countries=countries
        )
        return [Chain.from_dict(x) for x in response['chains']]
