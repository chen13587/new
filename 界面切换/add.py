# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import time

from PyQt5 import QtCore, QtGui, QtWidgets

from file_rw import write_data, read_data
from msg import Ui_msg

class Ui_add(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 90, 161, 31))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(90, 200, 91, 31))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(220, 290, 111, 31))
        self.pushButton_7.setObjectName("pushButton")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(250, 200, 61, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(390, 200, 161, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 150, 51, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(430, 140, 71, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(260, 140, 61, 41))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_7.clicked.connect(MainWindow.add_data)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "请输入新员工信息"))
        self.label_2.setText(_translate("MainWindow", "姓名"))
        self.label_3.setText(_translate("MainWindow", "电话"))
        self.label_4.setText(_translate("MainWindow", "性别"))

        self.pushButton_7.setText(_translate("MainWindow", "确认添加"))

    def add_data(self):
        self.label.setText("请输入新员工信息")
        self.name=self.textEdit.toPlainText()
        self.sex=self.textEdit_2.toPlainText()
        self.phone=self.textEdit_3.toPlainText()
        if not self.name=='' and not self.sex=='' and not self.phone=='':

            tmp_data=read_data()
            tmp_data.append([self.name,self.sex,self.phone])
            write_data(tmp_data)

            self.label.setText('    记录成功')
            self.textEdit.setText('')
            self.textEdit_2.setText('')
            self.textEdit_3.setText('')
            # time.sleep(2)

        else:
            self.win=Ui_msg('添加失败 请完整输入！')
            self.win.show()