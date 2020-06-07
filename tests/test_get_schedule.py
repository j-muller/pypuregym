from .utilities import Response

SCHEDULE_RESPONSE = b"""
{"error":{"code":200,"message":"Success"},"data":{"classes":[{
"id":113209,"sector":"F","class_type_id":48,"start_date":"2020-06-07",
"end_date":"2020-06-07","start_time":"09:00:00","end_time":"09:45:00",
"duration":"2700000","teacher_id":782,"location_id":10,"level_id":9,
"pillar_id":6,"button_status":0,"booking_id":0,
"start_datetime":"2020-06-07T09:00:00+08:00","is_free":false,
"color_code":"","is_filmed":false,"is_online":0,"is_cycling":false,
"free_class_type":0,"special_flag":null,"duration_min":45,
"class_type":{"id":48,"name":"TRX Blast",
"description":"","is_fuze":false,"pillar":{"name":"Strength",
"color":"#ed1c24","code":"strength_and_conditioning"},"level":"All Levels"},
"teacher":{"id":782,"name":"","full_name":"","image_link":"",
"type":"teacher"}}]}}
"""


def test_get_schedule(pure_api, monkeypatch):
    monkeypatch.setattr(
        'requests.sessions.Session.get',
        lambda *args, **kwargs: Response(SCHEDULE_RESPONSE),
    )

    classes = pure_api.get_schedule(
        start_date='2020-06-07',
        last_date='2020-06-07',
        location_id=10,
    )
    assert len(classes) == 1
