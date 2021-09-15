import cmd


class CliCmd(cmd.Cmd):
    intro = 'Connected to Queue Server. Type help or ? to list commands.\n'

    def __init__(self, protocol):
        super().__init__()
        self.protocol = protocol

    def do_call(self, arg):
        'Do call. Type call <id>'
        try:
            if not arg:
                raise CliCmd.CmdException()
            arg = arg.split()
            if len(arg) > 1:
                raise CliCmd.CmdException()
            id = int(arg[0])
            self.protocol.sendMessage("call", id)
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
            self.protocol.sendMessage("answer", id)
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
            self.protocol.sendMessage("reject", id)
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
            self.protocol.sendMessage("hangup", id)
        except (CliCmd.CmdException, ValueError):
            self.onecmd("help hangup")

    class CmdException(Exception):

        def __init__(self, *args, **kwargs):
            pass
