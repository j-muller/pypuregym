import json


class Response:

    def __init__(self, content, status_code=200):
        self.content = content
        self.status_code = status_code

    def raise_for_status(self):
        assert 200 <= self.status_code < 300

    def json(self):
        return json.loads(self.content)
