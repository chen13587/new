#!/usr/bin/env python3.6
#  -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from client import Ui_MainWindow

if __name__ == '__main__':

    pp=QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(pp.exec_())


