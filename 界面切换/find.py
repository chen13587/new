# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

from file_rw import read_data

li = ('姓名：','\t性别：','\t电话：')
class Ui_find(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 110, 41, 41))
        self.label.setObjectName("label")

        self.textBrowser = QtWidgets.QTextEdit(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 200, 600, 150))
        self.textBrowser.setObjectName("textBrowser")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(105, 118, 131, 30))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(260, 120, 103, 27))
        self.pushButton_6.setObjectName("pushButton")
        self.pushButton_6.clicked.connect(self.find_data)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "查询"))
        # self.textBrowser.setText(_translate("MainWindow", "这里显示结果"))
        self.pushButton_6.setText(_translate("MainWindow", "查询"))

    def find_data(self):
        find_num=0
        n=0
        # t=0
        self.textBrowser.setText('')
        str_find=str(self.textEdit.toPlainText())
        if not str_find=='':
            # f_data=open('f_data.py','r')
            # f_data.seek(5)
            # data=eval(f_data.read())
            # f_data.close()
            data=read_data()
            ################       管理员模块      #################
            if str_find == '666666':
                for i in data:
                    for t in range(len(i)):
                        str_old = self.textBrowser.toPlainText()
                        self.textBrowser.setText(str_old + li[t] + i[t] + ' ')
                    self.textBrowser.setText(self.textBrowser.toPlainText() + '\n')
                self.textBrowser.setText(self.textBrowser.toPlainText() + '\n\t\t\t欢迎管理员')
            ################       管理员模块      #################


            else:
                str_tmp=''
                for i in data:
                    n+=1
                    if str_find in str(i):
                        find_num+=1
                        print("在列表的第%d项找到"%n)
                        for t in range(len(i)):
                            str_tmp+=(li[t]+i[t])   #写入缓冲区
                        str_tmp+='\n'
                self.textBrowser.setText(str_tmp)
                self.textBrowser.setText(self.textBrowser.toPlainText()+'找到%d项'%find_num)
        else:
            self.textBrowser.setText('请输入查询条件')
        # print('共记录了%d条数据'%len(data_library.data))