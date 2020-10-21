import pytest

from pypuregym import PureAPI, Region


@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    monkeypatch.delattr('requests.sessions.Session.request')


# pylint: disable=protected-access
@pytest.fixture
def pure_api():
    api = PureAPI(
        username='john@doe.com',
        password='password123',
        region=Region.HK,
    )
    api._jwt_token = 'jwt-token'
    api._date = 42
    api._token = 'token'
    return api
