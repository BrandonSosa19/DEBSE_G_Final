# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(774, 322)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_1 = QtWidgets.QPushButton(self.centralwidget)
        self.button_1.setGeometry(QtCore.QRect(30, 130, 81, 71))
        self.button_1.setObjectName("button_1")
        self.button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.button_2.setGeometry(QtCore.QRect(120, 130, 81, 71))
        self.button_2.setObjectName("button_2")
        self.button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.button_3.setGeometry(QtCore.QRect(210, 130, 81, 71))
        self.button_3.setObjectName("button_3")
        self.button_4 = QtWidgets.QPushButton(self.centralwidget)
        self.button_4.setGeometry(QtCore.QRect(300, 130, 81, 71))
        self.button_4.setObjectName("button_4")
        self.button_5 = QtWidgets.QPushButton(self.centralwidget)
        self.button_5.setGeometry(QtCore.QRect(390, 130, 81, 71))
        self.button_5.setObjectName("button_5")
        self.button_6 = QtWidgets.QPushButton(self.centralwidget)
        self.button_6.setGeometry(QtCore.QRect(480, 130, 81, 71))
        self.button_6.setObjectName("button_6")
        self.button_7 = QtWidgets.QPushButton(self.centralwidget)
        self.button_7.setGeometry(QtCore.QRect(570, 130, 81, 71))
        self.button_7.setObjectName("button_7")
        self.button_8 = QtWidgets.QPushButton(self.centralwidget)
        self.button_8.setGeometry(QtCore.QRect(660, 130, 81, 71))
        self.button_8.setObjectName("button_8")
        self.lbl_Bin = QtWidgets.QLabel(self.centralwidget)
        self.lbl_Bin.setGeometry(QtCore.QRect(190, 30, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lbl_Bin.setFont(font)
        self.lbl_Bin.setWordWrap(False)
        self.lbl_Bin.setObjectName("lbl_Bin")
        self.lbl_Bin_2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_Bin_2.setGeometry(QtCore.QRect(380, 30, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lbl_Bin_2.setFont(font)
        self.lbl_Bin_2.setWordWrap(False)
        self.lbl_Bin_2.setObjectName("lbl_Bin_2")
        self.lbl_letter = QtWidgets.QLabel(self.centralwidget)
        self.lbl_letter.setGeometry(QtCore.QRect(420, 30, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lbl_letter.setFont(font)
        self.lbl_letter.setWordWrap(False)
        self.lbl_letter.setObjectName("lbl_letter")
        self.check_1 = QtWidgets.QCheckBox(self.centralwidget)
        self.check_1.setEnabled(True)
        self.check_1.setGeometry(QtCore.QRect(60, 210, 16, 20))
        self.check_1.setText("")
        self.check_1.setObjectName("check_1")
        self.check_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.check_2.setGeometry(QtCore.QRect(150, 210, 16, 20))
        self.check_2.setText("")
        self.check_2.setObjectName("check_2")
        self.check_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.check_3.setGeometry(QtCore.QRect(240, 210, 16, 20))
        self.check_3.setText("")
        self.check_3.setObjectName("check_3")
        self.check_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.check_4.setGeometry(QtCore.QRect(330, 210, 16, 20))
        self.check_4.setText("")
        self.check_4.setObjectName("check_4")
        self.check_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.check_5.setGeometry(QtCore.QRect(420, 210, 16, 20))
        self.check_5.setText("")
        self.check_5.setObjectName("check_5")
        self.check_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.check_6.setGeometry(QtCore.QRect(510, 210, 16, 20))
        self.check_6.setText("")
        self.check_6.setObjectName("check_6")
        self.check_7 = QtWidgets.QCheckBox(self.centralwidget)
        self.check_7.setGeometry(QtCore.QRect(600, 210, 16, 20))
        self.check_7.setText("")
        self.check_7.setObjectName("check_7")
        self.check_8 = QtWidgets.QCheckBox(self.centralwidget)
        self.check_8.setGeometry(QtCore.QRect(690, 210, 16, 20))
        self.check_8.setText("")
        self.check_8.setObjectName("check_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 774, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_1.setText(_translate("MainWindow", "128"))
        self.button_2.setText(_translate("MainWindow", "64"))
        self.button_3.setText(_translate("MainWindow", "32"))
        self.button_4.setText(_translate("MainWindow", "16"))
        self.button_5.setText(_translate("MainWindow", "8"))
        self.button_6.setText(_translate("MainWindow", "4"))
        self.button_7.setText(_translate("MainWindow", "2"))
        self.button_8.setText(_translate("MainWindow", "1"))
        self.lbl_Bin.setText(_translate("MainWindow", "00000000"))
        self.lbl_Bin_2.setText(_translate("MainWindow", ":"))
        self.lbl_letter.setText(_translate("MainWindow", "-"))
