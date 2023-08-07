# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from gui.core.functions import Functions
from gui.widgets.py_table_widget.py_table_widget import PyTableWidget
# IMPORT MAIN WINDOW PAGES / AND SIDE BOXES FOR APP
# ///////////////////////////////////////////////////////////////
from gui.uis.screens.ui_ser_screen import Ui_serScreen

from src.Services.FilesSrv import pcapFileSrv
from src.Services.FilesSrv.excelFileSrv import ExcelFilesSrv
from src.Services.FilesSrv.pcapFileSrv import pcapFilesSrv
from src.Services.FilesSrv.textFileSrv import Files
from src.Services.UserProcSrv.ProcProgSrv import ProcProgSrv
from . functions_main_window import *
import sys
import os
import pandas as pd

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////
from gui.core.json_themes import Themes

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *

# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
from . ui_main import *

# MAIN FUNCTIONS 
# ///////////////////////////////////////////////////////////////
from . functions_main_window import *


from src.services_core import *


# PY WINDOW
# ///////////////////////////////////////////////////////////////
class SetupMainWindow:
    def __init__(self):
        super().__init__()
        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

    # ADD LEFT MENUS
    # ///////////////////////////////////////////////////////////////
    add_left_menus = [
        {
            "btn_icon" : "icon_home.svg",
            "btn_id" : "btn_home",
            "btn_text" : "Home",
            "btn_tooltip" : "Home page",
            "show_top" : True,
            "is_active" : True
        },
        {
            "btn_icon": "icon_arrow_left.svg",
            "btn_id": "btn_eth",
            "btn_text": "Ethernet",
            "btn_tooltip": "Eth page",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "icon_arrow_right.svg",
            "btn_id": "btn_ser",
            "btn_text": "Serial",
            "btn_tooltip": "Serial page",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "icon_attachment.svg",
            "btn_id": "btn_ftp",
            "btn_text": "Ftp",
            "btn_tooltip": "FTP page",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon" : "icon_widgets.svg",
            "btn_id" : "btn_widgets",
            "btn_text" : "Show Custom Widgets",
            "btn_tooltip" : "Show custom widgets",
            "show_top" : True,
            "is_active" : False
        },
        #rfrog
        # {
        #     "btn_icon" : "icon_add_user.svg",
        #     "btn_id" : "btn_add_user",
        #     "btn_text" : "Add Users",
        #     "btn_tooltip" : "Add users",
        #     "show_top" : True,
        #     "is_active" : False
        # },
        {
            "btn_icon" : "icon_file.svg",
            "btn_id" : "btn_new_file",
            "btn_text" : "New File",
            "btn_tooltip" : "Create new file",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "icon_folder_open.svg",
            "btn_id" : "btn_open_file",
            "btn_text" : "Open File",
            "btn_tooltip" : "Open file",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "icon_save.svg",
            "btn_id" : "btn_save",
            "btn_text" : "Save File",
            "btn_tooltip" : "Save file",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "icon_info.svg",
            "btn_id" : "btn_info",
            "btn_text" : "Information",
            "btn_tooltip" : "Open informations",
            "show_top" : False,
            "is_active" : False
        },
        {
            "btn_icon" : "icon_settings.svg",
            "btn_id" : "btn_settings",
            "btn_text" : "Settings",
            "btn_tooltip" : "Open settings",
            "show_top" : False,
            "is_active" : False
        }
    ]

     # ADD TITLE BAR MENUS
    # ///////////////////////////////////////////////////////////////
    add_title_bar_menus = [
        {
            "btn_icon" : "icon_search.svg",
            "btn_id" : "btn_search",
            "btn_tooltip" : "Search",
            "is_active" : False
        },
        {
            "btn_icon" : "icon_settings.svg",
            "btn_id" : "btn_top_settings",
            "btn_tooltip" : "Top settings",
            "is_active" : False
        }
    ]

    # SETUP CUSTOM BTNs OF CUSTOM WIDGETS
    # Get sender() function when btn is clicked
    # ///////////////////////////////////////////////////////////////
    def setup_btns(self):
        if self.ui.title_bar.sender() != None:
            return self.ui.title_bar.sender()
        elif self.ui.left_menu.sender() != None:
            return self.ui.left_menu.sender()
        elif self.ui.left_column.sender() != None:
            return self.ui.left_column.sender()

    # SETUP MAIN WINDOW WITH CUSTOM PARAMETERS
    # ///////////////////////////////////////////////////////////////
    def setup_gui(self):
        # APP TITLE
        # ///////////////////////////////////////////////////////////////
        self.setWindowTitle(self.settings["app_name"])
        
        # REMOVE TITLE BAR
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

        # ADD GRIPS
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.left_grip = PyGrips(self, "left", self.hide_grips)
            self.right_grip = PyGrips(self, "right", self.hide_grips)
            self.top_grip = PyGrips(self, "top", self.hide_grips)
            self.bottom_grip = PyGrips(self, "bottom", self.hide_grips)
            self.top_left_grip = PyGrips(self, "top_left", self.hide_grips)
            self.top_right_grip = PyGrips(self, "top_right", self.hide_grips)
            self.bottom_left_grip = PyGrips(self, "bottom_left", self.hide_grips)
            self.bottom_right_grip = PyGrips(self, "bottom_right", self.hide_grips)

        # LEFT MENUS / GET SIGNALS WHEN LEFT MENU BTN IS CLICKED / RELEASED
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.left_menu.add_menus(SetupMainWindow.add_left_menus)

        # SET SIGNALS
        self.ui.left_menu.clicked.connect(self.btn_clicked)
        self.ui.left_menu.released.connect(self.btn_released)

        # TITLE BAR / ADD EXTRA BUTTONS
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.title_bar.add_menus(SetupMainWindow.add_title_bar_menus)

        # SET SIGNALS
        self.ui.title_bar.clicked.connect(self.btn_clicked)
        self.ui.title_bar.released.connect(self.btn_released)

        # ADD Title
        if self.settings["custom_title_bar"]:
            self.ui.title_bar.set_title(self.settings["app_name"])
        else:
            self.ui.title_bar.set_title("Welcome to PyOneDark")

        # LEFT COLUMN SET SIGNALS
        # ///////////////////////////////////////////////////////////////
        self.ui.left_column.clicked.connect(self.btn_clicked)
        self.ui.left_column.released.connect(self.btn_released)

        # SET INITIAL PAGE / SET LEFT AND RIGHT COLUMN MENUS
        # ///////////////////////////////////////////////////////////////
        #MainFunctions.set_page(self, self.ui.load_pages.page_1)
        MainFunctions.set_page(self, self.ui.load_pages.pageP0Main)
        MainFunctions.set_left_column_menu(
            self,
            menu = self.ui.left_column.menus.menu_1,
            title = "Settings Left Column",
            icon_path = Functions.set_svg_icon("icon_settings.svg")
        )
        MainFunctions.set_right_column_menu(self, self.ui.right_column.menu_1)

        # ///////////////////////////////////////////////////////////////
        # EXAMPLE CUSTOM WIDGETS
        # Here are added the custom widgets to pages and columns that
        # were created using Qt Designer.
        # This is just an example and should be deleted when creating
        # your application.
        #
        # OBJECTS FOR LOAD PAGES, LEFT AND RIGHT COLUMNS
        # You can access objects inside Qt Designer projects using
        # the objects below:
        #
        # <OBJECTS>
        # LEFT COLUMN: self.ui.left_column.menus
        # RIGHT COLUMN: self.ui.right_column
        # LOAD PAGES: self.ui.load_pages
        # </OBJECTS>
        # ///////////////////////////////////////////////////////////////

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        # ///////////////////////////////////////////////////////////////
        # ///////////////////////////////////////////////////////////////
        # LEFT COLUMN
        # ///////////////////////////////////////////////////////////////
        # ///////////////////////////////////////////////////////////////

        self.text_size_slider = PySlider(
            bg_color=self.themes["app_color"]["dark_one"],
            handle_color=self.themes["app_color"]["icon_color"],
            handle_color_hover=self.themes["app_color"]["icon_hover"],
            handle_color_pressed=self.themes["app_color"]["icon_pressed"],
        )

        self.text_size_slider.setRange(9,38)
        self.text_size_slider.setOrientation(Qt.Orientation.Horizontal)
        def update_label():
            value = self.text_size_slider.value()
            self.ui.left_column.menus.label_1.setText("Size: " + str(value))
            self.ui.load_pages.page_1.setStyleSheet(f"font-size: {value}pt")

        self.text_size_slider.valueChanged.connect(update_label)
        self.text_size_slider.setValue(14)
        self.ui.left_column.menus.btn_2_layout.addWidget(self.text_size_slider)
        # BTN 1
        # self.left_btn_1 = PyPushButton(
        #     text="Btn 1",
        #     radius=8,
        #     color=self.themes["app_color"]["text_foreground"],
        #     bg_color=self.themes["app_color"]["dark_one"],
        #     bg_color_hover=self.themes["app_color"]["dark_three"],
        #     bg_color_pressed=self.themes["app_color"]["dark_four"]
        # )
        # self.left_btn_1.setMaximumHeight(40)
        # self.ui.left_column.menus.btn_1_layout.addWidget(self.left_btn_1)

        # BTN 2
        # self.left_btn_2 = PyPushButton(
        #     text="Btn With Icon",
        #     radius=8,
        #     color=self.themes["app_color"]["text_foreground"],
        #     bg_color=self.themes["app_color"]["dark_one"],
        #     bg_color_hover=self.themes["app_color"]["dark_three"],
        #     bg_color_pressed=self.themes["app_color"]["dark_four"]
        # )
        # self.icon = QIcon(Functions.set_svg_icon("icon_settings.svg"))
        # self.left_btn_2.setIcon(self.icon)
        # self.left_btn_2.setMaximumHeight(40)
        # self.ui.left_column.menus.btn_2_layout.addWidget(self.left_btn_2)

        # BTN 3 - Default QPushButton
        # self.left_btn_3 = QPushButton("Default QPushButton")
        # self.left_btn_3.setMaximumHeight(40)
        # self.ui.left_column.menus.btn_3_layout.addWidget(self.left_btn_3)

        # ///////////////////////////////////////////////////////////////
        # ///////////////////////////////////////////////////////////////
        # PAGES //#rbo
        # ///////////////////////////////////////////////////////////////
        # ///////////////////////////////////////////////////////////////
        # ****************************************************************
        # PAGE Serial - screen to page
        # ****************************************************************
        #Ui_serScreen.setupUi()
        #self.serScreen = PySerialScrn(
        #    bg_two=self.themes["app_color"]["bg_two"],
        #    copyright=self.settings["copyright"],
        #    version=self.settings["version"],
        #    font_family=self.settings["font"]["family"],
        #    text_size=self.settings["font"]["text_size"],
        #    text_description_color=self.themes["app_color"]["text_description"]
        #)

        self.uiSerScreen  = Ui_serScreen(
            bg_two=self.themes["app_color"]["bg_two"],
            copyright=self.settings["copyright"],
            version=self.settings["version"],
            font_family=self.settings["font"]["family"],
            text_size=self.settings["font"]["text_size"],
            text_description_color=self.themes["app_color"]["text_description"]
        )

        self.ui.load_pages.pageSer_contLyt.addWidget(self.uiSerScreen)

        #****************************************************************
        # PAGE 1 - ADD LOGO TO MAIN PAGE
        #****************************************************************
        #self.logo_svg = QSvgWidget(Functions.set_svg_image("logo_home.svg"))
        #self.ui.load_pages.logo_layout.addWidget(self.logo_svg, Qt.AlignCenter, Qt.AlignCenter)
        # Program Process Button
        self.prog_proc_ipbtn = PyPushButton(
            text="Program",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.prog_proc_ipbtn_icon = QIcon(Functions.set_svg_icon("icon_settings.svg"))
        self.prog_proc_ipbtn.setMinimumHeight(100)
        self.prog_proc_ipbtn.setIcon(self.prog_proc_ipbtn_icon)
        def prog_proc_ipbtn_clicked():
            print("prog_proc_ipbtn_clicked")
            MainFunctions.set_page(self, self.ui.load_pages.pageP1Prog)
            #pcapFilesSrv.load(self)

        self.prog_proc_ipbtn.clicked.connect(prog_proc_ipbtn_clicked)
        self.ui.load_pages.pageP0Main_gLyt.addWidget(self.prog_proc_ipbtn, 0, 0)

        # Verify Process Button
        self.verify_proc_ipbtn = PyPushButton(
            text="Verify",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.verify_proc_ipbtn_icon = QIcon(Functions.set_svg_icon("icon_settings.svg"))
        self.verify_proc_ipbtn.setMinimumHeight(100)
        self.verify_proc_ipbtn.setIcon(self.prog_proc_ipbtn_icon)
        def verify_proc_ipbtn_clicked():
            print("verify_proc_ipbtn_clicked")
            MainFunctions.set_page(self, self.ui.load_pages.pageP4Verify)
            # pcapFilesSrv.load(self)

        self.verify_proc_ipbtn.clicked.connect(verify_proc_ipbtn_clicked)
        self.ui.load_pages.pageP0Main_gLyt.addWidget(self.verify_proc_ipbtn, 0, 1)

        # Back Process Button
        self.back_proc_ipbtn = PyPushButton(
            text="Backup",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.back_proc_ipbtn_icon = QIcon(Functions.set_svg_icon("icon_settings.svg"))
        self.back_proc_ipbtn.setMinimumHeight(100)
        self.back_proc_ipbtn.setIcon(self.prog_proc_ipbtn_icon)
        def back_proc_ipbtn_clicked():
            print("back_proc_ipbtn_clicked")
            MainFunctions.set_page(self, self.ui.load_pages.pageP2Back)
            # pcapFilesSrv.load(self)

        self.back_proc_ipbtn.clicked.connect(back_proc_ipbtn_clicked)
        self.ui.load_pages.pageP0Main_gLyt.addWidget(self.back_proc_ipbtn, 1, 0)

        # Restore Process Button
        self.restore_proc_ipbtn = PyPushButton(
            text="Restore",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.restore_proc_ipbtn_icon = QIcon(Functions.set_svg_icon("icon_settings.svg"))
        self.restore_proc_ipbtn.setMinimumHeight(100)
        self.restore_proc_ipbtn.setIcon(self.prog_proc_ipbtn_icon)
        def restore_proc_ipbtn_clicked():
            print("restore_proc_ipbtn_clicked")
            MainFunctions.set_page(self, self.ui.load_pages.pageP3Restore)
            # pcapFilesSrv.load(self)

        self.restore_proc_ipbtn.clicked.connect(restore_proc_ipbtn_clicked)
        self.ui.load_pages.pageP0Main_gLyt.addWidget(self.restore_proc_ipbtn, 1, 1)

        self.logo_svg = QSvgWidget(Functions.set_svg_image("logo_home.svg"))
        # self.ui.load_pages.logo_layout.addWidget(self.logo_svg, Qt.AlignCenter, Qt.AlignCenter)
        self.ui.load_pages.pageP0MainLogo_lyt.addWidget(self.logo_svg, Qt.AlignCenter, Qt.AlignCenter)

        # ****************************************************************
        #ELAD pageP1Prog  PAGE - programming task
        # ****************************************************************
        # PY LINE EDIT
        self.elad_task = PyLineEdit(
            text = "",
            place_holder_text="elad page",
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]
        )


        self.elad_task.setMinimumHeight(30)
        self.ui.load_pages.pageP2Back_r1Lyt.addWidget(self.elad_task)
        #****************************************************************
        #pageP1Prog  PAGE - programming task
        #****************************************************************



        # TABLE WIDGETS
        self.prog_task_table_widget = PyTableWidget(
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["context_color"],
            bg_color=self.themes["app_color"]["bg_two"],
            header_horizontal_color=self.themes["app_color"]["dark_two"],
            header_vertical_color=self.themes["app_color"]["bg_three"],
            bottom_line_color=self.themes["app_color"]["bg_three"],
            grid_line_color=self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color=self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color=self.themes["app_color"]["dark_four"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.prog_task_table_widget.setColumnCount(3)
        self.prog_task_table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.prog_task_table_widget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.prog_task_table_widget.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Columns / Header
        self.column_1 = QTableWidgetItem()
        self.column_1.setTextAlignment(Qt.AlignCenter)
        self.column_1.setText("NAME")

        self.column_2 = QTableWidgetItem()
        self.column_2.setTextAlignment(Qt.AlignCenter)
        self.column_2.setText("NICK")

        self.column_3 = QTableWidgetItem()
        self.column_3.setTextAlignment(Qt.AlignCenter)
        self.column_3.setText("PASS")

        # Set column
        self.prog_task_table_widget.setHorizontalHeaderItem(0, self.column_1)
        self.prog_task_table_widget.setHorizontalHeaderItem(1, self.column_2)
        self.prog_task_table_widget.setHorizontalHeaderItem(2, self.column_3)

        #load the process steps from excel
        self.prog_proc_df = pd.DataFrame(ExcelFilesSrv(self).load('prog_proc_db'))

        # Id,Name,Description,Action,Ref
        #for x in range(10):
        for index, row in self.prog_proc_df.iterrows():
            row_number = self.prog_task_table_widget.rowCount()
            self.prog_task_table_widget.insertRow(row_number)  # Insert row
            self.prog_task_table_widget.setItem(row_number, 0, QTableWidgetItem(row['Id']))  # Add name
            self.prog_task_table_widget.setItem(row_number, 1, QTableWidgetItem(row['Name']))  # Add nick
            self.pass_text = QTableWidgetItem()
            self.pass_text.setTextAlignment(Qt.AlignCenter)
            #self.pass_text.setText("12345" + str(x))
            self.prog_task_table_widget.setItem(row_number, 2, QTableWidgetItem(row['Action']))  # Add pass

        self.prog_task_table_widget.selectRow(2);
        self.ui.load_pages.pageP1Prog_r3Lyt.addWidget(self.prog_task_table_widget)

        # PY LINE EDIT
        self.prog_task_line_edit = PyLineEdit(
            text = "",
            place_holder_text="prog_task_line_edit place holder text",
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]
        )


        self.prog_task_line_edit.setMinimumHeight(30)
        self.ui.load_pages.pageP1Prog_r5Lyt.addWidget(self.prog_task_line_edit)

        self.prog_task_label_status = PyLabel(
            text="",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.ui.load_pages.pageP1Prog_r4Lyt.addWidget(self.prog_task_label_status)


        # TOGGLE BUTTON
        self.prog_task_toggle_button = PyToggle(
            width=50,
            bg_color=self.themes["app_color"]["dark_two"],
            circle_color=self.themes["app_color"]["icon_color"],
            active_color=self.themes["app_color"]["context_color"]
        )



        self.ui.load_pages.pageP1Prog_r1Lyt.addWidget(self.prog_task_toggle_button)

        self.proc_prog_srv =  ProcProgSrv(self)


        # ****************************************************************
        # PAGE 2
        # ****************************************************************
        # CIRCULAR PROGRESS 1
        self.circular_progress_1 = PyCircularProgress(
            value = 80,
            progress_color = self.themes["app_color"]["context_color"],
            text_color = self.themes["app_color"]["text_title"],
            font_size = 14,
            bg_color = self.themes["app_color"]["dark_four"]
        )
        self.circular_progress_1.setFixedSize(200,200)

        # CIRCULAR PROGRESS 2
        self.circular_progress_2 = PyCircularProgress(
            value = 45,
            progress_width = 4,
            progress_color = self.themes["app_color"]["context_color"],
            text_color = self.themes["app_color"]["context_color"],
            font_size = 14,
            bg_color = self.themes["app_color"]["bg_three"]
        )
        self.circular_progress_2.setFixedSize(160,160)

        # CIRCULAR PROGRESS 3
        self.circular_progress_3 = PyCircularProgress(
            value = 75,
            progress_width = 2,
            progress_color = self.themes["app_color"]["pink"],
            text_color = self.themes["app_color"]["white"],
            font_size = 14,
            bg_color = self.themes["app_color"]["bg_three"]
        )
        self.circular_progress_3.setFixedSize(140,140)

        # PY SLIDER 1
        self.vertical_slider_1 = PySlider(
            margin=8,
            bg_size=10,
            bg_radius=5,
            handle_margin=-3,
            handle_size=16,
            handle_radius=8,
            bg_color = self.themes["app_color"]["dark_three"],
            bg_color_hover = self.themes["app_color"]["dark_four"],
            handle_color = self.themes["app_color"]["context_color"],
            handle_color_hover = self.themes["app_color"]["context_hover"],
            handle_color_pressed = self.themes["app_color"]["context_pressed"]
        )
        self.vertical_slider_1.setMinimumHeight(100)

        # PY SLIDER 2
        self.vertical_slider_2 = PySlider(
            bg_color = self.themes["app_color"]["dark_three"],
            bg_color_hover = self.themes["app_color"]["dark_three"],
            handle_color = self.themes["app_color"]["context_color"],
            handle_color_hover = self.themes["app_color"]["context_hover"],
            handle_color_pressed = self.themes["app_color"]["context_pressed"]
        )
        self.vertical_slider_2.setMinimumHeight(100)

        # PY SLIDER 3
        self.vertical_slider_3 = PySlider(
            margin=8,
            bg_size=10,
            bg_radius=5,
            handle_margin=-3,
            handle_size=16,
            handle_radius=8,
            bg_color = self.themes["app_color"]["dark_three"],
            bg_color_hover = self.themes["app_color"]["dark_four"],
            handle_color = self.themes["app_color"]["context_color"],
            handle_color_hover = self.themes["app_color"]["context_hover"],
            handle_color_pressed = self.themes["app_color"]["context_pressed"]
        )
        self.vertical_slider_3.setOrientation(Qt.Horizontal)
        self.vertical_slider_3.setMaximumWidth(200)

        # PY SLIDER 4
        self.vertical_slider_4 = PySlider(
            bg_color = self.themes["app_color"]["dark_three"],
            bg_color_hover = self.themes["app_color"]["dark_three"],
            handle_color = self.themes["app_color"]["context_color"],
            handle_color_hover = self.themes["app_color"]["context_hover"],
            handle_color_pressed = self.themes["app_color"]["context_pressed"]
        )
        self.vertical_slider_4.setOrientation(Qt.Horizontal)
        self.vertical_slider_4.setMaximumWidth(200)

        # ICON BUTTON 1
        self.icon_button_1 = PyIconButton(
            icon_path = Functions.set_svg_icon("icon_heart.svg"),
            parent = self,
            app_parent = self.ui.central_widget,
            tooltip_text = "Icon button - Heart",
            width = 40,
            height = 40,
            radius = 20,
            dark_one = self.themes["app_color"]["dark_one"],
            icon_color = self.themes["app_color"]["icon_color"],
            icon_color_hover = self.themes["app_color"]["icon_hover"],
            icon_color_pressed = self.themes["app_color"]["icon_active"],
            icon_color_active = self.themes["app_color"]["icon_active"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_hover = self.themes["app_color"]["dark_three"],
            bg_color_pressed = self.themes["app_color"]["pink"]
        )

        # ICON BUTTON 2
        self.icon_button_2 = PyIconButton(
            icon_path = Functions.set_svg_icon("icon_add_user.svg"),
            parent = self,
            app_parent = self.ui.central_widget,
            tooltip_text = "BTN with tooltip",
            width = 40,
            height = 40,
            radius = 8,
            dark_one = self.themes["app_color"]["dark_one"],
            icon_color = self.themes["app_color"]["icon_color"],
            icon_color_hover = self.themes["app_color"]["icon_hover"],
            icon_color_pressed = self.themes["app_color"]["white"],
            icon_color_active = self.themes["app_color"]["icon_active"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_hover = self.themes["app_color"]["dark_three"],
            bg_color_pressed = self.themes["app_color"]["green"],
        )

        # ICON BUTTON 3
        self.icon_button_3 = PyIconButton(
            icon_path = Functions.set_svg_icon("icon_add_user.svg"),
            parent = self,
            app_parent = self.ui.central_widget,
            tooltip_text = "BTN actived! (is_actived = True)",
            width = 40,
            height = 40,
            radius = 8,
            dark_one = self.themes["app_color"]["dark_one"],
            icon_color = self.themes["app_color"]["icon_color"],
            icon_color_hover = self.themes["app_color"]["icon_hover"],
            icon_color_pressed = self.themes["app_color"]["white"],
            icon_color_active = self.themes["app_color"]["icon_active"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_hover = self.themes["app_color"]["dark_three"],
            bg_color_pressed = self.themes["app_color"]["context_color"],
            is_active = True
        )

        # PUSH BUTTON 1
        self.push_button_1 = PyPushButton(
            text = "Button Without Icon",
            radius  =8,
            color = self.themes["app_color"]["text_foreground"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_hover = self.themes["app_color"]["dark_three"],
            bg_color_pressed = self.themes["app_color"]["dark_four"]
        )
        self.push_button_1.setMinimumHeight(40)

        def push_button_1_clicked():
            #print(self.line_edit.text())
            pcapFilesSrv.load(self)

        self.push_button_1.clicked.connect(push_button_1_clicked)

        # PUSH BUTTON 2
        self.push_button_2 = PyPushButton(
            text = "Button With Icon",
            radius = 8,
            color = self.themes["app_color"]["text_foreground"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_hover = self.themes["app_color"]["dark_three"],
            bg_color_pressed = self.themes["app_color"]["dark_four"]
        )
        self.icon_2 = QIcon(Functions.set_svg_icon("icon_settings.svg"))
        self.push_button_2.setMinimumHeight(40)
        self.push_button_2.setIcon(self.icon_2)

        # PY LINE EDIT
        # self.line_edit = PyLineEdit(
        #     text = "",
        #     place_holder_text = "Place holder text",
        #     radius = 8,
        #     border_size = 2,
        #     color = self.themes["app_color"]["text_foreground"],
        #     selection_color = self.themes["app_color"]["white"],
        #     bg_color = self.themes["app_color"]["dark_one"],
        #     bg_color_active = self.themes["app_color"]["dark_three"],
        #     context_color = self.themes["app_color"]["context_color"]
        # )
        # self.line_edit.setMinimumHeight(30)

        # TOGGLE BUTTON
        self.toggle_button = PyToggle(
            width = 50,
            bg_color = self.themes["app_color"]["dark_two"],
            circle_color = self.themes["app_color"]["icon_color"],
            active_color = self.themes["app_color"]["context_color"]
        )

        # TABLE WIDGETS
        self.table_widget = PyTableWidget(
            radius = 8,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["context_color"],
            bg_color = self.themes["app_color"]["bg_two"],
            header_horizontal_color = self.themes["app_color"]["dark_two"],
            header_vertical_color = self.themes["app_color"]["bg_three"],
            bottom_line_color = self.themes["app_color"]["bg_three"],
            grid_line_color = self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color = self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color = self.themes["app_color"]["dark_four"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.table_widget.setColumnCount(3)
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_widget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_widget.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Columns / Header
        self.column_1 = QTableWidgetItem()
        self.column_1.setTextAlignment(Qt.AlignCenter)
        self.column_1.setText("NAME")

        self.column_2 = QTableWidgetItem()
        self.column_2.setTextAlignment(Qt.AlignCenter)
        self.column_2.setText("NICK")

        self.column_3 = QTableWidgetItem()
        self.column_3.setTextAlignment(Qt.AlignCenter)
        self.column_3.setText("PASS")

        # Set column
        self.table_widget.setHorizontalHeaderItem(0, self.column_1)
        self.table_widget.setHorizontalHeaderItem(1, self.column_2)
        self.table_widget.setHorizontalHeaderItem(2, self.column_3)

        for x in range(10):
            row_number = self.table_widget.rowCount()
            self.table_widget.insertRow(row_number) # Insert row
            self.table_widget.setItem(row_number, 0, QTableWidgetItem(str("Wanderson"))) # Add name
            self.table_widget.setItem(row_number, 1, QTableWidgetItem(str("vfx_on_fire_" + str(x)))) # Add nick
            self.pass_text = QTableWidgetItem()
            self.pass_text.setTextAlignment(Qt.AlignCenter)
            self.pass_text.setText("12345" + str(x))
            self.table_widget.setItem(row_number, 2, self.pass_text) # Add pass
            self.table_widget.setRowHeight(row_number, 22)


        # ADD WIDGETS #rbo

        #self.ui.load_pages.row_1_layout.addWidget(self.circular_progress_1)
        #self.ui.load_pages.row_1_layout.addWidget(self.circular_progress_2)
        #self.ui.load_pages.row_1_layout.addWidget(self.circular_progress_3)
        #self.ui.load_pages.row_2_layout.addWidget(self.vertical_slider_1)
        #self.ui.load_pages.row_2_layout.addWidget(self.vertical_slider_2)
        #self.ui.load_pages.row_2_layout.addWidget(self.vertical_slider_3)
        #self.ui.load_pages.row_2_layout.addWidget(self.vertical_slider_4)
        #self.ui.load_pages.row_3_layout.addWidget(self.icon_button_1)
        #self.ui.load_pages.row_3_layout.addWidget(self.icon_button_2)
        #self.ui.load_pages.row_3_layout.addWidget(self.icon_button_3)
        self.ui.load_pages.row_3_layout.addWidget(self.push_button_1)
        self.ui.load_pages.row_3_layout.addWidget(self.push_button_2)
        self.ui.load_pages.row_3_layout.addWidget(self.toggle_button)
        #self.ui.load_pages.row_4_layout.addWidget(self.line_edit)
        self.ui.load_pages.row_5_layout.addWidget(self.table_widget)

        # ****************************************************************
        # PAGE xxx - insert new page
        # ****************************************************************

        # ///////////////////////////////////////////////////////////////
        # ///////////////////////////////////////////////////////////////
        # RIGHT COLUMN
        # ///////////////////////////////////////////////////////////////
        # ///////////////////////////////////////////////////////////////

        # BTN 1
        self.right_btn_1 = PyPushButton(
            text="Show Menu 2",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon_right = QIcon(Functions.set_svg_icon("icon_arrow_right.svg"))
        self.right_btn_1.setIcon(self.icon_right)
        self.right_btn_1.setMaximumHeight(40)
        self.right_btn_1.clicked.connect(lambda: MainFunctions.set_right_column_menu(
            self,
            self.ui.right_column.menu_2
        ))
        self.ui.right_column.btn_1_layout.addWidget(self.right_btn_1)

        # BTN 2
        self.right_btn_2 = PyPushButton(
            text="Show Menu 1",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon_left = QIcon(Functions.set_svg_icon("icon_arrow_left.svg"))
        self.right_btn_2.setIcon(self.icon_left)
        self.right_btn_2.setMaximumHeight(40)
        self.right_btn_2.clicked.connect(lambda: MainFunctions.set_right_column_menu(
            self,
            self.ui.right_column.menu_1
        ))
        self.ui.right_column.btn_2_layout.addWidget(self.right_btn_2)

        # ///////////////////////////////////////////////////////////////
        # END - EXAMPLE CUSTOM WIDGETS
        # ///////////////////////////////////////////////////////////////

    # RESIZE GRIPS AND CHANGE POSITION
    # Resize or change position when window is resized
    # ///////////////////////////////////////////////////////////////
    def resize_grips(self):
        if self.settings["custom_title_bar"]:
            self.left_grip.setGeometry(5, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 15, 10, 10, self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(5, self.height() - 15, self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(self.width() - 20, self.height() - 20, 15, 15)