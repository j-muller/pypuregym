import pytest

from pypuregym import PureAPI


def test_create_pureapi():
    client = PureAPI(
        username='', password='', gym_type='fitness', region='HK')
    assert client is not None

    with pytest.raises(AssertionError):
        PureAPI(
            username='', password='', gym_type='foobar', region='HK')
        PureAPI(
            username='', password='', gym_type='foobar', region='US')
