# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mwin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MWin(object):
    def setupUi(self, MWin):
        MWin.setObjectName("MWin")
        MWin.resize(560, 280)
        MWin.setMinimumSize(QtCore.QSize(560, 280))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        MWin.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MWin.setWindowIcon(icon)
        self.centralWidget = QtWidgets.QWidget(MWin)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_1)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.duration_check = QtWidgets.QCheckBox(self.tab_1)
        self.duration_check.setChecked(True)
        self.duration_check.setObjectName("duration_check")
        self.horizontalLayout_4.addWidget(self.duration_check)
        self.label_2 = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.filename_label = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.filename_label.setFont(font)
        self.filename_label.setObjectName("filename_label")
        self.horizontalLayout_4.addWidget(self.filename_label)
        self.select_file_btn = QtWidgets.QToolButton(self.tab_1)
        self.select_file_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.select_file_btn.setObjectName("select_file_btn")
        self.horizontalLayout_4.addWidget(self.select_file_btn)
        self.horizontalLayout_4.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.tab_1)
        self.label.setMinimumSize(QtCore.QSize(70, 0))
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.start_time_edit = QtWidgets.QLineEdit(self.tab_1)
        self.start_time_edit.setObjectName("start_time_edit")
        self.horizontalLayout_2.addWidget(self.start_time_edit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radio_label = QtWidgets.QLabel(self.tab_1)
        self.radio_label.setMinimumSize(QtCore.QSize(70, 0))
        self.radio_label.setObjectName("radio_label")
        self.horizontalLayout_3.addWidget(self.radio_label)
        self.end_time_edit = QtWidgets.QLineEdit(self.tab_1)
        self.end_time_edit.setObjectName("end_time_edit")
        self.horizontalLayout_3.addWidget(self.end_time_edit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.start_btn = QtWidgets.QToolButton(self.tab_1)
        self.start_btn.setMinimumSize(QtCore.QSize(60, 0))
        self.start_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start_btn.setObjectName("start_btn")
        self.horizontalLayout_5.addWidget(self.start_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.select_files_btn = QtWidgets.QToolButton(self.tab_2)
        self.select_files_btn.setMinimumSize(QtCore.QSize(85, 0))
        self.select_files_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.select_files_btn.setObjectName("select_files_btn")
        self.horizontalLayout_6.addWidget(self.select_files_btn)
        self.start_merge_btn = QtWidgets.QToolButton(self.tab_2)
        self.start_merge_btn.setMinimumSize(QtCore.QSize(85, 0))
        self.start_merge_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start_merge_btn.setObjectName("start_merge_btn")
        self.horizontalLayout_6.addWidget(self.start_merge_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MWin.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MWin)
        self.statusBar.setObjectName("statusBar")
        MWin.setStatusBar(self.statusBar)

        self.retranslateUi(MWin)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MWin)

    def retranslateUi(self, MWin):
        _translate = QtCore.QCoreApplication.translate
        MWin.setWindowTitle(_translate("MWin", "FFmpeg Helper - v0.0.1"))
        self.duration_check.setToolTip(_translate("MWin", "Duration Mode/EndTime Mode"))
        self.duration_check.setText(_translate("MWin", "Duration"))
        self.label_2.setText(_translate("MWin", "|"))
        self.filename_label.setText(_translate("MWin", "no file selected..."))
        self.select_file_btn.setText(_translate("MWin", "..."))
        self.label.setText(_translate("MWin", "Start Time:"))
        self.start_time_edit.setPlaceholderText(_translate("MWin", "format: hh:mm:ss / mm:ss / ss"))
        self.radio_label.setText(_translate("MWin", "Duration:"))
        self.end_time_edit.setPlaceholderText(_translate("MWin", "format: hh:mm:ss / mm:ss / ss"))
        self.start_btn.setText(_translate("MWin", " Start "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MWin", "Cut"))
        self.select_files_btn.setText(_translate("MWin", "Select Files"))
        self.start_merge_btn.setText(_translate("MWin", "Merge"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MWin", "Merge"))

import res_rc
