 #-*-coding:utf-8-*-
import sys
import locale
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtGui

 # PyQt4中文显示
mycode = locale.getpreferredencoding()
code = QTextCodec.codecForName(mycode)
QTextCodec.setCodecForLocale(code)
QTextCodec.setCodecForTr(code)
QTextCodec.setCodecForCStrings(code)


class Home(QtGui.QWidget):

    def __init__(self):
        super(Home, self).__init__()
        self.initUI()

    def initUI(self):
        # setGeometry(起点横坐标, 起点纵坐标, 宽, 高)
        self.setGeometry(500, 300, 750, 550)
        self.setWindowTitle('企业人事档案管理系统')

        lbl1 = QtGui.QLabel('企业人事档案管理系统', self)
        lbl1.move(100, 200)

        user = QtGui.QLabel('user')
        password = QtGui.QLabel('password')

        userEdit = QtGui.QLineEdit()
        passwordEdit = QtGui.QLineEdit()

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(user, 1, 0)
        grid.addWidget(userEdit, 1, 1)

        grid.addWidget(password, 2, 0)
        grid.addWidget(passwordEdit, 2, 1)

        self.setLayout(grid)

        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Home()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
