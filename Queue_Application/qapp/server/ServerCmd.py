import cmd
import json
from queue import Queue
from qapp.entities.Operator import Operator, STATE
from twisted.internet import reactor


class Watchdog:

    is_on = False

    def start(self, response, op, cmd, protocol):
        self.call = reactor.callLater(10,self.timeout, response, op, cmd, protocol)
        self.is_on = True

    def stop(self):
        if self.is_on:
            self.call.cancel()
            self.is_on = False


    def timeout(self, response, op, cmd, protocol):
        protocol.sendMessage(response)
        op.set_state(STATE.AVAILABLE)
        call_id = op.get_call_id()
        op.set_call_id(None)
        cmd.onecmd("recall {}".format(call_id))
        op.set_state(STATE.AVAILABLE)


class ServerCmd(cmd.Cmd):

    def __init__(self, protocol):
        super().__init__()
        self.operators = []
        self.queue_calls = Queue()
        self.queue_count = 0
        with open("/etc/Queue_Application/config/operators.json", "r") as fp:
            obj = json.load(fp)
            for operator in obj["operators"]:
                op = Operator(operator["id"])
                self.operators.append(op)
        self.protocol = protocol
        self.watchdog = Watchdog()

    def do_recall(self, arg):
        try:
            if not arg:
                raise ServerCmd.CmdException()
            arg = arg.split()
            if len(arg) > 1:
                raise ServerCmd.CmdException()
            id = int(arg[0])
            reactor.callLater(1,self.call, id)
        except (ServerCmd.CmdException, ValueError):
            pass

    def call(self, id):
        for op in self.operators:
            if op.get_state() == STATE.AVAILABLE:
                op.set_state(STATE.RINGING)
                op.set_call_id(id)
                response = "Call {} ringing for operator {}".format(id, op.get_id())
                self.protocol.sendMessage(response)
                response = "Call {} ignored by operator {}".format(id, op.get_id())
                self.watchdog.start(response, op, self, self.protocol)
                return True
        self.queue_calls.put(id)
        self.queue_count += 1
        response = "Call {} waiting in queue".format(id)
        self.protocol.sendMessage(response)
        return True

    def do_call(self, arg):
        'Do call. Type call <id>'
        try:
            if not arg:
                raise ServerCmd.CmdException()
            arg = arg.split()
            if len(arg) > 1:
                raise ServerCmd.CmdException()
            id = int(arg[0])
            response = "Call {} received".format(id)
            self.protocol.sendMessage(response)
            reactor.callLater(1,self.call, id)
        except (ServerCmd.CmdException, ValueError):
            pass

    def do_answer(self, arg):
        'Do answer. Type answer <id>'
        try:
            if not arg:
                raise ServerCmd.CmdException()
            arg = arg.split()
            if len(arg) > 1:
                raise ServerCmd.CmdException()
            id = str(arg[0])
            self.watchdog.stop()
            for op in self.operators:
                if op.get_id() == id:
                    if op.get_state() == STATE.RINGING:
                        op.set_state(STATE.BUSY)
                        response = "Call {} answered by operator {}".format(op.get_call_id(), op.get_id())
                        self.protocol.sendMessage(response)
                    elif op.get_state() == STATE.AVAILABLE:
                        response = "Operator {} don't have calls to answer".format(op.get_id())
                        self.protocol.sendMessage(response)
                    else:
                        response = "Operator {} answered the call".format(op.get_id())
                        self.protocol.sendMessage(response)
                    return True
            response = "Operator {} don't exist".format(id)
            self.protocol.sendMessage(response)
            return True
        except (ServerCmd.CmdException, ValueError):
            pass

    def do_reject(self, arg):
        'Do reject. Type reject <id>'
        try:
            if not arg:
                raise ServerCmd.CmdException()
            arg = arg.split()
            if len(arg) > 1:
                raise ServerCmd.CmdException()
            id = str(arg[0])
            self.watchdog.stop()
            for op in self.operators:
                if op.get_id() == id:
                    if op.get_state() == STATE.RINGING:
                        op.set_state(STATE.AVAILABLE)
                        call_id = op.get_call_id()
                        op.set_call_id(None)
                        self.onecmd("recall {}".format(call_id))
                        response = "Call {} rejected by operator {}".format(call_id, op.get_id())
                        self.protocol.sendMessage(response)
                    elif op.get_state() == STATE.AVAILABLE:
                        response = "Operator {} don't have calls to reject".format(op.get_id())
                        self.protocol.sendMessage(response)
                    else:
                        response = "Operator {} answered the call".format(op.get_id())
                        self.protocol.sendMessage(response)
                    return True
            response = "Operator {} don't exist".format(id)
            self.protocol.sendMessage(response)
            return True
        except (ServerCmd.CmdException, ValueError):
            pass

    def do_hangup(self, arg):
        'Do hangup. Type hangup <id>'
        try:
            if not arg:
                raise ServerCmd.CmdException()
            arg = arg.split()
            if len(arg) > 1:
                raise ServerCmd.CmdException()
            id = int(arg[0])
            self.watchdog.stop()
            for op in self.operators:
                if op.get_call_id() == id:
                    if op.get_state() == STATE.RINGING:
                        response = "Call {} missed".format(id)
                    else:
                        response = "Call {} finished and operator {} available".format(id, op.get_id())
                    op.set_state(STATE.AVAILABLE)
                    op.set_call_id(None)
                    self.protocol.sendMessage(response)
                    if not self.queue_calls.empty():
                        self.onecmd("recall {}".format(self.queue_calls.get()))
                        self.queue_count -= 1
                    return True
            count = 0
            qcount = self.queue_count
            while count < qcount:
                count += 1
                call = self.queue_calls.get()
                if call == id:
                    self.queue_count -= 1
                    continue
                self.queue_calls.put(call)
            if count > self.queue_count:
                response = "Call {} missed".format(id)
            else:
                response = "Call {} don't exist".format(id)
            self.protocol.sendMessage(response)

            return True
        except (ServerCmd.CmdException, ValueError):
            pass

    class CmdException(Exception):

        def __init__(self, *args, **kwargs):
            pass
