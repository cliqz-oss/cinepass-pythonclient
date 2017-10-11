import collections
import datetime
import itertools

import six


def add_deserializer(klass):
    def deserilizer(cls, obj):
        return cls(**obj)

    klass.from_dict = classmethod(deserilizer)
    return klass


@add_deserializer
class Genre(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name


@add_deserializer
class TrailerFile(object):
    def __init__(self, format, transfert, url):
        self.format = format
        self.transfert = transfert
        self.url = url


class Trailer(object):
    def __init__(self, language, is_official=None, files=None):
        self.language = language
        self.is_official = is_official
        self.files = files

    @classmethod
    def from_dict(cls, obj):
        return cls(is_official=obj['is_official'], language=obj['language'],
                   files=[TrailerFile.from_dict(x) for x in obj['trailer_files']])

    @classmethod
    def from_list(cls, lst):
        if not lst:
            return None
        return [cls.from_dict(item) for item in lst]


@add_deserializer
class Rating(object):
    def __init__(self, value, vote_count):
        self.value = value
        self.vote_count = vote_count

    @classmethod
    def from_rating_struct(cls, dict_obj):
        if not dict_obj:
            return None
        result = {}
        for site, rating in six.iteritems(dict_obj):
            result[site] = cls.from_dict(rating)
        return result


@add_deserializer
class ReleaseDate(object):
    def __init__(self, locale, region, date):
        self.locale = locale
        self.region = region
        self.date = datetime.datetime.strptime(date, "%Y-%m-%d")

    @classmethod
    def from_releases_dict(cls, dict_object):
        if not dict_object:
            return None
        result = collections.defaultdict(list)
        for locale, release_list in six.iteritems(dict_object):
            for release in release_list:
                result[locale].append(cls.from_dict(release))
        return result


class Image(object):
    def __init__(self, url, height=None, width=None):
        self.url = url
        self.heigth = height
        self.width = width

    @classmethod
    def from_dict_single(cls, dict_obj):
        return cls(url=dict_obj['url'],
                   height=dict_obj['size']['height'],
                   width=dict_obj['size']['width'])

    @classmethod
    def from_dict(cls, dict_obj):
        if dict_obj:
            images = dict_obj['image_files']
            return [cls.from_dict_single(obj) for obj in images]

    @classmethod
    def from_list(cls, list_obj):
        if list_obj:
            return [cls.from_dict(dict_obj) for dict_obj in list_obj]


class Person(object):
    def __init__(self, id, name, image=None, job=None, character=None):
        self.name = name
        self.id = id
        self.job = job
        self.character = character
        self.image = image

    @classmethod
    def from_list(cls, entities):
        if not entities:
            return None
        return [cls(**obj) for obj in entities]


class Movie(object):
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.slug = kwargs.get('slug')
        self.original_title = kwargs.get('original_title')
        self.title = kwargs.get('title')
        self.original_language = kwargs.get('original_language')
        self.synopsis = kwargs.get('synopsis')
        self.poster_image = Image.from_dict(kwargs.get('poster_image'))
        self.poster_image_thumbnail = kwargs.get('poster_image_thumbnail')
        self.scene_images = Image.from_list(kwargs.get('scene_images'))
        self.runtime = kwargs.get('runtime')
        self.trailers = Trailer.from_list(kwargs.get('trailers'))
        self.ratings = Rating.from_rating_struct(kwargs.get('ratings'))
        self.age_limits = kwargs.get('age_limits')
        self.release_dates = ReleaseDate.from_releases_dict(kwargs.get('release_dates'))
        self.website = kwargs.get('website')
        self.production_companies = kwargs.get('production_companies')
        self.keywords = kwargs.get('keywords')
        self.imdb_id = kwargs.get('imdb_id')
        self.tmdb_id = kwargs.get('tmdb_id')
        self.rentrak_film_id = kwargs.get('rentrak_film_id')
        self.cast = Person.from_list(kwargs.get('cast'))
        self.crew = Person.from_list(kwargs.get('crew'))


class MoviesManager(object):
    ENDPOINT = '/movies'

    def __init__(self, http_client):
        self.http_client = http_client

    def get(self, id, **kwargs):
        response = self.http_client.get("%s/%s" % (self.ENDPOINT, id), params=kwargs)
        movie_data = response['movie']
        return Movie(**movie_data)

    def _all(self, **kwargs):
        fields = kwargs.get('fields') or \
                 'id,title,slug,poster_image_thumbnail,release_dates,runtime,age_limits' \
                 ',cast,crew,synopsis,imdb_id,ratings,website,trailers,poster_image,original_language,original_title'
        kwargs['fields'] = fields
        response = self.http_client.get(self.ENDPOINT, **kwargs)
        return [Movie(**data) for data in response['movies']]

    def all(self, chunk_size=100, limit=1500, offset=0, **kwargs):
        return list(itertools.chain.from_iterable(
            [self._all(limit=chunk_size, offset=offset+i, **kwargs) for i in range(0, limit, chunk_size)]))
