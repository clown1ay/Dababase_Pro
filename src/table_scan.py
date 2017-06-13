 #-*-coding:utf-8-*-
import sys
import locale
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtGui
from PyQt4 import QtCore
import Base_init
import Base_SQL
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


 # PyQt4中文显示
mycode = locale.getpreferredencoding()
code = QTextCodec.codecForName(mycode)
QTextCodec.setCodecForLocale(code)
QTextCodec.setCodecForTr(code)
QTextCodec.setCodecForCStrings(code)


# class Home2(QtGui.QWidget):
class Table_scan(QtGui.QDialog):

    scan_function_signal = QtCore.pyqtSignal()
    del_function_signal = QtCore.pyqtSignal()
    update_function_signal = QtCore.pyqtSignal()
    # zc_function_signal = QtCore.pyqtSignal()
    # sum_function_signal = QtCore.pyqtSignal()

    def __init__(self):
        super(Table_scan, self).__init__()
        # self.initUI()

    def initUI(self):
        '''
        self.zgbm = QtGui.QLabel('职工编码',self)
        self.zgbm.move(30, 40)
        self.zgbmEdit = QtGui.QLineEdit(self)
        self.zgbmEdit.move(110, 40)
        self.zgbmEdit.setText('系统生成')
        '''
        self.model=QStandardItemModel(5,2);
        # self.Headers = Base_init.column_name
        # self.model.setHorizontalHeaderLabels(self.Headers)

        self.tableView=QTableView(self);
        self.tableView.setModel(self.model)
        self.tableView.setGeometry(QtCore.QRect(300, 70, 230, 300))



        self.chooseBox = QtGui.QComboBox(self)
        self.chooseBox.addItems(['文化程度表','部门表','职称表'])
        self.chooseBox.move(100, 70)

        self.scan_Button = QtGui.QPushButton('查看表', self)
        self.scan_Button.move(100, 140)
        self.scan_Button.clicked.connect(self.scan_Button_Event)

        self.del_Button = QtGui.QPushButton('删除', self)
        self.del_Button.move(100, 210)
        self.del_Button.clicked.connect(self.del_Button_Event)

        self.update_Button = QtGui.QPushButton('修改', self)
        self.update_Button.move(100, 280)
        self.update_Button.clicked.connect(self.update_Button_Event)

        self.updateEdit = QtGui.QLineEdit(self)
        self.updateEdit.move(100, 330)

        self.insert_Button = QtGui.QPushButton('插入', self)
        self.insert_Button.move(100, 400)
        self.insert_Button.clicked.connect(self.insert_Button_Event)

        self.new_bm = QtGui.QLabel('编码',self)
        self.new_bm.move(220, 400)
        self.new_bmEdit = QtGui.QLineEdit(self)
        self.new_bmEdit.move(250, 400)

        self.new_name = QtGui.QLabel('名称',self)
        self.new_name.move(400, 400)
        self.new_nameEdit = QtGui.QLineEdit(self)
        self.new_nameEdit.move(430, 400)

        # setGeometry(起点横坐标, 起点纵坐标, 宽, 高)
        # self.setGeometry(500, 300, 750, 500)
        self.setWindowTitle('企业人事档案管理系统--相关表查看')
        # self.show()

    def Clear_Info(self):
        #  清空表内原有数据
        for row in range(10):
            for column in range(2):
                self.model.setItem(row, column, QStandardItem(''))


    def Set_Info(self, Info_dict):
        # 后续添加从数据库获取数据
        self.Clear_Info()
        length = Info_dict['length']
        for row in range(length):
            for column in range(2):
                index_str = Info_dict['data'][row][column]
                item = QStandardItem(str(index_str))
                self.model.setItem(row, column, item)

    # 表名转译
    def Type_trans(self, table_type):
        if table_type == '文化程度表':
            ttype = 'whcd'
        elif table_type == '部门表':
            ttype = 'bm'
        elif table_type == '职称表':
            ttype = 'zc'
        return ttype

    # 查看表信息
    def scan_Button_Event(self):
        table_type = str(self.chooseBox.currentText())
        print table_type
        if table_type == '文化程度表':
            self.model.setHorizontalHeaderLabels(['文化程度编码', '文化程度'])
            ttype = 'whcd'
        elif table_type == '部门表':
            self.model.setHorizontalHeaderLabels(['部门编码', '部门'])
            ttype = 'bm'
        elif table_type == '职称表':
            self.model.setHorizontalHeaderLabels(['职称编码', '职称'])
            ttype = 'zc'
        Info_dict = Base_SQL.SQL_Scan_Tables(ttype)
        self.Set_Info(Info_dict)

        # 更改内容
    def update_Button_Event(self):
        table_type = str(self.chooseBox.currentText())
        ttype = self.Type_trans(table_type)# 得到表类型
        row = self.tableView.currentIndex().row()
        column = self.tableView.currentIndex().column() # column=1代表修改具体名称， column=0代表修改编码
        column_bm = self.model.data(self.model.index(row, 0)).toString()# 得到修改字段的编码
        update_content = self.updateEdit.text()
        update = Base_SQL.SQL_Update_Tables(ttype, column_bm, column, update_content)
        if update == True:
            Qupdate_content = QStandardItem(update_content)
            self.model.setItem(row, column, Qupdate_content)
            response = QtGui.QMessageBox.information(self, 'Message',"修改成功！", QtGui.QMessageBox.Yes)
        else:
            response = QtGui.QMessageBox.information(self, 'Message',"修改失败！", QtGui.QMessageBox.Yes)


        # 插入新的信息
    def insert_Button_Event(self):
        table_type = str(self.chooseBox.currentText())
        ttype = self.Type_trans(table_type)# 得到表类型
        new_bm = self.new_bmEdit.text()
        new_name = self.new_nameEdit.text()
        insert = Base_SQL.SQL_Insert_Tables(ttype, new_bm, new_name)
        if insert == True:
            response = QtGui.QMessageBox.information(self, 'Message',"插入成功！", QtGui.QMessageBox.Yes)
        else:
            response = QtGui.QMessageBox.information(self, 'Message',"插入失败！", QtGui.QMessageBox.Yes)


    def del_Button_Event(self):
        table_type = str(self.chooseBox.currentText())
        ttype = self.Type_trans(table_type)# 得到表类型
        row = self.tableView.currentIndex().row()
        column_bm = self.model.data(self.model.index(row, 0)).toString()# 获取row行，0列数据，即该行编码
        print column_bm
        delete = Base_SQL.SQL_Del_Tables(ttype, column_bm)
        if delete == True:
            self.model.removeRow(row)
            response = QtGui.QMessageBox.information(self, 'Message',"删除成功！", QtGui.QMessageBox.Yes)
        else:
            response = QtGui.QMessageBox.information(self, 'Message',"删除失败！", QtGui.QMessageBox.Yes)





def main():
    app = QtGui.QApplication(sys.argv)
    ex = Table_scan()
    ex.initUI()
    ex.setGeometry(500, 300, 700, 500)
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
