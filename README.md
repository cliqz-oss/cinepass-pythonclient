cinepass-pythonclient, a Python SDK for cinepass.de
=====================

> Made by Cliqz, a provider of innovative, privacy-focused browser technologies with integrated quick-search functionality and anti-tracking. Cliqz is a German company owned by Mozilla and Hubert Burda Media. Visit https://cliqz.com for more information.

## Overview
This library can be used for access to https://cinepass.de REST API via Python.
Detailed description of API you can find at https://api.cinepass.de/documentation.


Basic usage:

```python
    from cinepass import Client
    client = Client(api_key='<your api key>')
    client.movies.all()  # get list of all movies
    client.cinemas.all(location='52.50,13.37')  # get cinemas around location
    ...  # and so on
```

## Installation
For the time being you need to use this lib from source, no package provided.

## Tests
See the tests directory

## Documentation
The library aims to provide a direct mapping for the Cinepass API. See https://api.cinepass.de/documentation for a detailed documentation of the API.

## Contributing
* Bug reports, feature requests and general question can be added as an Issue. 
* PRs are welcome. 
* Questions? Concerns? Feel free to [contact us](mailto:cliqz-oss@cliqz.com?subject=cinepass-pythonclient).
