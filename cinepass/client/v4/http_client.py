import requests
import requests.auth


class CIAPIException(Exception):
    def __init__(self, *args, **kwargs):
        super(self, CIAPIException).__init__(*args, **kwargs)


class AuthStrategy(requests.auth.AuthBase):
    def __init__(self, api_key):
        self.api_key = api_key

    def __call__(self, request):
        """
        Add auth header to request
        :type request: requests.Request
        :return: request.Request
        """
        request.headers['X-Api-Key'] = self.api_key
        return request


class HttpClient(object):
    BASE_ENDPOINT = "https://api.internationalshowtimes.com/v4"

    def __init__(self, api_key):
        self.auth_strategy = AuthStrategy(api_key)

    @staticmethod
    def check_retcode(response):
        response.raise_for_status()
        if response.status_code in [10000, 40000]:
            raise CIAPIException("cinepass Exception with code %s returned" % response.status_code)

    def get(self, url, **params):
        response = requests.get(url=self.BASE_ENDPOINT + url, auth=self.auth_strategy, params=params)
        self.check_retcode(response)
        return response.json()
