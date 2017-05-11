=====================
cinepass-pythonclient
=====================


This library can be used for access to
https://cinepass.de REST API via Python.
Detailed description of API you can find at https://api.cinepass.de/documentation.


Basic usage:

::
    from cinepass import Client
    client = Client(api_key='<your api key>')
    client.movies.all()  # get list of all movies
    client.cinemas.all(location='52.50,13.37')  # get cinemas around location
    ...  # and so on

