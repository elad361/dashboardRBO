from typing import Text
from qt_core import *

from gui.uis.windows.main_window.ui_main import *

file_name = None


class Files():
    def __init__(self):
        super().__init__()

        self.ui = UI_MainWindow()
        self.ui.setup_ui()
    ###########################################################
    ## File utility function
    ###########################################################
    def new(self):
        global file_name

        self.ui.load_pages.text_edit.setPlainText("")
        self.ui.title_bar.set_title("New file")
        file_name = None

    def load(self):
        global file_name

        dlg_file = QFileDialog.getOpenFileName(
            parent=self,
            caption=self.tr("Select a file"),
            filter=self.tr("Text files (*.txt)")
        )

        if dlg_file:
            file = open(dlg_file[0], encoding="utf 8")
            text = file.read()
            file.close()

            self.ui.load_pages.text_edit.setPlainText(text)
            file_name = dlg_file[0]
            self.ui.title_bar.set_title(file_name)

    def save(self):
        global file_name

        def write_text(self, file):
            print("saved in folder:" + file)
            file = open(file, "w")
            file.write(self.ui.load_pages.text_edit.toPlainText())

        if file_name:
            write_text(self, file_name)
            self.ui.title_bar.set_title(file_name)
        else:
            dlg_file = QFileDialog.getSaveFileName(
                parent=self,
                caption=self.tr("Select a file"),
                filter=self.tr("Text files (*.txt)")
            )

            if dlg_file:
                write_text(self, dlg_file[0])

                file_name = dlg_file[0]
                self.ui.title_bar.set_title(file_name)
