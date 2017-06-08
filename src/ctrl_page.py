# -*-coding:utf-8-*-
import sys
import locale
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtGui
from PyQt4 import QtCore
from scan_page import Scan_Page


  # PyQt4中文显示
mycode = locale.getpreferredencoding()
code = QTextCodec.codecForName(mycode)
QTextCodec.setCodecForLocale(code)
QTextCodec.setCodecForTr(code)
QTextCodec.setCodecForCStrings(code)


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

# 功能控制页
class Ctrl_Function(QtGui.QDialog):

     Scanl_function_signal = QtCore.pyqtSignal()

     def __init__(self):
         super(Ctrl_Function, self).__init__()
         # self.initUI()

     def initUI(self):


        self.Scan_Button = QtGui.QPushButton('浏览全部', self)
        self.Scan_Button.move(200, 100)
        self.Scan_Button.clicked.connect(self.Scan_Button_Event)

        self.Count_Button = QtGui.QPushButton('统计', self)
        self.Count_Button.move(200, 200)

        self.Manage_Button = QtGui.QPushButton('系统管理', self)
        self.Manage_Button.move(200, 300)

        self.Query_Button = QtGui.QPushButton('查询', self)
        self.Query_Button.move(400, 100)

        self.Insert_Button = QtGui.QPushButton('录入', self)
        self.Insert_Button.move(400, 200)

        self.furry_Button = QtGui.QPushButton('###', self)
        self.furry_Button.move(400, 300)

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
         ui.setGeometry(500, 300, 700, 500)
         ui.Get_Info()
         ui.show()
         ui.exec_()

def main():
    app = QtGui.QApplication(sys.argv)
    ui = Ctrl_Function()
    ui.initUI()
    ui.setGeometry(500, 300, 700, 500)
    ui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
