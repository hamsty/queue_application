from twisted.internet import reactor
from twisted.internet.endpoints import clientFromString, connectProtocol
from client.Communicate import Communicate

if __name__ == '__main__':
    point = clientFromString(reactor, "tcp:host=172.16.238.10:port=5678:timeout=10")
    connectProtocol(point, Communicate())
    reactor.run()
