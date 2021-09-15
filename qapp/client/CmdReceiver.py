from twisted.protocols.basic import LineReceiver
from qapp.client.CliCmd import CliCmd


class CmdReceiver(LineReceiver):
    delimiter = b'\n'
    c = None

    def connectionMade(self):
        self.transport.write(CliCmd.intro.encode("utf_8"))
        self.transport.write(b">>> ")
        self.c = CliCmd()

    def lineReceived(self, line):
        self.c.onecmd(line.decode("utf_8"))
        self.transport.write(b">>> ")
