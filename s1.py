# -*- coding: utf-8 -*-
import sys
# from connectionDB import db

# Form implementation generated from reading ui file 's1.ui'


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from s2 import Ui_Form
from Listfile import CommonList
from singedin import Ui_Form1


class Ui_MainWindow(object):
    # print(CommonList.reqData)
    # CommonList.reqData.append(({'name': "jk", 'code': "112"}))
    # print(CommonList.reqData)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(697, 442)
        MainWindow.setMinimumSize(QtCore.QSize(0, 3))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777212))
        MainWindow.setBaseSize(QtCore.QSize(4, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\492879\\PycharmProjects\\python_App_modified - Copy\\image\\i1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:0 rgba(221, 245, 255, 255), "
            "stop:1 rgba(255, 255, 255, 255));\n"
            "font: 75 12pt \"MS Shell Dlg 2\";")
        MainWindow.setIconSize(QtCore.QSize(24, 25))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(440, 130, 41, 41))
        self.label_5.setStyleSheet("color: rgb(0, 0, 127);")
        self.label_5.setObjectName("label_5")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 50, 371, 231))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(70, 2, 281, 41))
        self.label_3.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                                   "color: rgb(0, 85, 0);\n"
                                   " \n"
                                   "background-color: rgb(170, 170, 255);\n"
                                   "\n"
                                   "")
        self.label_3.setObjectName("label_3")

        # checkbox
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(10, 140, 121, 16))
        self.checkBox.setStyleSheet("font: 6pt \"MS Shell Dlg 2\";\n"
                                    "color: rgb(0, 0, 127);")
        self.checkBox.setObjectName("checkBox")

        # login
        self.login = QtWidgets.QPushButton(self.frame)
        self.login.setGeometry(QtCore.QRect(130, 180, 101, 24))
        self.login.setStyleSheet("background-color: rgb(170, 170, 255);\n"
                                 "font: 75 10pt \"MS Shell Dlg 2\";\n"
                                 "gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(9, 41, 4, 255), stop:0.085 rgba(2, 79, 0, 255), stop:0.19 rgba(50, 147, 22, 255), stop:0.275 rgba(236, 191, 49, 255), stop:0.39 rgba(243, 61, 34, 255), stop:0.555 rgba(135, 81, 60, 255), stop:0.667 rgba(121, 75, 255, 255), stop:0.825 rgba(164, 255, 244, 255), stop:0.885 rgba(104, 222, 71, 255), stop:1 rgba(93, 128, 0, 255));")
        self.login.setObjectName("login")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(10, 3, 47, 41))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("295128 (1).png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 60, 111, 31))
        self.label.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
                                 "color: rgb(0, 0, 127);")
        self.label.setObjectName("label")
        self.name = QtWidgets.QLineEdit(self.frame)
        self.name.setGeometry(QtCore.QRect(120, 60, 231, 31))
        self.name.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.name.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.name.setStyleSheet(
            "border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));")
        self.name.setText("")
        self.name.setObjectName("name")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 111, 21))
        self.label_2.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";color: rgb(0, 0, 127);\n"
                                   "border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));")
        self.label_2.setObjectName("label_2")
        self.passco = QtWidgets.QLineEdit(self.frame)
        self.passco.setGeometry(QtCore.QRect(120, 110, 231, 31))
        self.passco.setMinimumSize(QtCore.QSize(0, 8))
        self.passco.setStyleSheet(
            "border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));")
        self.passco.setObjectName("passco")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(510, 60, 171, 181))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(20, 10, 131, 31))
        self.label_6.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                                   "color: rgb(0, 85, 0);\n"
                                   " \n"
                                   "background-color: rgb(170, 170, 255);\n"
                                   "\n"
                                   "")
        self.label_6.setObjectName("label_6")
        self.crtaccnt = QtWidgets.QPushButton(self.frame_2)
        self.crtaccnt.setGeometry(QtCore.QRect(40, 140, 101, 24))
        self.crtaccnt.setStyleSheet("background-color: rgb(170, 170, 255);\n"
                                    "font: 75 10pt \"MS Shell Dlg 2\";\n"
                                    "gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(9, 41, 4, 255), stop:0.085 rgba(2, 79, 0, 255), stop:0.19 rgba(50, 147, 22, 255), stop:0.275 rgba(236, 191, 49, 255), stop:0.39 rgba(243, 61, 34, 255), stop:0.555 rgba(135, 81, 60, 255), stop:0.667 rgba(121, 75, 255, 255), stop:0.825 rgba(164, 255, 244, 255), stop:0.885 rgba(104, 222, 71, 255), stop:1 rgba(93, 128, 0, 255));")
        self.crtaccnt.setObjectName("crtaccnt")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(20, 40, 131, 101))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
                                   "color: rgb(0, 104, 76);")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("i2.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")

        # white message box
        self.Messages = QtWidgets.QTextBrowser(self.centralwidget)
        self.Messages.setGeometry(QtCore.QRect(60, 310, 461, 81))
        self.Messages.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "font: 75 10pt \"MS Shell Dlg 2\";\n"
                                    "color: rgb(255, 0, 0);")
        self.Messages.setObjectName("Messages")
        MainWindow.setCentralWidget(self.centralwidget)
        self.crtaccnt.clicked.connect(lambda: self.secondscr(MainWindow))
        self.login.clicked.connect(lambda: self.newind(MainWindow))
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def secondscr(self, Mainwindow):
        # print("in action")
        self.MainWindow = QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        # MainWindow.close()

    def newind(self, MainWindow):
        print(self.name.text(), self.passco.text())
        if (len(CommonList.reqData) == 0):
            self.Messages.setText("Data not found kindly create an account")

        for item in CommonList.reqData:
            print(item)
            for it in item:

                if item["name"] == self.name.text():
                    self.MainWindow = QMainWindow()
                    Name = self.name.text()
                    Code = self.passco.text()
                    self.ui = Ui_Form1()
                    print(Name, Code)

                    # data of name and code lies within var Name and Code

                    self.ui.setupUi(self.MainWindow)
                    self.MainWindow.show()
                    if len(Name) != 0:
                        print(f"hello {Name} Your password is {Code}")
                        self.ui.label.setText(f"hello {Name} Your password is {Code}")
                    else:
                        self.ui.label.setText("kkk")

                    print(Name, Code)
                    MainWindow.close()
                else:
                    print("no")
                    # self.Messages.setTest("yes")
        # self.MainWindow = QMainWindow()
        # Name = self.name.text()
        # Code = self.passco.text()
        # self.ui = Ui_Form1()
        #
        # self.ui.setupUi(self.MainWindow)
        # self.MainWindow.show()
        # if len(Name) != 0:
        #     print("hello")
        #     self.ui.label.setText(Name)
        # else:
        #     self.ui.label.setText("kkk")
        #
        # print(Name, Code)
        # MainWindow.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login Page "))
        self.label_5.setText(_translate("MainWindow", "Or"))
        self.label_3.setText(_translate("MainWindow", "Login to Your Account"))
        self.checkBox.setText(_translate("MainWindow", "Keep log in"))
        self.login.setText(_translate("MainWindow", "LOG IN"))
        self.label.setText(_translate("MainWindow", "USERNAME"))
        self.name.setToolTip(_translate("MainWindow", "<html><head/><body><p>Enter user name</p></body></html>"))
        self.name.setPlaceholderText(_translate("MainWindow", "Enter user name"))
        self.label_2.setText(_translate("MainWindow", "PASSWORD"))
        self.passco.setToolTip(_translate("MainWindow", "<html><head/><body><p>Enter your password</p></body></html>"))
        self.passco.setPlaceholderText(_translate("MainWindow", "Enter your password"))
        self.label_6.setText(_translate("MainWindow", "New Here "))
        self.crtaccnt.setText(_translate("MainWindow", "Sign Up"))


app = QApplication(sys.argv)
MainWindow = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
