# pylint: disable=unused-argument, protected-access
from .utilities import Response

TOKEN_RESPONSE = b"""
var jQueryHeaders = {"X-Date":1591455317,"X-Token":"e4c593102ab8"};
var jQueryData = {"language_id":1,"region_id":4};
"""

LOGIN_RESPONSE = b"""
{"error":{"code":200,"message":"Success"},"data":{"user":{
"id":"42","username":"","first_name":"John","last_name":"Doe",
"token":"amVmZ0xNTkxNDUxMjAx",
"mbo_rssid":"42","mbo_uid":"42","bind_chat":false,
"jwt":"Bu34arQ"}}}
"""


def test_authenticate(pure_api, monkeypatch):
    monkeypatch.setattr(
        'requests.sessions.Session.get',
        lambda *args, **kwargs: Response(TOKEN_RESPONSE))

    monkeypatch.setattr(
        'requests.sessions.Session.post',
        lambda *args, **kwargs: Response(LOGIN_RESPONSE))

    pure_api.authenticate()

    assert pure_api._token
    assert pure_api._date
    assert pure_api._jwt_token
