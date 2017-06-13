# -*-coding:utf-8-*-
import sys
import locale
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtGui
from PyQt4 import QtCore
from scan_page import Scan_Page
from query_page import Query_Page
from insert_page import Insert_Page
from count_page import Count_Page
from table_scan import Table_scan
from person_page import Person_Page
from sys_page import Sys_Page


  # PyQt4中文显示
mycode = locale.getpreferredencoding()
code = QTextCodec.codecForName(mycode)
QTextCodec.setCodecForLocale(code)
QTextCodec.setCodecForTr(code)
QTextCodec.setCodecForCStrings(code)


# 功能控制页
class Ctrl_Function(QtGui.QDialog):

     Scan_function_signal = QtCore.pyqtSignal()
     Query_function_signal = QtCore.pyqtSignal()
     Insert_function_signal = QtCore.pyqtSignal()
     Count_function_signal = QtCore.pyqtSignal()
     Person_function_signal = QtCore.pyqtSignal()
     Manage_function_signal = QtCore.pyqtSignal()
     Quit_function_signal = QtCore.pyqtSignal()


     def __init__(self):
         super(Ctrl_Function, self).__init__()
         # self.initUI()

     def initUI(self):


        self.Scan_Button = QtGui.QPushButton('档案浏览', self)
        self.Scan_Button.move(200, 100)
        self.Scan_Button.clicked.connect(self.Scan_Button_Event)

        self.Count_Button = QtGui.QPushButton('人员统计', self)
        self.Count_Button.move(200, 200)
        self.Count_Button.clicked.connect(self.Count_Button_Event)

        self.Person_Page_Button = QtGui.QPushButton('个人报表', self)
        self.Person_Page_Button.move(200, 300)
        self.Person_Page_Button.clicked.connect(self.Person_Page_Button_Event)

        self.Query_Button = QtGui.QPushButton('人员查询', self)
        self.Query_Button.move(400, 100)
        self.Query_Button.clicked.connect(self.Query_Button_Event)

        self.Insert_Button = QtGui.QPushButton('档案录入', self)
        self.Insert_Button.move(400, 200)
        self.Insert_Button.clicked.connect(self.Insert_Button_Event)

        self.Scan_Table_Button = QtGui.QPushButton('相关表浏览', self)
        self.Scan_Table_Button.move(400, 300)
        self.Scan_Table_Button.clicked.connect(self.Scan_Table_Button_Event)

        self.Manage_Button = QtGui.QPushButton('系统管理', self)
        self.Manage_Button.move(200, 400)
        self.Manage_Button.clicked.connect(self.Manage_Button_Event)

        self.Quit_Button = QtGui.QPushButton('退出', self)
        self.Quit_Button.move(400, 400)
        self.Quit_Button.clicked.connect(QtCore.QCoreApplication.instance().quit)

        self.setWindowTitle('企业人事档案管理系统')

        '''
        # setGeometry(起点横坐标, 起点纵坐标, 宽, 高)
        self.setGeometry(500, 300, 700, 500)
        self.setWindowTitle('企业人事档案管理系统')
        self.show()
        '''

     def Scan_Button_Event(self):
         self.hide()
         print '---'
         ui = Scan_Page()
         ui.setGeometry(500, 300, 700, 550)
         ui.Get_Info()
         ui.show()
         ui.exec_()
         self.show()

     def Query_Button_Event(self):
        self.hide()
        print '---'
        ui = Query_Page()
        ui.setGeometry(500, 300, 700, 550)
        ui.show()
        ui.exec_()
        self.show()

     def Insert_Button_Event(self):
        print '===='
        self.hide()
        ui = Insert_Page()
        ui.setGeometry(500, 300, 750, 800)
        ui.initUI()
        ui.show()
        ui.exec_()
        self.show()

     def Count_Button_Event(self):
        self.hide()
        ui = Count_Page()
        ui.initUI()
        ui.setGeometry(500, 300, 700, 500)
        ui.show()
        ui.exec_()
        self.show()

     def Scan_Table_Button_Event(self):
        self.hide()
        ui = Table_scan()
        ui.initUI()
        ui.setGeometry(500, 300, 700, 500)
        ui.show()
        ui.exec_()
        self.show()

     def Person_Page_Button_Event(self):
        self.hide()
        ui = Person_Page()
        ui.initUI()
        ui.setGeometry(500, 300, 750, 800)
        ui.show()
        ui.exec_()
        self.show()

     def Manage_Button_Event(self):
        self.hide()
        ui = Sys_Page()
        ui.initUI()
        ui.setGeometry(500, 300, 700, 500)
        ui.show()
        ui.exec_()
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    ui = Ctrl_Function()
    ui.initUI()
    ui.setGeometry(500, 300, 700, 500)
    ui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
