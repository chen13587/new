# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_msg(QtWidgets.QWidget):
    def __init__(self,msg):
        super(Ui_msg, self).__init__()
        self.setObjectName("view1")
        self.resize(300, 200)
        self.show_msg=msg

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(90, 40, 181, 91))
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(110, 150, 70, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.close)

        self.retranslateUi()       #设置按钮

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate

        self.setWindowTitle("消息")
        self.label.setText(self.show_msg)
        self.pushButton.setText(_translate("view1", "关闭"))



