import json


class Response:

    def __init__(self, response:str):
        self.response = response

    @staticmethod
    def get_object(json_str):
        obj = json.loads(json_str)
        return Response(obj["response"])

    def __str__(self):
        return json.dumps(self.__dict__)

    def __repr__(self):
        return json.dumps(self.__dict__)

    def __bytes__(self):
        return json.dumps(self.__dict__).encode("utf_8")