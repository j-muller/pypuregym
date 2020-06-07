from .utilities import Response

BOOKING_RESPONSE = b"""
{"error":{"message":"Success","code":200}}
"""


def test_book(pure_api, monkeypatch):
    monkeypatch.setattr(
        'requests.sessions.Session.post',
        lambda *args, **kwargs: Response(BOOKING_RESPONSE),
    )

    pure_api.book(42)
