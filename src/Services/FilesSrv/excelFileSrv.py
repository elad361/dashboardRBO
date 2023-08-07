from typing import Text
import pandas as pd
import os

from qt_core import *

from gui.uis.windows.main_window.ui_main import *

file_name = None


class ExcelFilesSrv():
    def __init__(self, parent_ui):
        super().__init__()
        self.ui = parent_ui


    ###########################################################
    ## Service Utility functions
    ###########################################################



    ###########################################################
    ## File utility functions
    ###########################################################
    def new(self):
        global file_name

        self.ui.load_pages.text_edit.setPlainText("")
        self.ui.title_bar.set_title("New file")
        file_name = None

    def load(self,db_name):

        df_sheet_all = pd.read_excel("D:\\dashboardRBO\\data\\proc_db.xlsx", sheet_name=None)
        print(df_sheet_all)
        return df_sheet_all[db_name]
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
