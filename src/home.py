 #-*-coding:utf-8-*-
import sys
import locale
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtGui
from PyQt4 import QtCore
from ctrl_page import Ctrl_Page

 # PyQt4中文显示
mycode = locale.getpreferredencoding()
code = QTextCodec.codecForName(mycode)
QTextCodec.setCodecForLocale(code)
QTextCodec.setCodecForTr(code)
QTextCodec.setCodecForCStrings(code)

# app = QtGui.QApplication(sys.argv)

# 用户登录首页
class Home(QtGui.QWidget):

    ctrl_function_signal = QtCore.pyqtSignal()

    def __init__(self):
        super(Home, self).__init__()
        # self.initUI()

    def initUI(self, Form):

        self.title = QtGui.QLabel('企业人事档案管理系统',self)
        self.title.setFont(QFont("Roman times",28,QFont.Bold))
        self.title.move(190, 70)

        self.user = QtGui.QLabel('user', self)
        self.user.move(230, 180)
        self.user.setFont(QFont("Times",15,QFont.Bold))

        self.password = QtGui.QLabel('password', self)
        self.password.move(220,250)
        self.password.setFont(QFont("Times",15,QFont.Bold))

        self.userEdit = QtGui.QLineEdit(self)
        self.userEdit.move(310, 180)

        self.passwordEdit = QtGui.QLineEdit(self)
        self.passwordEdit.move(310, 250)

        self.quit_Button = QtGui.QPushButton('退出', self)
        self.quit_Button.move(400, 330)
        self.quit_Button.clicked.connect(QtCore.QCoreApplication.instance().quit)

        self.login_Button = QtGui.QPushButton('登录', self)
        self.login_Button.move(240, 330)
        self.login_Button.clicked.connect(self.login_Button_Event)

        # setGeometry(起点横坐标, 起点纵坐标, 宽, 高)
        self.setGeometry(500, 300, 700, 500)
        self.setWindowTitle('企业人事档案管理系统')
        self.show()

    def login_Button_Event(self):
        # self.userEdit.setText('ssso')
        username = self.userEdit.text()
        password = self.passwordEdit.text()
        QtCore.QCoreApplication.instance().quit
        # if username == 'admin' and password == 'admin123':
        # app=QtGui.QApplication.instance()  # checks if QApplication already exists
        # if not app:    # create QApplication if it doesnt exist
        ex = Ctrl_Page()
        ex.initUI()
        sys.exit(app.exec_())
        # else:
            # 对话框提示重新输入
            # pass


def main():
    app = QtGui.QApplication(sys.argv)
    form = QtGui.QWidget()
    ex = Home()
    ex.initUI(form)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
