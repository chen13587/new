# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(QtWidgets.QWidget):
    def __init__(self):
        super(Ui_Form, self).__init__()
        self.setObjectName("nihao")
        self.resize(400, 300)
        self.setWindowTitle("消息")

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(100, 80, 181, 91))
        self.label.setObjectName("label")
        self.label.setText("你好！")

        self.retranslateUi()       #设置按钮
        
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(130, 100, 103, 27))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText(_translate("MainWindow", "查询员工"))



