from twisted.internet.protocol import Protocol
from qapp.entities.Response import Response
from qapp.entities.Request import Request


class Communicate(Protocol):

    def connectionMade(self):
        request = Request("call","1")
        self.transport.write(bytes(request))
        print("batata")

    def dataReceived(self, data: bytes):
        data = Response.get_object(data)
        print(data.response)

    def sendMessage(self, msg):
        print(msg)
        self.transport.write(msg)