# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets
from socket import *
import threading

from PyQt5.QtCore import pyqtSignal, QObject


class Ui_MainWindow(QObject):
    msignal=pyqtSignal(str)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(554, 482)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 260, 491, 201))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(390, 40, 103, 27))
        self.pushButton.setObjectName("pushButton")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(30, 100, 261, 141))
        self.textEdit_4.setObjectName("textEdit_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 140, 111, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        # self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_3.setGeometry(QtCore.QRect(390, 70, 103, 27))
        # self.pushButton_3.setObjectName("pushButton_3")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(60, 40, 131, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 40, 21, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 40, 51, 31))
        self.label_2.setObjectName("label_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(270, 40, 71, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(self.send)
        # self.pushButton_3.clicked.connect(self.disconnect)
        self.pushButton.clicked.connect(self.connect)

        self.statusflag=False   #连接状态标志
        self.sendflag=False     #发送标志

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "连接"))
        self.pushButton_2.setText(_translate("MainWindow", "发送"))
        self.label.setText(_translate("MainWindow", "IP"))
        self.label_2.setText(_translate("MainWindow", "PORT"))

    def connect(self):
        if not self.statusflag:
            self.ip=self.textEdit_2.toPlainText()
            self.port=self.textEdit_3.toPlainText()
            # self.ip='10.10.70.53'
            # self.port=8089
            if self.ip and self.port:
                print(self.ip,self.port)
                try:
                    self.c_client = socket(AF_INET, SOCK_STREAM)
                    self.c_client.connect((self.ip,int(self.port)))

                    thread1=threading.Thread(target=self.send_thread,args=(self.c_client,))
                    thread1.start()     #开始任务
                    thread2=threading.Thread(target=self.recv_thread,args=(self.c_client,))
                    thread2.start()     #开始任务
                    self.statusflag = True
                    self.pushButton.setText('断开')
                except BaseException as e:
                    self.pushButton.setText('连接')
                    self.statusflag = False
                    print('连接失败')
                    print(e)

        elif self.statusflag:
            try:
                self.c_client.close()
                self.statusflag=False
                self.pushButton.setText('连接')
            except BaseException as e:
                self.pushButton.setText('断开')
                self.statusflag = True
                print('断开失败')
                print(e)

    def send(self):
        self.sendflag=True
        print(self.sendflag)

    def recv(self,data):
        str='%s%s\n'%(self.textEdit.toPlainText(),data)

        self.textEdit.setText(str)

    def send_thread(self,socked):
        print('发送任务创建成功')
        while True:
            # while self.statusflag:      #如果为Flase，就等待
            #     pass
            if self.sendflag:
                try:
                    str = self.textEdit_4.toPlainText()
                    socked.send(str.encode('utf-8'))
                    print(str)
                    self.sendflag=False
                except BaseException as e:
                    socked.close()
                    print('连接断开')
                    print(e)
                    break

    def recv_thread(self,socked):
        self.msignal.connect(self.recv)  # 绑定信号到函数
        print('接收任务创建成功')
        while True:
            try:
                data = socked.recv(1024).decode('utf-8')
                print(data)
                self.msignal.emit(data)   # 发射信号.
            except BaseException as e:
                socked.close()
                print('断开连接')
                print(e)
                break
