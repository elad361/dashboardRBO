from statemachine import StateMachine, State

class ProcMachine(StateMachine):
    procStart = State(initial=True)
    procActive = State()
    procEnd = State()
    cycle = (procStart.to(procActive)| procActive.to(procEnd)| procEnd.to(procStart))

    def before_cycle(self, event: str, source: State, target: State, message: str = ""):
       message = ". " + message if message else ""
       return f"Running {event} from {source.id} to {target.id}{message}"

    def on_enter_procStart(self):
       print("enter start state.")

    def on_exit_procStart(self):
       print("exit start state.")

    def on_enter_procActive(self):
        print("enter active state.")

    def on_exit_procActive(self):
        print("exit active state.")

    def on_enter_procEnd(self):
        print("enter end state.")

    def on_exit_procEnd(self):
        print("exit end state.")