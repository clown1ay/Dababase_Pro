 #-*-coding:utf-8-*-
import sys
import locale
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtGui
from PyQt4 import QtCore
from reset_page import Reset_Page
import Base_SQL

 # PyQt4中文显示
mycode = locale.getpreferredencoding()
code = QTextCodec.codecForName(mycode)
QTextCodec.setCodecForLocale(code)
QTextCodec.setCodecForTr(code)
QTextCodec.setCodecForCStrings(code)


# class Home2(QtGui.QWidget):
class Sys_Page(QtGui.QDialog):

    reset_function_signal = QtCore.pyqtSignal()
    backup_function_signal = QtCore.pyqtSignal()

    def __init__(self):
        super(Sys_Page, self).__init__()
        # self.initUI()

    def initUI(self):

        self.title = QtGui.QLabel('企业人事档案管理系统',self)
        self.title.setFont(QFont("Roman times",28,QFont.Bold))
        self.title.move(190, 70)


        self.Reset_Button = QtGui.QPushButton('修改密码', self)
        self.Reset_Button.move(300, 170)
        self.Reset_Button.clicked.connect(self.Reset_Button_Event)

        self.Backup_Button = QtGui.QPushButton('数据库备份', self)
        self.Backup_Button.move(170, 250)
        self.Backup_Button.clicked.connect(self.Backup_Button_Event)
        self.Backup_name = QtGui.QLabel('备份名称', self)
        self.Backup_name.move(290,250)
        self.Backup_nameEdit = QtGui.QLineEdit(self)
        self.Backup_nameEdit.move(370,250)

        self.Restore_Button = QtGui.QPushButton('数据库还原', self)
        self.Restore_Button.move(170, 350)
        self.Restore_Button.clicked.connect(self.Restore_Button_Event)
        self.Restore_name = QtGui.QLabel('还原名称', self)
        self.Restore_name.move(290,350)
        self.Restore_nameEdit = QtGui.QLineEdit(self)
        self.Restore_nameEdit.move(370,350)

        # setGeometry(起点横坐标, 起点纵坐标, 宽, 高)
        # self.setGeometry(500, 300, 700, 500)
        self.setWindowTitle('企业人事档案管理系统--系统管理')
        # self.show()

    def Reset_Button_Event(self):
        ui = Reset_Page()
        ui.initUI()
        ui.setGeometry(500, 300, 400, 300)
        ui.show()
        ui.exec_()


    def Backup_Button_Event(self):
        filename = str(self.Backup_nameEdit.text())
        backup = Base_SQL.SQL_Backup(filename)
        if backup == True:
            response = QtGui.QMessageBox.information(self, 'Message',"备份成功！", QtGui.QMessageBox.Yes)
        else:
            response = QtGui.QMessageBox.information(self, 'Message',"备份有误，请重新操作 ！", QtGui.QMessageBox.Yes)

    def Restore_Button_Event(self):
        filename = str(self.Restore_nameEdit.text())
        restore = Base_SQL.SQL_Restore(filename)
        if restore == True:
            response = QtGui.QMessageBox.information(self, 'Message',"还原成功！", QtGui.QMessageBox.Yes)
        else:
            response = QtGui.QMessageBox.information(self, 'Message',"还原有误，请重新操作 ！", QtGui.QMessageBox.Yes)


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Sys_Page()
    ex.initUI()
    ex.setGeometry(500, 300, 700, 500)
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
