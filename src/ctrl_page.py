# -*-coding:utf-8-*-
import sys
import locale
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtGui
from PyQt4 import QtCore


  # PyQt4中文显示
mycode = locale.getpreferredencoding()
code = QTextCodec.codecForName(mycode)
QTextCodec.setCodecForLocale(code)
QTextCodec.setCodecForTr(code)
QTextCodec.setCodecForCStrings(code)

# 功能控制页
class Ctrl_Page(QtGui.QWidget):

     def __init__(self):
         super(Ctrl_Page, self).__init__()
         # self.initUI()

     def initUI(self):

        self.Scan_Button = QtGui.QPushButton('浏览全部', self)
        self.Scan_Button.move(200, 100)

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


        # setGeometry(起点横坐标, 起点纵坐标, 宽, 高)
        self.setGeometry(500, 300, 700, 500)
        self.setWindowTitle('企业人事档案管理系统')
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Ctrl_Page()
    ex.initUI()
    sys.exit(app.exec_())
    # app = QtGui.QApplication(sys.argv)
    # Dialog = QtGui.QDialog()
    # ui = Ctrl_Function()
    # ui.initUI(Dialog)
    # Dialog.show()
    # sys.exit(app.exec_())



if __name__ == '__main__':
    main()
