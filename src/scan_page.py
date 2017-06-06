# -*-coding:utf-8-*-
import sys
import locale
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtGui
from PyQt4 import QtCore


  # PyQt4中文显示
mycode = locale.getpreferredencoding()
code = QTextCodec.codecForName(mycode)
QTextCodec.setCodecForLocale(code)
QTextCodec.setCodecForTr(code)
QTextCodec.setCodecForCStrings(code)

# QDialog
class Scan_Page(QtGui.QWidget):
    """docstring for myDialog"""
    def __init__(self, arg=None):
        super(Scan_Page, self).__init__(arg)
        # https://www.zhaokeli.com/article/7986.html

        # self.setWindowTitle("first window")
        # self.setWindowFlags(Qt.WindowMaximizeButtonHint|Qt.WindowMinimizeButtonHint|Qt.WindowCloseButtonHint)
        # self.resize(500,300);

        model=QStandardItemModel(4,4);
        model.setHorizontalHeaderLabels(['标题1', '标题2', '标题3',' 标题4', '标题4', '标题4', '标题2', '标题2', '标题2', '标题2', '标题2', '标题2', '标题2', '标题2'])
        for row in range(20):
            for column in range(4):
                item = QStandardItem("row %s, column %s"%(row,column))
                model.setItem(row, column, item)
        tableView=QTableView();
        tableView.setModel(model)

        test_Button = QtGui.QPushButton('登录')

        self.dlgLayout=QVBoxLayout();
        self.dlgLayout.addWidget(tableView)
        # self.dlgLayout.addWidget(test_Button) # 这里可以添加button
        self.setLayout(self.dlgLayout)

        self.setGeometry(500, 300, 700, 500)
        self.setWindowTitle('企业人事档案管理系统')
        self.show()


def main():
    # app = QApplication(sys.argv)
    #全局设置QPushButton的背景样式
    # dlg = myDialog()
    # dlg.show()
    # dlg.exec_()
    # app.exit()
    app = QtGui.QApplication(sys.argv)
    ex = Scan_Page()
    sys.exit(app.exec_())
    # app = QtGui.QApplication(sys.argv)
    # ex = Scan_Function()
    # sys.exit(app.exec_())


if __name__ == '__main__':
    main()
