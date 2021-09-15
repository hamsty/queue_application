import cmd
from qapp.client.Communicate import Communicate
from qapp.entities.Request import Request


class CliCmd(cmd.Cmd):
    intro = 'Welcome to the Queue Cli. Type help or ? to list commands.\n'

    def do_call(self, arg):
        'Do call. Type call <id>'
        try:
            if not arg:
                raise CliCmd.CmdException()
            arg = arg.split()
            if len(arg) > 1:
                raise CliCmd.CmdException()
            id = int(arg[0])
            json = Request("call",id)
            print(json)
        except (CliCmd.CmdException, ValueError):
            self.onecmd("help call")

    def do_answer(self, arg):
        'Do answer. Type answer <id>'
        try:
            if not arg:
                raise CliCmd.CmdException()
            arg = arg.split()
            if len(arg) > 1:
                raise CliCmd.CmdException()
            id = str(arg[0])
            json = Request("answer", id)
            print(json)
        except (CliCmd.CmdException, ValueError):
            self.onecmd("help answer")

    def do_reject(self, arg):
        'Do reject. Type reject <id>'
        try:
            if not arg:
                raise CliCmd.CmdException()
            arg = arg.split()
            if len(arg) > 1:
                raise CliCmd.CmdException()
            id = str(arg[0])
            json = Request("reject", id)
            print(json)
        except (CliCmd.CmdException, ValueError):
            self.onecmd("help reject")

    def do_hangup(self, arg):
        'Do hangup. Type hangup <id>'
        try:
            if not arg:
                raise CliCmd.CmdException()
            arg = arg.split()
            if len(arg) > 1:
                raise CliCmd.CmdException()
            id = int(arg[0])
            json = Request("hangup", id)
            print(json)
        except (CliCmd.CmdException, ValueError):
            self.onecmd("help hangup")

    class CmdException(Exception):

        def __init__(self, *args, **kwargs):
            pass
