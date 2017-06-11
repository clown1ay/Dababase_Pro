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

    # xb_function_signal = QtCore.pyqtSignal()
    # bm_function_signal = QtCore.pyqtSignal()
    # wh_function_signal = QtCore.pyqtSignal()
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


        self.whcd_Button = QtGui.QPushButton('文化程度表', self)
        self.whcd_Button.move(100, 70)
        # self.whcd_Button.clicked.connect(self.whcd_Button_Event)

        self.xb_Button = QtGui.QPushButton('职称', self)
        self.xb_Button.move(100, 140)
        # self.xb_Button.clicked.connect(self.xb_Button_Event)

        self.bm_Button = QtGui.QPushButton('部门表', self)
        self.bm_Button.move(100, 210)
        # self.bm_Button.clicked.connect(self.bm_Button_Event)




        # setGeometry(起点横坐标, 起点纵坐标, 宽, 高)
        # self.setGeometry(500, 300, 750, 500)
        self.setWindowTitle('企业人事档案管理系统--相关表查看')
        # self.show()




def main():
    app = QtGui.QApplication(sys.argv)
    ex = Table_scan()
    ex.initUI()
    ex.setGeometry(500, 300, 700, 500)
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
