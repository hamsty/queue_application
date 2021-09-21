from qapp.entities.Request import Request
from qapp.entities.Response import Response
from twisted.internet.protocol import Protocol
from twisted.internet.endpoints import Factory
from qapp.server.ServerCmd import ServerCmd


class Communicate(Protocol):


    def __init__(self):
        self.cmd = ServerCmd(self)

    def dataReceived(self, data: bytes):
        request = Request.get_object(data)
        print(request)
        self.cmd.onecmd("{} {}".format(request.command, request.id))


    def sendMessage(self, msg):
        response = Response(msg)
        self.transport.write(bytes(response))

class CommunicateFactory(Factory):

    def buildProtocol(self, addr):
        return Communicate()