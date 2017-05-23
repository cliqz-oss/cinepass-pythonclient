import itertools


class Address(object):
    __slots = ['text', 'street', 'house', 'zipcode', 'city', 'state', 'state_abbr', 'country_name', 'country_code']

    def __init__(self, display_text, street, house, zipcode, city, state, state_abbr, country, country_code):
        self.text = display_text
        self.street = street
        self.house = house
        self.zipcode = zipcode
        self.city = city
        self.state = state
        self.state_abbr = state_abbr
        self.country_name = country
        self.country_code = country_code

    def __repr__(self):
        return '<Address: %s>' % self.text


class Location(object):
    __slots__ = ['lat', 'lon', 'address']

    def __init__(self, lat, lon, address=None):
        self.lat = lat
        self.lon = lon
        self.address = address

    @classmethod
    def from_dict(cls, dict_object):
        address_dict = dict_object.pop('address')
        address = Address(**address_dict)
        dict_object['address'] = address
        return cls(**dict_object)


class Cinema(object):
    def __init__(self, id, slug, name, booking_type,
                 telephone=None, chain_id=None, phone=None, email=None, website=None, location=None):
        self.id = id
        self.slug = slug
        self.name = name
        self.chain_id = chain_id
        self.phone = phone
        self.email = email
        self.website = website
        self.location = Location.from_dict(location)
        self.booking_type = booking_type
        self.telephone = telephone

    def __repr__(self):
        return '<Cinema %s: %s>' % (self.id, self.name)


class CinemasManager(object):
    ENDPOINT = '/cinemas'

    def __init__(self, http_client):
        self.http_client = http_client

    def get(self, cinema_id, lang='en'):
        response = self.http_client.get('%s/%s' % (self.ENDPOINT, cinema_id), lang=lang)
        cinema_info = response['cinema']
        cinema = Cinema(**cinema_info)
        return cinema

    def _all(self, offset=0, limit=1500, distance=20,
             city_ids=None, chain_ids=None, location=None, bounds=None, countries=None):
        """

        :type countries: str
        :param countries: Filters the cinemas by country based on a single or a list of ISO 3166-1 alpha-2 codes.
        Example: DE,AT

        :type city_ids: str
        :param city_ids: Example: 1,2,4

        :type chain_ids: str
        :param chain_ids: Filters the cinemas by the giving single or list of chain ids.
        Example: 1,2,4

        :type location: str
        :param location: Retrieve cinemas in a particular area by passing a geo loaction as center
        in the format lat,lon. Format lat,lon.
        Example: 52.50,13.37

        :type bounds: str
        :param bounds: Limit cinemas to geographical polygon given as list of at least two points in the follwoing
        format: (lat,lon),(lat,lon)[,(lat,lon)...]
        When passing only two points a bounding box will be build. For polygons make sure there are no crossing edges by
        sorting the points appropriately.
        Example: (52.1,13.15),(52.9,13.37)
        """
        params = {
            'offset': offset,
            'limit': limit,
            'distance': distance
        }
        if city_ids:
            params['city_ids'] = city_ids
        if chain_ids:
            params['chain_ids'] = chain_ids
        if location:
            params['location'] = location
        if bounds:
            params['bounds'] = bounds
        if countries:
            params['countries'] = countries

        response = self.http_client.get(self.ENDPOINT, **params)
        return [Cinema(**info) for info in response['cinemas']]

    def all(self, chunk_size=100, limit=1500, offset=0, **kwargs):
        return list(itertools.chain.from_iterable(
            [self._all(limit=chunk_size, offset=offset + i, **kwargs) for i in
             range(0, limit, chunk_size)]))
