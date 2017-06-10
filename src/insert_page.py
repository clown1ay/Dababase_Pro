 #-*-coding:utf-8-*-
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


# class Home2(QtGui.QWidget):
class Insert_Page(QtGui.QDialog):

    # ctrl_function_signal = QtCore.pyqtSignal()

    def __init__(self):
        super(Insert_Page, self).__init__()
        # self.initUI()

    def initUI(self):

        # Form.setObjectName(_fromUtf8("Form"))
        # Form.resize(700, 500)
        # self.form = Form

        self.zgbm = QtGui.QLabel('职工编码',self)
        self.zgbm.move(30, 40)
        self.zgbmEdit = QtGui.QLineEdit(self)
        self.zgbmEdit.move(110, 40)

        self.xm = QtGui.QLabel('姓   名',self)
        self.xm.move(30, 80)
        self.xm = QtGui.QLineEdit(self)
        self.xm.move(110, 80)

        self.xb = QtGui.QLabel('性   别',self)
        self.xb.move(30, 120)
        self.xb = QtGui.QLineEdit(self)
        self.xb.move(110, 120)

        self.mz = QtGui.QLabel('民   族',self)
        self.mz.move(30, 160)
        self.mz = QtGui.QLineEdit(self)
        self.mz.move(110, 160)

        self.csny = QtGui.QLabel('出生年月 ',self)
        self.csny.move(30, 200)
        self.csny = QtGui.QLineEdit(self)
        self.csny.move(110, 200)

        self.hyzk = QtGui.QLabel('婚姻状况 ',self)
        self.hyzk.move(30, 240)
        self.hyzk = QtGui.QLineEdit(self)
        self.hyzk.move(110, 240)

        self.whcd = QtGui.QLabel('文化程度 ',self)
        self.whcd.move(30, 280)
        self.whcdBox = QtGui.QComboBox(self)
        self.whcdBox.addItems(['hello', 'good'])
        self.whcdBox.move(110, 280)

        self.jkzk = QtGui.QLabel('健康状况 ',self)
        self.jkzk.move(30, 320)
        self.jkzkBox = QtGui.QComboBox(self)
        self.jkzkBox.addItems(['hello', 'good'])
        self.jkzkBox.move(110, 320)

        self.zzmm = QtGui.QLabel('政治面貌 ',self)
        self.zzmm.move(30, 360)
        self.zzmmBox = QtGui.QComboBox(self)
        self.zzmmBox.addItems(['hello', 'good'])
        self.zzmmBox.move(110, 360)


        self.jg = QtGui.QLabel('籍   贯',self)
        self.jg.move(270, 40)
        self.jgEdit = QtGui.QLineEdit(self)
        self.jgEdit.move(340, 40)

        self.sfzh = QtGui.QLabel('身份证号',self)
        self.sfzh.move(270, 80)
        self.sfzhEdit = QtGui.QLineEdit(self)
        self.sfzhEdit.move(340, 80)

        self.byxx = QtGui.QLabel('毕业学校',self)
        self.byxx.move(270, 120)
        self.byxxEdit = QtGui.QLineEdit(self)
        self.byxxEdit.move(340, 120)

        self.zytc = QtGui.QLabel('专业特长',self)
        self.zytc.move(270, 160)
        self.zytcEdit = QtGui.QLineEdit(self)
        self.zytcEdit.move(340, 160)

        self.hkszd = QtGui.QLabel('户口所在',self)
        self.hkszd.move(270, 200)
        self.hkszdEdit = QtGui.QLineEdit(self)
        self.hkszdEdit.move(340, 200)

        self.hkxz = QtGui.QLabel('户口性质',self)
        self.hkxz.move(270, 240)
        self.hkxzEdit = QtGui.QLineEdit(self)
        self.hkxzEdit.move(340, 240)

        self.xzz = QtGui.QLabel('现住址',self)
        self.xzz.move(270, 280)
        self.xzzEdit = QtGui.QLineEdit(self)
        self.xzzEdit.move(340, 280)

        self.zw = QtGui.QLabel('职务',self)
        self.zw.move(270, 320)
        self.zwBox = QtGui.QComboBox(self)
        self.zwBox.addItems(['hello', 'good'])
        self.zwBox.move(340, 320)

        self.gzm = QtGui.QLabel('工种名  ',self)
        self.gzm.move(270, 360)
        self.gzmEdit = QtGui.QLineEdit(self)
        self.gzmEdit.move(340, 360)



        self.tbrqm = QtGui.QLabel('填表人签名',self)
        self.tbrqm.move(510, 40)
        self.tbrqmEdit = QtGui.QLineEdit(self)
        self.tbrqmEdit.move(600, 40)

        self.tbrq = QtGui.QLabel('填表日期',self)
        self.tbrq.move(510, 80)
        self.tbrqEdit = QtGui.QLineEdit(self)
        self.tbrqEdit.move(600, 80)

        self.scyj = QtGui.QLabel('审查意见',self)
        self.scyj.move(510, 120)
        self.scyjEdit = QtGui.QLineEdit(self)
        self.scyjEdit.move(600, 120)

        self.scrq = QtGui.QLabel('审查日期',self)
        self.scrq.move(510, 160)
        self.scrqEdit = QtGui.QLineEdit(self)
        self.scrqEdit.move(600, 160)

        self.ryxz = QtGui.QLabel('人员性质',self)
        self.ryxz.move(510, 200)
        self.ryxzEdit = QtGui.QLineEdit(self)
        self.ryxzEdit.move(600, 200)

        self.rcsj = QtGui.QLabel('入厂时间',self)
        self.rcsj.move(510, 240)
        self.rcsjEdit = QtGui.QLineEdit(self)
        self.rcsjEdit.move(600, 240)

        self.ryzt = QtGui.QLabel('人员状态',self)
        self.ryzt.move(510, 280)
        self.ryztEdit = QtGui.QLineEdit(self)
        self.ryztEdit.move(600, 280)

        self.szbm = QtGui.QLabel('所在部门',self)
        self.szbm.move(510, 320)
        self.szbmBox = QtGui.QComboBox(self)
        self.szbmBox.addItems(['hello', 'good'])
        self.szbmBox.move(600, 320)

        self.zc = QtGui.QLabel('职   称',self)
        self.zc.move(510, 360)
        self.zcBox = QtGui.QComboBox(self)
        self.zcBox.addItems(['hello', 'good'])
        self.zcBox.move(600, 360)


        # self.whcd = QtGui.QComboBox(self)
        # self.whcd.addItems(['hello', 'good'])




        # self.zgbmEdit = QtGui.QLineEdit(self)
        # self.zgbmEdit.move(110, 80)



        # self.jgEdit = QtGui.QLineEdit(self)
        # self.jgEdit.move(600, 40)

        # self.quit_Button = QtGui.QPushButton('退出', self)
        # self.quit_Button.move(400, 330)
        # self.quit_Button.clicked.connect(QtCore.QCoreApplication.instance().quit)


        # setGeometry(起点横坐标, 起点纵坐标, 宽, 高)
        # self.setGeometry(500, 300, 750, 500)
        self.setWindowTitle('企业人事档案管理系统--信息录入')
        # self.show()




def main():
    app = QtGui.QApplication(sys.argv)
    ex = Insert_Page()
    ex.initUI()
    ex.setGeometry(500, 300, 750, 500)
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
