from twisted.internet import reactor
from server.Communicate import CommunicateFactory
from twisted.internet.endpoints import serverFromString


if __name__ == '__main__':
    point = serverFromString(reactor, "tcp:port=5678")
    point.listen(CommunicateFactory())
    print("Server started")
    reactor.run()
