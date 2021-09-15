from qapp.entities.Request import Request
from qapp.entities.Response import Response
from twisted.internet.protocol import Protocol
from twisted.internet import reactor
from twisted.internet.endpoints import Factory


class Communicate(Protocol):

    def dataReceived(self, data: bytes):
        data = Request.get_object(data)

    def sendMessage(self, msg):
        response = Response(msg)
        self.transport.write(response)

class CommunicateFactory(Factory):

    def buildProtocol(self, addr):
        return Communicate()