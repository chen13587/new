# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets, QtCore, QtGui


def int2bin(b):
    a = ''
    tmp = b
    for i in range(0,8):
        a =str(tmp-((tmp//2)*2))+a
        tmp=int(tmp//2)
    return a

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # self.child = Ui_ChildrenWindow()


        self.label=QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200,30,150,30))

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 290, 103, 27))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 290, 103, 27))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(50, 60, 201, 181))
        self.textEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textEdit.setObjectName("textEdit")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(290, 60, 201, 181))
        # self.textBrowser.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))   #鼠标设为文本指针
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.set_text)
        self.pushButton_2.clicked.connect(self.get_text)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "写入"))
        self.pushButton_2.setText(_translate("MainWindow", "转换"))
        self.label.setText(_translate("MainWindow", "浮点转为二进制"))

    # def childShow(self):
    #     self.MainWindow.addWidget(self.child)  # 添加子窗口
    #     self.child.show()

    def set_text(self):
        s1=self.textEdit.toPlainText()+'hello'
        self.textEdit.setText(s1)


        # self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_3.setGeometry(QtCore.QRect(220, 340, 103, 27))
        # self.pushButton_3.clicked.connect(self.output)
        # self.pushButton_3.show()

        # self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_3.setGeometry(QtCore.QRect(0, 0, 103, 27))
    def get_text(self):
        # s2=self.textBrowser.toPlainText()+self.textEdit.toPlainText()
        # self.textBrowser.setText(s2)

        num=float(self.textEdit.toPlainText())
        zs=int(num)
        xs=int(100*(num-zs))
        print('整数位：'+str(zs))
        print('小数位：'+str(xs))
        print('---------------------------------------')

        b1=''
        tmp=zs
        for i in range(0, 16):
            b1 = str(tmp-((tmp//2)*2))+b1
            tmp = int(tmp // 2)
        print('整数2进制'+b1)

        b2=''
        tmp=xs
        for i in range(0,8):
            tmp=tmp*2
            b2+=str(int(tmp/100))
            tmp=int(tmp%100)
            if tmp==0:
                break
        print('小数2进制'+b2)

        i=0
        while b1[i]=='0':
            i+=1
        i=16-(i+1)

        print('i=%d' % (i))

        sum=b1+b2
        print(sum)

        jm=127+i  #阶码
        jm=int2bin(jm)
        print('阶码='+jm)

        end=jm+b1[-i:]+b2

        print(end)
        print('---------------------------------------')

        self.textBrowser.setText(end)

    def output(self):
        print("I'm button 3")

# class Ui_ChildrenWindow(object):
#
#     def setupUi(self, ChildrenWindow):
#         ChildrenWindow.setObjectName("ChildrenWindow")
#         ChildrenWindow.resize(413, 233)
#         self.centralwidget = QtWidgets.QWidget(ChildrenWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.pushButton = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton.setGeometry(QtCore.QRect(150, 120, 103, 27))
#         self.pushButton.setObjectName("pushButton")
#         ChildrenWindow.setCentralWidget(self.centralwidget)
#
#         self.retranslateUi(ChildrenWindow)
#         QtCore.QMetaObject.connectSlotsByName(ChildrenWindow)
#
#     def retranslateUi(self, ChildrenWindow):
#         _translate = QtCore.QCoreApplication.translate
#         ChildrenWindow.setWindowTitle(_translate("ChildrenWindow", "ChildrenWindow"))
#         self.pushButton.setText(_translate("ChildrenWindow", "button"))
