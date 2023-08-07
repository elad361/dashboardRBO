#GUI interactions
from PySide6.QtCore import QThread, Signal, Slot
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget

# MULTI-THREADING

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

class ProcManagerCls(Qwidget):
    def __init__(self):

        QMainWindow.__init__(self)
        loadUi('qt.ui', self)

        self.thread = None
        self.worker = None
        self.pushButton.clicked.connect(self.start_loop)
        self.pushBtnClicked = False
        self.CopyFlag = 0

    def loop_finished(self):
        print('Loop Finished')

    def start_loop(self):
        s
        #Verify the correct COM Port
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

        self.worker = ProcWorker()   # a new worker to perform those tasks
        self.thread = QThread()  # a new thread to run our background tasks in
        self.worker.moveToThread(self.thread)  # move the worker into the thread, do this first before connecting the signals

        self.thread.started.connect(self.worker.work) # begin our worker object's loop when the thread starts running

        self.worker.intReady.connect(self.onIntReady)

        self.pushButton_2.clicked.connect(self.stop_loop)      # stop the loop on the stop button click

        self.worker.finished.connect(self.loop_finished)       # do something in the gui when the worker loop ends
        self.worker.finished.connect(self.thread.quit)         # tell the thread it's time to stop running
        self.worker.finished.connect(self.worker.deleteLater)  # have worker mark itself for deletion
        self.thread.finished.connect(self.thread.deleteLater)  # have thread mark itself for deletion
        self.thread.start()

    def stop_loop(self):
        self.worker.working = False







"""
    def onIntReady(self, i):
        if i != '':
            self.textEdit_3.append("{}".format(i))
            print(i)
            if i.find('CINE Frames') != -1:
                #IQ file stored make beep
                winsound.Beep(1740, 800)

            if self.ck_AuSC.isChecked():
                #Auto Copy files
                if i.find('io copy j:') != -1:
                    #First autocopy condition
                    self.CopyFlag = 1

                if i.find('nvdbg>') != -1 and self.CopyFlag == 1:
                    count = self.sb_Num.value()
                    if count < 10:
                        numb = '0' + str(count)
                    else:
                        numb = str(count)

                    mytext = "io copy j:" + self.txtIQfile.toPlainText() + numb + ".iq " + self.cb_Drive.currentText() + "\n"
                    ser.write(mytext.encode())

                    #Check for final file copy
                    if count == self.sb_NumFin.value():
                        self.ck_AuSC.setCheckState(False)
                        self.sb_NumFin.setEnabled(False)
                        self.CopyFlag = 0
                        mytext = "\n"       #Clear buffer
                        ser.write(mytext.encode())
                    else:
                        self.sb_Num.setValue(count + 1)


    # TXT Save
    def on_pushButton_5_clicked(self):
        if self.pushBtnClicked:
            self.pushBtnClicked = False
            return

        fileName = QFileDialog.getSaveFileName(self, 'Select location to Log', "", '*.txt')
        if not fileName:
            return

        with open(fileName[0], 'w') as f:
            my_text = self.textEdit_3.toPlainText()
            f.write(my_text)

        self.textEdit_3.append("Log Saved in :" + fileName[0] + "\r\n")
        self.pushBtnClicked = True
"""




