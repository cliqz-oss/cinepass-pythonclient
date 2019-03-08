import asyncio
import json
from contextlib import asynccontextmanager

import mock


class Session(object):
    def __init__(self, value):
        self.value = value

    def __call__(self):
        return self

    @asynccontextmanager
    async def get(self, _, **kwargs):
        yield MockResponse(self.value)

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        pass

    async def __anext__(self):
        return self


class MockResponse(object):
    def __init__(self, text):
        self.text = text
        self.status = 200

    async def json(self):
        return json.loads(self.text)

    def raise_for_status(self):
        pass


def mock_session(value):
    def decorator(func):
        async def wrapper(*args, **kwargs):
            with mock.patch("aiohttp.ClientSession", Session(value)):
                return await func(*args, **kwargs)
        return wrapper
    return decorator


def async_test(func):
    def decorator(*args, **kwargs):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(func(*args, **kwargs))
    return decorator
