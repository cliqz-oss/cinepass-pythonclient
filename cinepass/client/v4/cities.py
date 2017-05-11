class City(object):
    __slots__ = ['id', 'name', 'slug', 'lat', 'lon', 'country']

    def __init__(self, id, name, slug, lat, lon, country):
        self.id = int(id)
        self.name = name
        self.slug = slug
        self.lat = lat
        self.lon = lon
        self.country = country

    def __repr__(self):
        return "<City: %s %s %s (%s %s) %s>" % (self.id, self.name, self.slug, self.lat, self.lon, self.country)

    def __eq__(self, other):
        return self.id == other.id


class CityManager(object):
    ENDPOINT = '/cities'

    def __init__(self, http_client):
        self.http_client = http_client

    def get(self, offset=0, limit=1500, lang='en', countries=None, near_to=None, movie_id=None, query=None):
        params = {
            'offset': offset,
            'limit': limit,
            'lang': lang
        }
        if countries:
            params['countries'] = countries
        if near_to:
            params['near_to'] = near_to
        if movie_id:
            params['movie_id'] = movie_id
        if query:
            params['query'] = query
        result = self.http_client.get(self.ENDPOINT, **params)
        cities = result['cities']
        return [City(**args) for args in cities]
