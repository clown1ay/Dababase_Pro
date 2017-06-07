 #-*-coding:utf-8-*-
import sys
import locale
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtGui
from PyQt4 import QtCore
from ctrl_page import Ctrl_Function

 # PyQt4中文显示
mycode = locale.getpreferredencoding()
code = QTextCodec.codecForName(mycode)
QTextCodec.setCodecForLocale(code)
QTextCodec.setCodecForTr(code)
QTextCodec.setCodecForCStrings(code)


# class Home2(QtGui.QWidget):
class Home(QtGui.QDialog):

    ctrl_function_signal = QtCore.pyqtSignal()

    def __init__(self):
        super(Home, self).__init__()
        # self.initUI()

    def initUI(self):

        # Form.setObjectName(_fromUtf8("Form"))
        # Form.resize(700, 500)
        # self.form = Form
	'''
        self.title = QtGui.QLabel(Form)
        self.title.setGeometry(QtCore.QRect(190, 40, 54, 16))
        # self.title.setObjectName(_fromUtf8("企业人事档案管理系统"))
        self.title.setFont(QFont("Roman times",15,QFont.Bold))
        self.title.setText(_translate("Form", "企业人事档案管理系统", None))
        print '---'
	'''

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

	'''
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(70, 90, 75, 23))
        # elf.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.setText(_translate("Form", "dialog1", None))
        self.pushButton.clicked.connect(self.login_Button_Event)
	'''

        self.login_Button = QtGui.QPushButton('登录', self)
        self.login_Button.move(240, 330)
        self.login_Button.clicked.connect(self.login_Button_Event)


        # setGeometry(起点横坐标, 起点纵坐标, 宽, 高)
        self.setGeometry(500, 300, 700, 500)
        self.setWindowTitle('企业人事档案管理系统')
        self.show()

    def login_Button_Event(self):
        username = self.userEdit.text()
        password = self.passwordEdit.text()
        if username == 'admin' and password == 'admin123':
            print '0'
            self.hide()
            # self.exec_()
            ui = Ctrl_Function()
            ui.initUI()
            ui.setGeometry(500, 300, 700, 500)
            ui.show()
            ui.exec_()
            # self.show()
        else:
            print '---'
            pass


def main():
    app = QtGui.QApplication(sys.argv)
    # form = QtGui.QWidget()
    ex = Home()
    ex.initUI()
    # form.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
