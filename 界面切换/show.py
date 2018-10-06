
# import sys
#
# from PyQt5.QtWidgets import QApplication, QMainWindow
#
# from add import Ui_add
# from find import Ui_find
# from main import Ui_MainWindow
#
#
#
# class Main(QMainWindow,Ui_MainWindow):
#     def __init__(self):
#         super (Main,self).__init__()
#         self.setupUi(self)
#         self.chaild_find = Ui_find()
#         self.chaild_add=Ui_add()
#         self.pushButton.clicked.connect(self.show_f)
#         self.pushButton_2.clicked.connect(self.show_a)
#     def show_f(self):
#         self.gridLayout.addWidget(self.chaild_find)  # 将窗口放入girdLayout中
#         self.chaild_find.show()
#     def show_a(self):
#         self.gridLayout.addWidget(self.chaild_add)
#         self.chaild_add.show()
#
#
# class show_f(QMainWindow,Ui_find):
#     def __init__(self):
#         super(show_f,self).__init__()
#         self.setupUi(self)
#
# class show_a(QMainWindow,Ui_add):
#
#     def __init__(self):
#         super(show_a,self).__init__()
#         self.setupUi(self)
#
#
# if __name__=='__main__':
#     app = QApplication(sys.argv)
#     Main = Main()
#     Show = show_f()
#     New = show_a()
#     Main.show()
#     sys.exit(app.exec_())


# <--*-- coding:utf-8 --*-->
from PyQt5.QtWidgets import QMainWindow, QApplication

from delete import Ui_delete
from main import Ui_MainWindow
from find import Ui_find
from add import Ui_add
import sys


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.child1=Show_find()       #构建子界面
        self.child2=Show_add()
        self.child3=Show_delete()

        self.pushButton.clicked.connect(self.Show_f)
        self.pushButton_2.clicked.connect(self.Show_a)
        self.pushButton_3.clicked.connect(self.Show_d)
        self.Show_f()
    def Show_f(self):       #切换到界面
        self.Close_all()
        self.gridLayout.addWidget(self.child1)  # 将窗口放入girdLayout中
        self.child1.show()  # 打开子窗口1

    def Show_a(self):
        self.Close_all()
        self.gridLayout.addWidget(self.child2)
        self.child2.show()
    def Show_d(self):
        self.Close_all()
        self.gridLayout.addWidget(self.child3)
        self.child3.show()

    def Close_all(self):
        self.child1.close()
        self.child2.close()
        self.child3.close()


class Show_delete(QMainWindow,Ui_delete):
    def __init__(self):
        super(Show_delete,self).__init__()
        self.setupUi(self)




class Show_add(QMainWindow, Ui_add):       #用于构建界面
    def __init__(self):
        super(Show_add, self).__init__()
        self.setupUi(self)
        # self.pushButton.clicked.connect(self.Close)

    def Close(self):
        self.close()


class Show_find(QMainWindow, Ui_find):
    def __init__(self):
        super(Show_find, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main = Main()
    # Show = Show()
    # New = New()
    Main.show()

    sys.exit(app.exec_())