from enum import Enum


class STATE(Enum):
    AVAILABLE = 0
    RINGING = 1
    BUSY = 2


class Operator:

    def __init__(self, id):
        self._id = id
        self._state = STATE.AVAILABLE
        self._call_id = None
        self.timeout = None

    def get_id(self):
        return self._id

    def set_state(self, state: STATE):
        self._state = state

    def get_state(self):
        return self._state

    def get_call_id(self):
        return self._call_id

    def set_call_id(self, call_id):
        self._call_id = call_id

    def __str__(self):
        return self.__dict__.__str__()

    def __repr__(self):
        return self.__dict__.__repr__()
