from twisted.internet import stdio, reactor
from twisted.internet.endpoints import clientFromString, connectProtocol
from twisted.internet import defer
from client.CmdReceiver import CmdReceiver
from client.Communicate import Communicate




if __name__ == '__main__':
    stdio.StandardIO(CmdReceiver())
    point = clientFromString(reactor, "tcp:host=127.0.0.1:port=5678:timeout=10")
    deferer = defer.Deferred(connectProtocol(point, Communicate()))
    reactor.run()
