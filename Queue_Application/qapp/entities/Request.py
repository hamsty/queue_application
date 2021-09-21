import json


class Request:

    def __init__(self, command, id):
        self.command = command
        self.id = id

    @staticmethod
    def get_object(json_str):
        obj = json.loads(json_str)
        return Request(obj["command"],obj["id"])

    def __str__(self):
        return json.dumps(self.__dict__)

    def __repr__(self):
        return json.dumps(self.__dict__)

    def __bytes__(self):
        return json.dumps(self.__dict__).encode("utf_8")