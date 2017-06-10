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
class Query_Page(QtGui.QDialog):
    """docstring for myDialog"""

    Delete_function_signal = QtCore.pyqtSignal()
    Update_function_signal = QtCore.pyqtSignal()
    xm_Extract_function_signal = QtCore.pyqtSignal()
    xb_flurry_function_signal = QtCore.pyqtSignal()
    xb_Extract_function_signal = QtCore.pyqtSignal()
    xm_flurry_function_signal = QtCore.pyqtSignal()

    def __init__(self, arg=None):
        super(Query_Page, self).__init__(arg)
        # https://www.zhaokeli.com/article/7986.html

        self.model=QStandardItemModel(4,4);
        self.Headers = Base_init.column_name
        self.model.setHorizontalHeaderLabels(self.Headers)

        self.tableView=QTableView(self);
        self.tableView.setModel(self.model)
        self.tableView.setGeometry(QtCore.QRect(0, 0, 700, 350))

        self.xm_Extract_Button = QtGui.QPushButton('姓名精确查询', self)
        self.xm_Extract_Button.move(100, 450)
        self.xm_Extract_Button.clicked.connect(self.xm_Extract_Query)

        self.xm_Flurry_Button = QtGui.QPushButton('姓名模糊查询', self)
        self.xm_Flurry_Button.move(220, 450)
        self.xm_Flurry_Button.clicked.connect(self.xm_Flurry_Query)

        self.zgbm_Extract_Button = QtGui.QPushButton('编码精确查询', self)
        self.zgbm_Extract_Button.move(340, 450)
        self.zgbm_Extract_Button.clicked.connect(self.zgbm_Extract_Query)

        self.zgbm_Flurry_Button = QtGui.QPushButton('编码模糊查询', self)
        self.zgbm_Flurry_Button.move(460, 450)
        self.zgbm_Flurry_Button.clicked.connect(self.zgbm_Flurry_Query)


        self.Del_Button = QtGui.QPushButton('Delete', self)
        self.Del_Button.move(100, 390)
        self.Del_Button.clicked.connect(self.Del_Button_Event)

        self.Update_Button = QtGui.QPushButton('Update', self)
        self.Update_Button.move(220, 390)
        self.Update_Button.clicked.connect(self.Update_Button_Event)

        self.user = QtGui.QLabel('请输入：', self)
        self.user.move(390, 390)

        self.InputEdit = QtGui.QLineEdit(self)
        self.InputEdit.move(450, 390)

        self.Info = QtGui.QLabel('注：1.文化程度：本科、大专、硕士、博士、博士后;\n2.职称：处长、局长、科长、科员、实习;\n3.部门:培训部、外联部、项目部、人事部、财务部',self)
        self.Info.move(100, 480)


        # self.setGeometry(500, 300, 700, 500)
        self.setWindowTitle('企业人事档案信息浏览')
        # self.show()

    def Set_Info(self, Info_dict):
        # 后续添加从数据库获取数据
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


    def xm_Extract_Query(self):
        xm = self.InputEdit.text()
        # 1精确， 2 模糊
        Info_dict = Base_SQL.SQL_Query_xm(xm, '1')
        self.Set_Info(Info_dict)


    def xm_Flurry_Query(self):
        xm = self.InputEdit.text()
        # print xm
        # 1精确， 2 模糊
        Info_dict = Base_SQL.SQL_Query_xm(xm, '2')
        self.Set_Info(Info_dict)

    def zgbm_Extract_Query(self):
        zgbm = self.InputEdit.text()
        print zgbm
        # 1精确， 2 模糊
        Info_dict = Base_SQL.SQL_Query_zgbm(zgbm, '1')
        self.Set_Info(Info_dict)

    def zgbm_Flurry_Query(self):
        zgbm = self.InputEdit.text()
        print zgbm
        # 1精确， 2 模糊
        Info_dict = Base_SQL.SQL_Query_zgbm(zgbm, '2')
        self.Set_Info(Info_dict)


    def Del_Button_Event(self):
        row = self.tableView.currentIndex().row()
        column = self.tableView.currentIndex().column()
        zgbm = self.model.data(self.model.index(row, 0)).toString()
        print zgbm
        print row
        # 删除功能，在这里获取到ID，从库内删除
        Base_SQL.SQL_Del(zgbm)
        self.model.removeRow(row)
        print '删除成功！'


    def Update_Button_Event(self):
        row = self.tableView.currentIndex().row()
        column = self.tableView.currentIndex().column()

        column_name = self.Headers[column] # 获取列名
        column_name = Base_init.NameTOSQLname(column_name) #  转意

        zgbm = self.model.data(self.model.index(row, 0)).toString()

        update_content = self.InputEdit.text()
        Qupdate_content = QStandardItem(update_content)
        self.model.setItem(row, column, Qupdate_content)
        # 根据zgbm, updaet_content 和 column_name 转意后字段名称，修改数据库
        Base_SQL.SQL_Update(zgbm, column_name, update_content)
        # print update_content
        print '修改成功！ '




def main():
    app = QtGui.QApplication(sys.argv)
    ex = Query_Page()
    ex.setGeometry(500, 300, 700, 550)
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
