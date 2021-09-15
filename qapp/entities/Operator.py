from enum import Enum


class STATE(Enum):
    AVAILABLE = 0
    RINGING = 1
    BUSY = 2


class Operator:

    def __init__(self, id):
        self._id = id
        self._state = STATE.AVAILABLE

    def get_id(self):
        return self._id

    def set_state(self, state: STATE):
        self._state = state

    def get_state(self):
        return self._state
