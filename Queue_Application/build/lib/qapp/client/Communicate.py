from twisted.internet.protocol import Protocol, ClientFactory
from qapp.entities.Response import Response
from qapp.client.CmdReceiver import CmdReceiver
from qapp.entities.Request import Request
from twisted.internet import stdio


class Communicate(Protocol):

    def connectionMade(self):
        self.io = stdio.StandardIO(CmdReceiver(self))

    def dataReceived(self, data: bytes):
        data = Response.get_object(data)
        print(data.response)

    def sendMessage(self, commmand, id):
        request = Request(commmand, id)
        self.transport.write(bytes(request))

    def connectionLost(self, reason):
        self.io.loseConnection()
        print("Connection ended!")


class CommunicateFactory(ClientFactory):

    def startedConnecting(self, connector):
        print("Wait for Connection!")

    def clientConnectionFailed(self, connector, reason):
        print(".", end="")
        connector.connect()

    def buildProtocol(self, addr):
        return Communicate()

    def clientConnectionLost(self, connector, reason):
        print(".", end="")
        connector.connect()
