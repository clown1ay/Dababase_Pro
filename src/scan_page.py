# -*-coding:utf-8-*-
import sys
import locale
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtGui
from PyQt4 import QtCore
import Base_SQL
import Base_init
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
    # Ctrlpage_function_signal = QtCore.pyqtSignal()

    def __init__(self, arg=None):
        super(Scan_Page, self).__init__(arg)
        # https://www.zhaokeli.com/article/7986.html

        self.model=QStandardItemModel(4,4);
        self.Headers = Base_init.column_name
        self.model.setHorizontalHeaderLabels(self.Headers)

        self.tableView=QTableView(self);
        self.tableView.setModel(self.model)
        self.tableView.setGeometry(QtCore.QRect(0, 0, 700, 400))

        self.Ctrlpage_Button = QtGui.QPushButton('回首页', self)
        self.Ctrlpage_Button.move(100, 430)
        # self.Ctrlpage_Button.clicked.connect(self.exec_())

        self.Del_Button = QtGui.QPushButton('Delete', self)
        self.Del_Button.move(230, 430)
        self.Del_Button.clicked.connect(self.Del_Button_Event)

        self.Update_Button = QtGui.QPushButton('Update', self)
        self.Update_Button.move(360, 430)
        self.Update_Button.clicked.connect(self.Update_Button_Event)

        self.UpdateEdit = QtGui.QLineEdit(self)
        self.UpdateEdit.move(450, 430)


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


    def Del_Button_Event(self):
        row = self.tableView.currentIndex().row()
        column = self.tableView.currentIndex().column()
        zgbm = self.model.data(self.model.index(row, 0)).toString()
        # 删除功能，在这里获取到ID，从库内删除
        # Base_SQL.SQL_Del(zgbm)
        self.model.removeRow(row)
        print '删除成功！'


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
        Base_SQL.SQL_Update(zgbm, column_name, update_content)
        # print update_content
        print '修改成功！ '


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Scan_Page()
    ex.setGeometry(500, 300, 700, 500)
    ex.Get_Info()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
