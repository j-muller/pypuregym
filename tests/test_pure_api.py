from pypuregym import PureAPI, Region


def test_create_pureapi():
    client = PureAPI(username='', password='', region=Region.HK)
    assert client is not None
