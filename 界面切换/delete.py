# -*- coding: utf-8 -*-
import os

from PyQt5 import QtCore, QtGui, QtWidgets

from file_rw import read_data, write_data
from msg import Ui_msg

class Ui_delete(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 120, 41, 41))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 200, 300, 41))
        self.label_2.setObjectName("label")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(140, 127, 121, 30))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(280, 130, 103, 27))
        self.pushButton_8.setObjectName("pushButton")
        self.pushButton_8.clicked.connect(self.delete_data)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "删除"))
        # self.label_2.setText(_translate("MainWindow", "提示"))
        self.pushButton_8.setText(_translate("MainWindow", "删除"))

    def delete_data(self):
        self.label_2.setText('\t\t未找到数据')
        str_del=str(self.textEdit.toPlainText())
        if not str_del=='':
            data=read_data()
            for i in range(len(data)):
                if str_del in str(data[i]):        #转换为字符串才可以实现模糊匹配
                    print('删除一条数据：%s'%data[i])
                    self.label_2.setText('删除一条数据：'+str(data[i]))
                    del data[i]

                    #写回文件
                    write_data(data)
                    break
            # data_library.data=filter(lambda x: 'yxy' not in str(x),data_library.data)
        else:
            self.label_2.setText    ('\t\t请输入！')
            self.win =Ui_msg('\t请输入！')
            self.win.show()
            local_path=os.path.dirname(__file__)
            print(local_path)
