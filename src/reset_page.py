 #-*-coding:utf-8-*-
import sys
import locale
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtGui
from PyQt4 import QtCore
import Base_SQL

 # PyQt4中文显示
mycode = locale.getpreferredencoding()
code = QTextCodec.codecForName(mycode)
QTextCodec.setCodecForLocale(code)
QTextCodec.setCodecForTr(code)
QTextCodec.setCodecForCStrings(code)


# class Home2(QtGui.QWidget):
class Reset_Page(QtGui.QDialog):

    def __init__(self):
        super(Reset_Page, self).__init__()
        # self.initUI()

    def initUI(self):

        self.password = QtGui.QLabel('原密码',self)
        self.password.move(100, 90)
        self.passwordEdit = QtGui.QLineEdit(self)
        self.passwordEdit.setEchoMode(QLineEdit.Password)
        self.passwordEdit.move(170, 90)

        self.new_password  = QtGui.QLabel('新密码',self)
        self.new_password.move(100, 130)
        self.new_passwordEdit = QtGui.QLineEdit(self)
        self.new_passwordEdit.setEchoMode(QLineEdit.Password)
        self.new_passwordEdit.move(170, 130)

        self.assure_passwd = QtGui.QLabel('密码确认',self)
        self.assure_passwd.move(100, 170)
        self.assure_passwdEdit = QtGui.QLineEdit(self)
        self.assure_passwdEdit.setEchoMode(QLineEdit.Password)
        self.assure_passwdEdit.move(170, 170)

        self.OK_Button = QtGui.QPushButton('确认', self)
        self.OK_Button.move(150, 220)
        self.OK_Button.clicked.connect(self.OK_Button_Event)

        # setGeometry(起点横坐标, 起点纵坐标, 宽, 高)
        # self.setGeometry(500, 300, 700, 500)
        self.setWindowTitle('企业人事档案管理系统--密码重置')
        # self.show()

    def OK_Button_Event(self):
        new_password = self.new_passwordEdit.text()
        assure_passwd = self.assure_passwdEdit.text()
        # print new_passwrod, assure_passwd
        if new_password != assure_passwd:
            response = QtGui.QMessageBox.information(self, 'Message',"两次密码不一致", QtGui.QMessageBox.Yes)
        password = self.passwordEdit.text()
        verify = Base_SQL.SQL_verify(password)
        if verify == True:
            reset = Base_SQL.SQL_Reset(new_password)
            if reset:
                response = QtGui.QMessageBox.information(self, 'Message',"重置成功！", QtGui.QMessageBox.Yes)
            else:
                response = QtGui.QMessageBox.information(self, 'Message',"重置失败！", QtGui.QMessageBox.Yes)
        else:
            response = QtGui.QMessageBox.information(self, 'Message',"原密码错误！", QtGui.QMessageBox.Yes)


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Reset_Page()
    ex.initUI()
    ex.setGeometry(500, 300, 400, 300)
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
