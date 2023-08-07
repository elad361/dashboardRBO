# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pageslILyrr.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *

class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(860, 668)
        self.verticalLayout_2 = QVBoxLayout(MainPages)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"font-size: 14pt")
        self.page_1_layout = QVBoxLayout(self.page_1)
        self.page_1_layout.setSpacing(5)
        self.page_1_layout.setObjectName(u"page_1_layout")
        self.page_1_layout.setContentsMargins(5, 5, 5, 5)
        self.text_edit = QPlainTextEdit(self.page_1)
        self.text_edit.setObjectName(u"text_edit")

        self.page_1_layout.addWidget(self.text_edit)

        self.pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2_layout = QVBoxLayout(self.page_2)
        self.page_2_layout.setSpacing(5)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.page_2_layout.setContentsMargins(5, 5, 5, 5)
        self.scroll_area = QScrollArea(self.page_2)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setStyleSheet(u"background: transparent;")
        self.scroll_area.setFrameShape(QFrame.NoFrame)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.contents = QWidget()
        self.contents.setObjectName(u"contents")
        self.contents.setGeometry(QRect(0, 0, 214, 266))
        self.contents.setStyleSheet(u"background: transparent;")
        self.verticalLayout = QVBoxLayout(self.contents)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.title_label = QLabel(self.contents)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(16)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(u"font-size: 16pt")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title_label)

        self.description_label = QLabel(self.contents)
        self.description_label.setObjectName(u"description_label")
        self.description_label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.description_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.description_label)

        self.row_1_layout = QHBoxLayout()
        self.row_1_layout.setObjectName(u"row_1_layout")

        self.verticalLayout.addLayout(self.row_1_layout)

        self.row_2_layout = QHBoxLayout()
        self.row_2_layout.setObjectName(u"row_2_layout")

        self.verticalLayout.addLayout(self.row_2_layout)

        self.row_3_layout = QHBoxLayout()
        self.row_3_layout.setObjectName(u"row_3_layout")

        self.verticalLayout.addLayout(self.row_3_layout)

        self.row_4_layout = QVBoxLayout()
        self.row_4_layout.setObjectName(u"row_4_layout")

        self.verticalLayout.addLayout(self.row_4_layout)

        self.row_5_layout = QVBoxLayout()
        self.row_5_layout.setObjectName(u"row_5_layout")

        self.verticalLayout.addLayout(self.row_5_layout)

        self.scroll_area.setWidget(self.contents)

        self.page_2_layout.addWidget(self.scroll_area)

        self.pages.addWidget(self.page_2)
        self.pageSer = QWidget()
        self.pageSer.setObjectName(u"pageSer")
        self.pageSer.setStyleSheet(u"QFrame {\n"
"	font-size: 16pt;\n"
"}")
        self.gridLayout = QGridLayout(self.pageSer)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pageSer_scrl = QScrollArea(self.pageSer)
        self.pageSer_scrl.setObjectName(u"pageSer_scrl")
        self.pageSer_scrl.setStyleSheet(u"background: transparent;")
        self.pageSer_scrl.setFrameShape(QFrame.NoFrame)
        self.pageSer_scrl.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.pageSer_scrl.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.pageSer_scrl.setWidgetResizable(True)
        self.pageSer_cont = QWidget()
        self.pageSer_cont.setObjectName(u"pageSer_cont")
        self.pageSer_cont.setGeometry(QRect(0, 0, 832, 640))
        self.pageSer_cont.setStyleSheet(u"background: transparent;")
        self.pageSer_contLyt = QVBoxLayout(self.pageSer_cont)
        self.pageSer_contLyt.setSpacing(15)
        self.pageSer_contLyt.setObjectName(u"pageSer_contLyt")
        self.pageSer_contLyt.setContentsMargins(5, 5, 5, 5)
        self.pageSer_scrl.setWidget(self.pageSer_cont)

        self.gridLayout.addWidget(self.pageSer_scrl, 0, 0, 1, 1)

        self.pages.addWidget(self.pageSer)
        self.pageP0Main = QWidget()
        self.pageP0Main.setObjectName(u"pageP0Main")
        self.pageP0Main_lyt = QVBoxLayout(self.pageP0Main)
        self.pageP0Main_lyt.setObjectName(u"pageP0Main_lyt")
        self.pageP0Main_scrl = QScrollArea(self.pageP0Main)
        self.pageP0Main_scrl.setObjectName(u"pageP0Main_scrl")
        self.pageP0Main_scrl.setStyleSheet(u"background: transparent;")
        self.pageP0Main_scrl.setFrameShape(QFrame.NoFrame)
        self.pageP0Main_scrl.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.pageP0Main_scrl.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.pageP0Main_scrl.setWidgetResizable(True)
        self.pageP0Main_cont = QWidget()
        self.pageP0Main_cont.setObjectName(u"pageP0Main_cont")
        self.pageP0Main_cont.setGeometry(QRect(0, 0, 832, 640))
        self.pageP0Main_cont.setStyleSheet(u"background: transparent;")
        self.pageP0Main_contLyt = QVBoxLayout(self.pageP0Main_cont)
        self.pageP0Main_contLyt.setSpacing(15)
        self.pageP0Main_contLyt.setObjectName(u"pageP0Main_contLyt")
        self.pageP0Main_contLyt.setContentsMargins(5, 5, 5, 5)
        self.pageP0Main_tLbl = QLabel(self.pageP0Main_cont)
        self.pageP0Main_tLbl.setObjectName(u"pageP0Main_tLbl")
        self.pageP0Main_tLbl.setMaximumSize(QSize(16777215, 40))
        self.pageP0Main_tLbl.setFont(font)
        self.pageP0Main_tLbl.setStyleSheet(u"font-size: 16pt")
        self.pageP0Main_tLbl.setAlignment(Qt.AlignCenter)

        self.pageP0Main_contLyt.addWidget(self.pageP0Main_tLbl)

        self.pageP0Main_dLbl = QLabel(self.pageP0Main_cont)
        self.pageP0Main_dLbl.setObjectName(u"pageP0Main_dLbl")
        self.pageP0Main_dLbl.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pageP0Main_dLbl.sizePolicy().hasHeightForWidth())
        self.pageP0Main_dLbl.setSizePolicy(sizePolicy)
        self.pageP0Main_dLbl.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.pageP0Main_dLbl.setWordWrap(True)

        self.pageP0Main_contLyt.addWidget(self.pageP0Main_dLbl)

        self.pageP0MainLogo_lyt = QVBoxLayout()
        self.pageP0MainLogo_lyt.setObjectName(u"pageP0MainLogo_lyt")

        self.pageP0Main_contLyt.addLayout(self.pageP0MainLogo_lyt)

        self.pageP0Main_gLyt = QGridLayout()
        self.pageP0Main_gLyt.setObjectName(u"pageP0Main_gLyt")

        self.pageP0Main_contLyt.addLayout(self.pageP0Main_gLyt)

        self.pageP0Main_scrl.setWidget(self.pageP0Main_cont)

        self.pageP0Main_lyt.addWidget(self.pageP0Main_scrl)

        self.pages.addWidget(self.pageP0Main)
        self.pageP4Verify = QWidget()
        self.pageP4Verify.setObjectName(u"pageP4Verify")
        self.pageP4Verify_lyt = QVBoxLayout(self.pageP4Verify)
        self.pageP4Verify_lyt.setObjectName(u"pageP4Verify_lyt")
        self.pageP4Verify_scrl = QScrollArea(self.pageP4Verify)
        self.pageP4Verify_scrl.setObjectName(u"pageP4Verify_scrl")
        self.pageP4Verify_scrl.setStyleSheet(u"background: transparent;")
        self.pageP4Verify_scrl.setFrameShape(QFrame.NoFrame)
        self.pageP4Verify_scrl.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.pageP4Verify_scrl.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.pageP4Verify_scrl.setWidgetResizable(True)
        self.pageP4Verify_cont = QWidget()
        self.pageP4Verify_cont.setObjectName(u"pageP4Verify_cont")
        self.pageP4Verify_cont.setGeometry(QRect(0, 0, 189, 282))
        self.pageP4Verify_cont.setStyleSheet(u"background: transparent;")
        self.pageP4Verify_contLyt = QVBoxLayout(self.pageP4Verify_cont)
        self.pageP4Verify_contLyt.setSpacing(15)
        self.pageP4Verify_contLyt.setObjectName(u"pageP4Verify_contLyt")
        self.pageP4Verify_contLyt.setContentsMargins(5, 5, 5, 5)
        self.pageP4Verify_tLbl = QLabel(self.pageP4Verify_cont)
        self.pageP4Verify_tLbl.setObjectName(u"pageP4Verify_tLbl")
        self.pageP4Verify_tLbl.setMaximumSize(QSize(16777215, 40))
        self.pageP4Verify_tLbl.setFont(font)
        self.pageP4Verify_tLbl.setStyleSheet(u"font-size: 16pt")
        self.pageP4Verify_tLbl.setAlignment(Qt.AlignCenter)

        self.pageP4Verify_contLyt.addWidget(self.pageP4Verify_tLbl)

        self.pageP4Verify_dLbl = QLabel(self.pageP4Verify_cont)
        self.pageP4Verify_dLbl.setObjectName(u"pageP4Verify_dLbl")
        self.pageP4Verify_dLbl.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.pageP4Verify_dLbl.setWordWrap(True)

        self.pageP4Verify_contLyt.addWidget(self.pageP4Verify_dLbl)

        self.pageP4Verify_r1Lyt = QHBoxLayout()
        self.pageP4Verify_r1Lyt.setObjectName(u"pageP4Verify_r1Lyt")

        self.pageP4Verify_contLyt.addLayout(self.pageP4Verify_r1Lyt)

        self.pageP4Verify_r2Lyt = QHBoxLayout()
        self.pageP4Verify_r2Lyt.setObjectName(u"pageP4Verify_r2Lyt")

        self.pageP4Verify_contLyt.addLayout(self.pageP4Verify_r2Lyt)

        self.pageP4Verify_r3Lyt = QHBoxLayout()
        self.pageP4Verify_r3Lyt.setObjectName(u"pageP4Verify_r3Lyt")

        self.pageP4Verify_contLyt.addLayout(self.pageP4Verify_r3Lyt)

        self.pageP4Verify_r4Lyt = QVBoxLayout()
        self.pageP4Verify_r4Lyt.setObjectName(u"pageP4Verify_r4Lyt")

        self.pageP4Verify_contLyt.addLayout(self.pageP4Verify_r4Lyt)

        self.pageP4Verify_r5Lyt = QVBoxLayout()
        self.pageP4Verify_r5Lyt.setObjectName(u"pageP4Verify_r5Lyt")

        self.pageP4Verify_contLyt.addLayout(self.pageP4Verify_r5Lyt)

        self.pageP4Verify_scrl.setWidget(self.pageP4Verify_cont)

        self.pageP4Verify_lyt.addWidget(self.pageP4Verify_scrl)

        self.pages.addWidget(self.pageP4Verify)
        self.pageP1Prog = QWidget()
        self.pageP1Prog.setObjectName(u"pageP1Prog")
        self.pageP1Prog_lyt = QVBoxLayout(self.pageP1Prog)
        self.pageP1Prog_lyt.setObjectName(u"pageP1Prog_lyt")
        self.pageP1Prog_scrl = QScrollArea(self.pageP1Prog)
        self.pageP1Prog_scrl.setObjectName(u"pageP1Prog_scrl")
        self.pageP1Prog_scrl.setStyleSheet(u"background: transparent;")
        self.pageP1Prog_scrl.setFrameShape(QFrame.NoFrame)
        self.pageP1Prog_scrl.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.pageP1Prog_scrl.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.pageP1Prog_scrl.setWidgetResizable(True)
        self.pageP1Prog_cont = QWidget()
        self.pageP1Prog_cont.setObjectName(u"pageP1Prog_cont")
        self.pageP1Prog_cont.setGeometry(QRect(0, 0, 832, 640))
        self.pageP1Prog_cont.setStyleSheet(u"background: transparent;")
        self.pageP1Prog_conLyt = QVBoxLayout(self.pageP1Prog_cont)
        self.pageP1Prog_conLyt.setSpacing(15)
        self.pageP1Prog_conLyt.setObjectName(u"pageP1Prog_conLyt")
        self.pageP1Prog_conLyt.setContentsMargins(5, 5, 5, 5)
        self.pageP1Prog_tLbl = QLabel(self.pageP1Prog_cont)
        self.pageP1Prog_tLbl.setObjectName(u"pageP1Prog_tLbl")
        self.pageP1Prog_tLbl.setMaximumSize(QSize(16777215, 40))
        self.pageP1Prog_tLbl.setFont(font)
        self.pageP1Prog_tLbl.setStyleSheet(u"font-size: 16pt")
        self.pageP1Prog_tLbl.setAlignment(Qt.AlignCenter)

        self.pageP1Prog_conLyt.addWidget(self.pageP1Prog_tLbl)

        self.pageP1Prog_dLbl = QLabel(self.pageP1Prog_cont)
        self.pageP1Prog_dLbl.setObjectName(u"pageP1Prog_dLbl")
        self.pageP1Prog_dLbl.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.pageP1Prog_dLbl.setWordWrap(True)

        self.pageP1Prog_conLyt.addWidget(self.pageP1Prog_dLbl)

        self.pageP1Prog_r1Lyt = QHBoxLayout()
        self.pageP1Prog_r1Lyt.setObjectName(u"pageP1Prog_r1Lyt")

        self.pageP1Prog_conLyt.addLayout(self.pageP1Prog_r1Lyt)

        self.pageP1Prog_r2Lyt = QHBoxLayout()
        self.pageP1Prog_r2Lyt.setObjectName(u"pageP1Prog_r2Lyt")

        self.pageP1Prog_conLyt.addLayout(self.pageP1Prog_r2Lyt)

        self.pageP1Prog_r3Lyt = QHBoxLayout()
        self.pageP1Prog_r3Lyt.setObjectName(u"pageP1Prog_r3Lyt")

        self.pageP1Prog_conLyt.addLayout(self.pageP1Prog_r3Lyt)

        self.pageP1Prog_r4Lyt = QVBoxLayout()
        self.pageP1Prog_r4Lyt.setObjectName(u"pageP1Prog_r4Lyt")

        self.pageP1Prog_conLyt.addLayout(self.pageP1Prog_r4Lyt)

        self.pageP1Prog_r5Lyt = QVBoxLayout()
        self.pageP1Prog_r5Lyt.setObjectName(u"pageP1Prog_r5Lyt")

        self.pageP1Prog_conLyt.addLayout(self.pageP1Prog_r5Lyt)

        self.pageP1Prog_scrl.setWidget(self.pageP1Prog_cont)

        self.pageP1Prog_lyt.addWidget(self.pageP1Prog_scrl)

        self.pages.addWidget(self.pageP1Prog)
        self.pageP2Back = QWidget()
        self.pageP2Back.setObjectName(u"pageP2Back")
        self.pageP2Back_Lyt = QVBoxLayout(self.pageP2Back)
        self.pageP2Back_Lyt.setObjectName(u"pageP2Back_Lyt")
        self.pageP2Back_scrl = QScrollArea(self.pageP2Back)
        self.pageP2Back_scrl.setObjectName(u"pageP2Back_scrl")
        self.pageP2Back_scrl.setStyleSheet(u"background: transparent;")
        self.pageP2Back_scrl.setFrameShape(QFrame.NoFrame)
        self.pageP2Back_scrl.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.pageP2Back_scrl.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.pageP2Back_scrl.setWidgetResizable(True)
        self.pageP2Back_cont = QWidget()
        self.pageP2Back_cont.setObjectName(u"pageP2Back_cont")
        self.pageP2Back_cont.setGeometry(QRect(0, 0, 204, 266))
        self.pageP2Back_cont.setStyleSheet(u"background: transparent;")
        self.pageP2Back_contLyt = QVBoxLayout(self.pageP2Back_cont)
        self.pageP2Back_contLyt.setSpacing(15)
        self.pageP2Back_contLyt.setObjectName(u"pageP2Back_contLyt")
        self.pageP2Back_contLyt.setContentsMargins(5, 5, 5, 5)
        self.pageP2Back_tLbl = QLabel(self.pageP2Back_cont)
        self.pageP2Back_tLbl.setObjectName(u"pageP2Back_tLbl")
        self.pageP2Back_tLbl.setMaximumSize(QSize(16777215, 40))
        self.pageP2Back_tLbl.setFont(font)
        self.pageP2Back_tLbl.setStyleSheet(u"font-size: 16pt")
        self.pageP2Back_tLbl.setAlignment(Qt.AlignCenter)

        self.pageP2Back_contLyt.addWidget(self.pageP2Back_tLbl)

        self.pageP2Back_dLbl = QLabel(self.pageP2Back_cont)
        self.pageP2Back_dLbl.setObjectName(u"pageP2Back_dLbl")
        self.pageP2Back_dLbl.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.pageP2Back_dLbl.setWordWrap(True)

        self.pageP2Back_contLyt.addWidget(self.pageP2Back_dLbl)

        self.pageP2Back_r1Lyt = QHBoxLayout()
        self.pageP2Back_r1Lyt.setObjectName(u"pageP2Back_r1Lyt")

        self.pageP2Back_contLyt.addLayout(self.pageP2Back_r1Lyt)

        self.pageP2Back_r2Lyt = QHBoxLayout()
        self.pageP2Back_r2Lyt.setObjectName(u"pageP2Back_r2Lyt")

        self.pageP2Back_contLyt.addLayout(self.pageP2Back_r2Lyt)

        self.pageP2Back_r3Lyt = QHBoxLayout()
        self.pageP2Back_r3Lyt.setObjectName(u"pageP2Back_r3Lyt")

        self.pageP2Back_contLyt.addLayout(self.pageP2Back_r3Lyt)

        self.pageP2Back_r4Lyt = QVBoxLayout()
        self.pageP2Back_r4Lyt.setObjectName(u"pageP2Back_r4Lyt")

        self.pageP2Back_contLyt.addLayout(self.pageP2Back_r4Lyt)

        self.pageP2Back_r5Lyt = QVBoxLayout()
        self.pageP2Back_r5Lyt.setObjectName(u"pageP2Back_r5Lyt")

        self.pageP2Back_contLyt.addLayout(self.pageP2Back_r5Lyt)

        self.pageP2Back_scrl.setWidget(self.pageP2Back_cont)

        self.pageP2Back_Lyt.addWidget(self.pageP2Back_scrl)

        self.pages.addWidget(self.pageP2Back)
        self.pageP3Restore = QWidget()
        self.pageP3Restore.setObjectName(u"pageP3Restore")
        self.pageP3Restore_lyt = QVBoxLayout(self.pageP3Restore)
        self.pageP3Restore_lyt.setObjectName(u"pageP3Restore_lyt")
        self.pageP3Restore_scrl = QScrollArea(self.pageP3Restore)
        self.pageP3Restore_scrl.setObjectName(u"pageP3Restore_scrl")
        self.pageP3Restore_scrl.setStyleSheet(u"background: transparent;")
        self.pageP3Restore_scrl.setFrameShape(QFrame.NoFrame)
        self.pageP3Restore_scrl.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.pageP3Restore_scrl.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.pageP3Restore_scrl.setWidgetResizable(True)
        self.pageP3Restore_cont = QWidget()
        self.pageP3Restore_cont.setObjectName(u"pageP3Restore_cont")
        self.pageP3Restore_cont.setGeometry(QRect(0, 0, 206, 266))
        self.pageP3Restore_cont.setStyleSheet(u"background: transparent;")
        self.pageP3Restore_contLyt = QVBoxLayout(self.pageP3Restore_cont)
        self.pageP3Restore_contLyt.setSpacing(15)
        self.pageP3Restore_contLyt.setObjectName(u"pageP3Restore_contLyt")
        self.pageP3Restore_contLyt.setContentsMargins(5, 5, 5, 5)
        self.pageP3Restore_tLbl = QLabel(self.pageP3Restore_cont)
        self.pageP3Restore_tLbl.setObjectName(u"pageP3Restore_tLbl")
        self.pageP3Restore_tLbl.setMaximumSize(QSize(16777215, 40))
        self.pageP3Restore_tLbl.setFont(font)
        self.pageP3Restore_tLbl.setStyleSheet(u"font-size: 16pt")
        self.pageP3Restore_tLbl.setAlignment(Qt.AlignCenter)

        self.pageP3Restore_contLyt.addWidget(self.pageP3Restore_tLbl)

        self.pageP3Restore_dLbl = QLabel(self.pageP3Restore_cont)
        self.pageP3Restore_dLbl.setObjectName(u"pageP3Restore_dLbl")
        self.pageP3Restore_dLbl.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.pageP3Restore_dLbl.setWordWrap(True)

        self.pageP3Restore_contLyt.addWidget(self.pageP3Restore_dLbl)

        self.pageP2Back_r1Lyt_2 = QHBoxLayout()
        self.pageP2Back_r1Lyt_2.setObjectName(u"pageP2Back_r1Lyt_2")

        self.pageP3Restore_contLyt.addLayout(self.pageP2Back_r1Lyt_2)

        self.pageP2Back_r2Lyt_2 = QHBoxLayout()
        self.pageP2Back_r2Lyt_2.setObjectName(u"pageP2Back_r2Lyt_2")

        self.pageP3Restore_contLyt.addLayout(self.pageP2Back_r2Lyt_2)

        self.pageP2Back_r3Lyt_2 = QHBoxLayout()
        self.pageP2Back_r3Lyt_2.setObjectName(u"pageP2Back_r3Lyt_2")

        self.pageP3Restore_contLyt.addLayout(self.pageP2Back_r3Lyt_2)

        self.pageP2Back_r4Lyt_2 = QVBoxLayout()
        self.pageP2Back_r4Lyt_2.setObjectName(u"pageP2Back_r4Lyt_2")

        self.pageP3Restore_contLyt.addLayout(self.pageP2Back_r4Lyt_2)

        self.pageP2Back_r5Lyt_2 = QVBoxLayout()
        self.pageP2Back_r5Lyt_2.setObjectName(u"pageP2Back_r5Lyt_2")

        self.pageP3Restore_contLyt.addLayout(self.pageP2Back_r5Lyt_2)

        self.pageP3Restore_scrl.setWidget(self.pageP3Restore_cont)

        self.pageP3Restore_lyt.addWidget(self.pageP3Restore_scrl)

        self.pages.addWidget(self.pageP3Restore)

        self.verticalLayout_2.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("MainPages", u"Custom Widgets Page", None))
        self.description_label.setText(QCoreApplication.translate("MainPages", u"Here will be all the custom widgets, they will be added over time on this page.\n"
"I will try to always record a new tutorial when adding a new Widget and updating the project on Patreon before launching on GitHub and GitHub after the public release.", None))
        self.pageP0Main_tLbl.setText(QCoreApplication.translate("MainPages", u"Main Process Selection Page", None))
        self.pageP0Main_dLbl.setText(QCoreApplication.translate("MainPages", u"Here will be all the custom widgets, they will be added over time on this page.\n"
"I will try to always record a new tutorial when adding a new Widget and updating the project on Patreon before launching on GitHub and GitHub after the public release.", None))
        self.pageP4Verify_tLbl.setText(QCoreApplication.translate("MainPages", u"Verify Process Page", None))
        self.pageP4Verify_dLbl.setText(QCoreApplication.translate("MainPages", u"Here will be all the custom widgets, they will be added over time on this page.\n"
"I will try to always record a new tutorial when adding a new Widget and updating the project on Patreon before launching on GitHub and GitHub after the public release.", None))
        self.pageP1Prog_tLbl.setText(QCoreApplication.translate("MainPages", u"Programming Process Page", None))
        self.pageP1Prog_dLbl.setText(QCoreApplication.translate("MainPages", u"Here will be all the custom widgets, they will be added over time on this page.\n"
"I will try to always record a new tutorial when adding a new Widget and updating the project on Patreon before launching on GitHub and GitHub after the public release.", None))
        self.pageP2Back_tLbl.setText(QCoreApplication.translate("MainPages", u"Backup Process Page", None))
        self.pageP2Back_dLbl.setText(QCoreApplication.translate("MainPages", u"Here will be all the custom widgets, they will be added over time on this page.\n"
"I will try to always record a new tutorial when adding a new Widget and updating the project on Patreon before launching on GitHub and GitHub after the public release.", None))
        self.pageP3Restore_tLbl.setText(QCoreApplication.translate("MainPages", u"Restore Process Page", None))
        self.pageP3Restore_dLbl.setText(QCoreApplication.translate("MainPages", u"Here will be all the custom widgets, they will be added over time on this page.\n"
"I will try to always record a new tutorial when adding a new Widget and updating the project on Patreon before launching on GitHub and GitHub after the public release.", None))
    # retranslateUi

