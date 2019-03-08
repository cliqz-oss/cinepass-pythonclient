import collections

Country = collections.namedtuple('Country', 'iso_code is_access_granted')


class CountriesManager(object):
    ENDPOINT = '/countries'

    def __init__(self, http_client):
        self.http_client = http_client

    async def all(self, access_granted=None):
        """
        Returns list of all countries
        :param access_granted: boolean
        :return: [Country]
        """
        response = await self.http_client.get(self.ENDPOINT)
        countries = response['countries']
        if access_granted is not None:
            countries = filter(lambda x: x['is_access_granted'], countries)
        return [Country(x['iso_code'], x['is_access_granted']) for x in countries]
