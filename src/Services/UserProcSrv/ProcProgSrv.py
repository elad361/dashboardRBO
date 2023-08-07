from statemachine import StateMachine, State
#GUI interactions
from PySide6.QtCore import QThread, Signal, Slot
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget

class ProcProgSrvSm(StateMachine):
    procProgStart = State(initial=True)
    procProgActive = State()
    procProgEnd = State()
    cycle = (procProgStart.to(procProgActive)| procProgActive.to(procProgEnd)| procProgEnd.to(procProgStart))

    def before_cycle(self, event: str, source: State, target: State, message: str = ""):
       message = ". " + message if message else ""
       return f"Running {event} from {source.id} to {target.id}{message}"

    def on_enter_procProgStart(self):
       print("enter prog start state.")

    def on_exit_procProgStart(self):
       print("exit prog start state.")

    def on_enter_procProgActive(self):
        print("enter prog active state.")

    def on_exit_procProgActive(self):
        print("exit prog active state.")

    def on_enter_procProgEnd(self):
        print("enter prog end state.")

    def on_exit_procProgEnd(self):
        print("exit prog end state.")


class ProcWorker(QWidget):
    finished = Signal()
    intReady = Signal(str)

    @Slot()
    def __init__(self):
        super(ProcWorker, self).__init__()
        self.working = True

    def work(self):
        while self.working:
           self.intReady.emit(line)

        self.finished.emit()

class ProcProgSrv():
    def __init__(self,proc_ui):

        self.ui_main = proc_ui

        sm = ProcProgSrvSm()

        self.thread = None
        self.worker = None


        #self.ui_prog_srv_pageproc_page.enter_search_layout(self.prog_task_toggle_button)
        self.ui_main.prog_task_toggle_button.clicked.connect(self.start_loop)
        self.pushBtnClicked = False
        self.CopyFlag = 0

    def loop_finished(self):
        print('Loop Finished')

    def start_loop(self):
        print('Loop start')

        # Verify the correct COM Port
        # try:
        #     mytext = "\n"  # Send first enter
        #     global ser
        #     ser = serial.Serial(self.cb_Port.currentText(), 115200, timeout=1)  # (ports[0], 115200)    #('COM1', 115200, timeout=1)
        #     ser.write(mytext.encode())
        # except:
        #     msgBox = QMessageBox()
        #     msgBox.setWindowTitle("COM Port Error!")
        #     msgBox.setIcon(QMessageBox.Warning)
        #     msgBox.setText("Selected COM port does not exist. Please verify the COM port Number.")
        #     msgBox.exec()
        #     self.label_5.setText("Not Connected")
        #     self.label_5.setStyleSheet('color: red')
        #     return

        # self.worker = ProcWorker()  # a new worker to perform those tasks
        # self.thread = QThread()  # a new thread to run our background tasks in
        # self.worker.moveToThread(
        #     self.thread)  # move the worker into the thread, do this first before connecting the signals
        #
        # self.thread.started.connect(
        #     self.worker.work)  # begin our worker object's loop when the thread starts running
        #
        # self.worker.intReady.connect(self.onIntReady)
        #
        # self.pushButton_2.clicked.connect(self.stop_loop)  # stop the loop on the stop button click
        #
        # self.worker.finished.connect(self.loop_finished)  # do something in the gui when the worker loop ends
        # self.worker.finished.connect(self.thread.quit)  # tell the thread it's time to stop running
        # self.worker.finished.connect(self.worker.deleteLater)  # have worker mark itself for deletion
        # self.thread.finished.connect(self.thread.deleteLater)  # have thread mark itself for deletion
        # self.thread.start()

    def stop_loop(self):
        self.worker.working = False

