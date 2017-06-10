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
class Count_Page(QtGui.QDialog):

    xb_function_signal = QtCore.pyqtSignal()
    bm_function_signal = QtCore.pyqtSignal()
    wh_function_signal = QtCore.pyqtSignal()
    zc_function_signal = QtCore.pyqtSignal()
    sum_function_signal = QtCore.pyqtSignal()

    def __init__(self):
        super(Count_Page, self).__init__()
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


        self.whcd_Button = QtGui.QPushButton('文 化统计', self)
        self.whcd_Button.move(100, 70)
        self.whcd_Button.clicked.connect(self.whcd_Button_Event)

        self.xb_Button = QtGui.QPushButton('性  别统计', self)
        self.xb_Button.move(100, 140)
        self.xb_Button.clicked.connect(self.xb_Button_Event)

        self.bm_Button = QtGui.QPushButton('部  门统计', self)
        self.bm_Button.move(100, 210)
        self.bm_Button.clicked.connect(self.bm_Button_Event)

        self.zc_Button = QtGui.QPushButton('职  称统计', self)
        self.zc_Button.move(100, 280)
        self.zc_Button.clicked.connect(self.zc_Button_Event)

        self.sum_Button = QtGui.QPushButton('人 数统计', self)
        self.sum_Button.move(100, 350)
        self.sum_Button.clicked.connect(self.sum_Button_Event)
        # self.sum_Button.clicked.connect(self.Commit_Button_Event)


        # setGeometry(起点横坐标, 起点纵坐标, 宽, 高)
        # self.setGeometry(500, 300, 750, 500)
        self.setWindowTitle('企业人事档案管理系统--信息统计')
        # self.show()

    def Set_Info(self, Info_dict, ttype):
        # 后续添加从数据库获取数据
        length = Info_dict['length']
        for row in range(length):
            for column in range(2):
                index_str = Info_dict['data'][row][column]
                if column == 1:
                    index_str = str(index_str)
                else:
                    if ttype == 'whcd':
                        index_str = Base_init.Read_whbm[str(index_str)]
                    elif ttype == 'zcbm':
                        print '---'
                        index_str = Base_init.Read_zcbm[str(index_str)]
                    elif ttype == 'bmbm':
                        index_str = Base_init.Read_bmbm[str(index_str)]
                # print index_str
                item = QStandardItem(index_str)
                self.model.setItem(row, column, item)

    def Clear_Info(self):
        #  清空表内原有数据
        for row in range(5):
            for column in range(2):
                self.model.setItem(row, column, QStandardItem(''))

    def xb_Button_Event(self):
        self.Clear_Info()
        self.model.setHorizontalHeaderLabels(['性别', '人数'])
        ttype = 'xb'
        Info_dict = Base_SQL.SQL_Count(ttype)
        self.Set_Info(Info_dict, ttype)

    def whcd_Button_Event(self):
        self.Clear_Info()
        self.model.setHorizontalHeaderLabels(['文化程度', '人数'])
        ttype = 'whcd'
        Info_dict = Base_SQL.SQL_Count(ttype)
        self.Set_Info(Info_dict, ttype)

    def bm_Button_Event(self):
        self.Clear_Info()
        self.model.setHorizontalHeaderLabels(['部门', '人数'])
        ttype = 'bmbm'
        Info_dict = Base_SQL.SQL_Count(ttype)
        self.Set_Info(Info_dict, ttype)

    def zc_Button_Event(self):
        self.Clear_Info()
        self.model.setHorizontalHeaderLabels(['职称', '人数'])
        ttype = 'zcbm'
        Info_dict = Base_SQL.SQL_Count(ttype)
        self.Set_Info(Info_dict, ttype)


    def sum_Button_Event(self):
        self.Clear_Info()
        self.model.setHorizontalHeaderLabels(['总计人数', '人数'])
        ttype = 'sum'
        Info_dict = Base_SQL.SQL_Count(ttype)
        self.Set_Info(Info_dict, ttype)







def main():
    app = QtGui.QApplication(sys.argv)
    ex = Count_Page()
    ex.initUI()
    ex.setGeometry(500, 300, 700, 500)
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
