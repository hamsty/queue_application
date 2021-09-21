from twisted.protocols.basic import LineReceiver
from qapp.client.CliCmd import CliCmd


class CmdReceiver(LineReceiver):
    delimiter = b'\n'
    c = None

    def __init__(self, protocol):
        super().__init__()
        self.protocol = protocol

    def connectionMade(self):
        self.transport.write(CliCmd.intro.encode("utf_8"))
        self.c = CliCmd(self.protocol)

    def lineReceived(self, line):
        self.c.onecmd(line.decode("utf_8"))
