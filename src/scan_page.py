# -*-coding:utf-8-*-
import sys
import locale
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtGui
from PyQt4 import QtCore
from person_page import Person_Page
import Base_SQL
import Base_init
import Tofile
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


  # PyQt4中文显示
mycode = locale.getpreferredencoding()
code = QTextCodec.codecForName(mycode)
QTextCodec.setCodecForLocale(code)
QTextCodec.setCodecForTr(code)
QTextCodec.setCodecForCStrings(code)

# QDialog
class Scan_Page(QtGui.QDialog):
    """docstring for myDialog"""

    Delete_function_signal = QtCore.pyqtSignal()
    Update_function_signal = QtCore.pyqtSignal()
    toFile_function_signal = QtCore.pyqtSignal()

    def __init__(self, arg=None):
        super(Scan_Page, self).__init__(arg)
        # https://www.zhaokeli.com/article/7986.html

        self.model=QStandardItemModel(4,4);
        self.Headers = Base_init.column_name
        self.model.setHorizontalHeaderLabels(self.Headers)

        self.tableView=QTableView(self);
        self.tableView.setModel(self.model)
        self.tableView.setGeometry(QtCore.QRect(0, 0, 700, 400))

        self.toFile_Button = QtGui.QPushButton('导出数据', self)
        self.toFile_Button.move(70, 430)
        self.toFile_Button.clicked.connect(self.toFile_Button_Event)

        self.Del_Button = QtGui.QPushButton('Delete', self)
        self.Del_Button.move(180, 430)
        self.Del_Button.clicked.connect(self.Del_Button_Event)

        self.Update_Button = QtGui.QPushButton('Update', self)
        self.Update_Button.move(290, 430)
        self.Update_Button.clicked.connect(self.Update_Button_Event)

        self.UpdateEdit = QtGui.QLineEdit(self)
        self.UpdateEdit.move(390, 430)

        self.Info = QtGui.QLabel('注：1.文化程度：本科、大专、硕士、博士、博士后;\n2.职称：处长、局长、科长、科员、实习;\n3.部门:培训部、外联部、项目部、人事部、财务部',self)
        self.Info.move(100, 470)

        self.Person_Button = QtGui.QPushButton('个人报表', self)
        self.Person_Button.move(540, 430)
        self.Person_Button.clicked.connect(self.Person_Button_Event)

        # self.setGeometry(500, 300, 700, 500)
        self.setWindowTitle('企业人事档案信息浏览')
        # self.show()

    def Get_Info(self):
        # 后续添加从数据库获取数据
        Info_dict = Base_SQL.SQL_Scan()
        length = Info_dict['length']
        for row in range(length):
            for column in range(31):
                index_str = Info_dict['data'][row][column]
                if column == 0:
                    index_str = str(index_str)
                elif column == 6:
                    index_str = Base_init.Read_whbm[str(index_str)]
                elif column == 9:
                    index_str = Base_init.Read_zcbm[str(index_str)]
                elif column == 30:
                    index_str = Base_init.Read_bmbm[str(index_str)]
                # print index_str
                item = QStandardItem(index_str)
                self.model.setItem(row, column, item)

    def toFile_Button_Event(self):
        Info_dict = Base_SQL.SQL_Scan()
        Tofile.Gene_file('All_data', Info_dict['data'])
        response = QtGui.QMessageBox.information(self, 'Message',"导出文件成功！", QtGui.QMessageBox.Yes)



    def Del_Button_Event(self):
        row = self.tableView.currentIndex().row()
        column = self.tableView.currentIndex().column()
        zgbm = self.model.data(self.model.index(row, 0)).toString()
        # 删除功能，在这里获取到ID，从库内删除
        delete = Base_SQL.SQL_Del(zgbm)
        if delete == True:
            response = QtGui.QMessageBox.information(self, 'Message',"删除成功！", QtGui.QMessageBox.Yes)
            self.model.removeRow(row)
        else:
            response = QtGui.QMessageBox.information(self, 'Message',"删除失败！", QtGui.QMessageBox.Yes)


    def Update_Button_Event(self):
        row = self.tableView.currentIndex().row()
        column = self.tableView.currentIndex().column()

        column_name = self.Headers[column] # 获取列名
        column_name = Base_init.NameTOSQLname(column_name) #  转意

        zgbm = self.model.data(self.model.index(row, 0)).toString()

        update_content = self.UpdateEdit.text()
        Qupdate_content = QStandardItem(update_content)
        self.model.setItem(row, column, Qupdate_content)
        # 根据zgbm, updaet_content 和 column_name 转意后字段名称，修改数据库
        update = Base_SQL.SQL_Update(zgbm, column_name, update_content)
        if update == True:
            response = QtGui.QMessageBox.information(self, 'Message',"修改成功！", QtGui.QMessageBox.Yes)
        else:
            response = QtGui.QMessageBox.information(self, 'Message',"修改失败！", QtGui.QMessageBox.Yes)


    def Person_Button_Event(self):
        row = self.tableView.currentIndex().row()
        zgbm = self.model.data(self.model.index(row, 0)).toString()
        self.hide()
        ex = Person_Page()
        ex.initUI()
        ex.Out_Query_Button_Event(zgbm)
        ex.setGeometry(500, 300, 750, 800)
        ex.show()
        ex.exec_()
        self.show()




def main():
    app = QtGui.QApplication(sys.argv)
    ex = Scan_Page()
    ex.setGeometry(500, 300, 700, 550)
    ex.Get_Info()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
