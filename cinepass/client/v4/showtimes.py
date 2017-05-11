import cinemas
import movies


class Showtime(object):
    def __init__(self, id, movie_id, cinema_id, start_at, is_3d, **kwargs):
        self.id = id
        self.movie_id = movie_id
        self.cinema_id = cinema_id
        self.start_at = start_at
        self.is_3d = is_3d
        self.language = kwargs.get('language')
        self.subtitle_language = kwargs.get('subtitle_language')
        self.auditorium = kwargs.get('auditorium')
        self.booking_type = kwargs.get('booking_type')
        self.cinema_movie_title = kwargs.get('cinema_movie_title')
        self.booking_link = kwargs.get('booking_link')
        self.http_client = kwargs.get('http_client')
        self._movie = None
        self._cinema = None

    @property
    def cinema(self):
        if self._cinema:
            return self._cinema
        if self.http_client:
            manager = cinemas.CinemasManager(self.http_client)
            return manager.get(self.cinema_id)

    @property
    def movie(self):
        if self._movie:
            return self._movie
        if self.http_client:
            manager = movies.MoviesManager(self.http_client)
            return manager.get(self.movie_id)


class ShowtimeManager(object):
    ENDPOINT = '/showtimes'

    def __init__(self, http_client):
        self.http_client = http_client

    def get(self, id, **kwargs):
        response = self.http_client.get("%s/%s" % (self.ENDPOINT, id), params=kwargs)
        showtime_data = response['showtime']
        return Showtime(http_client=self.http_client, **showtime_data)

    def all(self, **kwargs):
        response = self.http_client.get(self.ENDPOINT, **kwargs)['showtimes']
        return [Showtime(http_client=self.http_client, **obj) for obj in response]
