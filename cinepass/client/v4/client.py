from cinepass.client.v4 import showtimes, cities, cinemas, countries, http_client, movies, chains


class Client(object):
    def __init__(self, api_key):
        self.http = http_client.HttpClient(api_key)
        self.movies = movies.MoviesManager(self.http)
        self.cinemas = cinemas.CinemasManager(self.http)
        self.countries = countries.CountriesManager(self.http)
        self.cities = cities.CityManager(self.http)
        self.showtimes = showtimes.ShowtimeManager(self.http)
        self.chains = chains.ChainManeger(self.http)
