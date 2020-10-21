from pypuregym import GymType
from .utilities import Response


LOCATION_RESPONSE = b"""
{"error":{"code":200,"message":"Success"},"data":{"locations":[
{"id":15,"code":"LKF","image_link":"","contact_no":"+852 82000032",
"latitude":"22.2810210000","longitude":"114.1554130000",
"region_id":1,"crm_location_id":23,"is_yoga":false,"is_fitness":true,
"is_public":true,"is_fuze":false,"is_online":false,
"names":{"en":"Fitness - California Tower - LKF"},
"short_name":{"en":"California Tower - LKF"}}]}}
"""


def test_get_locations(pure_api, monkeypatch):
    monkeypatch.setattr(
        'requests.sessions.Session.get',
        lambda *args, **kwargs: Response(LOCATION_RESPONSE),
    )

    locations = pure_api.get_locations(GymType.FITNESS)
    assert len(locations) == 1
    assert locations[0]['id'] == 15
