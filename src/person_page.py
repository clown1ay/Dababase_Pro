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


class Person_Page(QtGui.QDialog):

    Query_function_signal = QtCore.pyqtSignal()

    def __init__(self):
        super(Person_Page, self).__init__()
        # self.initUI()

    def initUI(self):

        # Form.setObjectName(_fromUtf8("Form"))
        # Form.resize(700, 500)
        # self.form = Form

        self.zgbm = QtGui.QLabel('职工编码',self)
        self.zgbm.move(30, 40)
        self.zgbmEdit = QtGui.QLineEdit(self)
        self.zgbmEdit.move(110, 40)
        # self.zgbmEdit.setText('系统生成')

        self.xm = QtGui.QLabel('姓   名',self)
        self.xm.move(30, 80)
        self.xmEdit = QtGui.QLineEdit(self)
        self.xmEdit.move(110, 80)

        self.xb = QtGui.QLabel('性   别',self)
        self.xb.move(30, 120)
        self.xbEdit = QtGui.QLineEdit(self)
        self.xbEdit.move(110, 120)

        self.mz = QtGui.QLabel('民   族',self)
        self.mz.move(30, 160)
        self.mzEdit = QtGui.QLineEdit(self)
        self.mzEdit.move(110, 160)

        self.csny = QtGui.QLabel('出生年月 ',self)
        self.csny.move(30, 200)
        self.csnyEdit = QtGui.QLineEdit(self)
        self.csnyEdit.move(110, 200)

        self.hyzk = QtGui.QLabel('婚姻状况 ',self)
        self.hyzk.move(30, 240)
        self.hyzkEdit = QtGui.QLineEdit(self)
        self.hyzkEdit.move(110, 240)

        self.whcd = QtGui.QLabel('文化程度 ',self)
        self.whcd.move(30, 280)
        self.whcdEdit = QtGui.QLineEdit(self)
        self.whcdEdit.move(110, 280)

        self.jkzk = QtGui.QLabel('健康状况 ',self)
        self.jkzk.move(30, 320)
        self.jkzkEdit = QtGui.QLineEdit(self)
        self.jkzkEdit.move(110, 320)

        self.zzmm = QtGui.QLabel('政治面貌 ',self)
        self.zzmm.move(30, 360)
        self.zzmmEdit = QtGui.QLineEdit(self)
        self.zzmmEdit.move(110, 360)

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
        self.zwEdit = QtGui.QLineEdit(self)
        self.zwEdit.move(340, 320)

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

        self.gsyj = QtGui.QLabel('审查意见',self)
        self.gsyj.move(510, 120)
        self.gsyjEdit = QtGui.QLineEdit(self)
        self.gsyjEdit.move(600, 120)

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
        self.szbmEdit = QtGui.QLineEdit(self)
        self.szbmEdit.move(600, 320)

        self.zc = QtGui.QLabel('职   称',self)
        self.zc.move(510, 360)
        self.zcEdit = QtGui.QLineEdit(self)
        self.zcEdit.move(600, 360)

        # self.whcd = QtGui.QComboBox(self)
        # self.whcd.addItems(['hello', 'good'])
        self.jspx = QtGui.QLabel('何时技术培训',self)
        self.jspx.move(30, 400)
        self.jspxText = QtGui.QTextEdit(self)
        self.jspxText.setGeometry(QtCore.QRect(30, 430, 200, 50))

        self.jlcf = QtGui.QLabel('奖励处分',self)
        self.jlcf.move(340, 400)
        self.jlcfText = QtGui.QTextEdit(self)
        self.jlcfText.setGeometry(QtCore.QRect(340, 430, 200, 50))

        self.smwt = QtGui.QLabel('说明问题',self)
        self.smwt.move(30, 500)
        self.smwtText = QtGui.QTextEdit(self)
        self.smwtText.setGeometry(QtCore.QRect(30, 530, 200, 50))

        self.bz = QtGui.QLabel('备注',self)
        self.bz.move(340, 500)
        self.bzText = QtGui.QTextEdit(self)
        self.bzText.setGeometry(QtCore.QRect(340, 530, 200, 50))

        self.bz = QtGui.QLabel('成员信息',self)
        self.bz.move(30, 600)

        self.Mem_1 = QtGui.QLabel('成员一',self)
        self.Mem_1.move(30, 630)

        self.Mem_relation_1 = QtGui.QLabel('关系',self)
        self.Mem_relation_1.move(90, 630)
        self.Mem_relation_Edit_1 = QtGui.QLineEdit(self)
        self.Mem_relation_Edit_1.move(130, 630)

        self.Mem_xm_1 = QtGui.QLabel('姓名',self)
        self.Mem_xm_1.move(280, 630)
        self.Mem_xm_Edit_1 = QtGui.QLineEdit(self)
        self.Mem_xm_Edit_1.move(320, 630)

        self.Mem_job_1 = QtGui.QLabel('工作',self)
        self.Mem_job_1.move(470, 630)
        self.Mem_job_Edit_1 = QtGui.QLineEdit(self)
        self.Mem_job_Edit_1.move(510, 630)


        self.bz = QtGui.QLabel('成员二',self)
        self.bz.move(30, 680)

        self.Mem_relation_2 = QtGui.QLabel('关系',self)
        self.Mem_relation_2.move(90, 680)
        self.Mem_relation_Edit_2 = QtGui.QLineEdit(self)
        self.Mem_relation_Edit_2.move(130, 680)

        self.Mem_xm_2 = QtGui.QLabel('姓名',self)
        self.Mem_xm_2.move(280, 680)
        self.Mem_xm_Edit_2 = QtGui.QLineEdit(self)
        self.Mem_xm_Edit_2.move(320, 680)

        self.Mem_job_2 = QtGui.QLabel('工作',self)
        self.Mem_job_2.move(470, 680)
        self.Mem_job_Edit_2 = QtGui.QLineEdit(self)
        self.Mem_job_Edit_2.move(510, 680)


        self.bz = QtGui.QLabel('成员三',self)
        self.bz.move(30, 730)

        self.Mem_relation_3 = QtGui.QLabel('关系',self)
        self.Mem_relation_3.move(90, 730)
        self.Mem_relation_Edit_3 = QtGui.QLineEdit(self)
        self.Mem_relation_Edit_3.move(130, 730)

        self.Mem_xm_3 = QtGui.QLabel('姓名',self)
        self.Mem_xm_3.move(280, 730)
        self.Mem_xm_Edit_3 = QtGui.QLineEdit(self)
        self.Mem_xm_Edit_3.move(320, 730)

        self.Mem_job_3 = QtGui.QLabel('工作',self)
        self.Mem_job_3.move(470, 730)
        self.Mem_job_Edit_3 = QtGui.QLineEdit(self)
        self.Mem_job_Edit_3.move(510, 730)

        self.Input_tag = QtGui.QLabel('查询编码',self)
        self.Input_tag.move(600, 430)
        self.Input_zgbm = QtGui.QLineEdit(self)
        self.Input_zgbm.move(600, 455)


        self.Person_Query_Button = QtGui.QPushButton('查看个人档案', self)
        self.Person_Query_Button.move(600, 500)
        self.Person_Query_Button.clicked.connect(self.Person_Query_Button_Event)

        self.Reset_Button = QtGui.QPushButton('重置更新', self)
        self.Reset_Button.move(600, 550)
        self.Reset_Button.clicked.connect(self.Reset_Button_Event)

        # setGeometry(起点横坐标, 起点纵坐标, 宽, 高)
        # self.setGeometry(500, 300, 750, 500)
        self.setWindowTitle('企业人事档案管理系统--个人档案查看')
        # self.show()

    def Set_Info(self, person_res, cygx_res):
        self.zgbmEdit.setText(str(person_res[0]))
        self.xmEdit.setText(str(person_res[1]))
        self.xbEdit.setText(str(person_res[2]))
        self.mzEdit.setText(str(person_res[3]))
        self.csnyEdit.setText(str(person_res[4]))
        self.hyzkEdit.setText(str(person_res[5]))
        whcd = Base_init.Read_whbm[str(person_res[6])]
        self.whcdEdit.setText(whcd)
        self.jkzkEdit.setText(str(person_res[7]))
        self.zzmmEdit.setText(str(person_res[8]))
        zc = Base_init.Read_zcbm[str(person_res[9])]
        self.zcEdit.setText(zc)
        self.jgEdit.setText(str(person_res[10]))
        self.sfzhEdit.setText(str(person_res[11]))
        self.byxxEdit.setText(str(person_res[12]))
        self.zytcEdit.setText(str(person_res[13]))
        self.hkszdEdit.setText(str(person_res[14]))
        self.hkxzEdit.setText(str(person_res[15]))
        self.xzzEdit.setText(str(person_res[16]))
        self.zwEdit.setText(str(person_res[17]))
        self.gzmEdit.setText(str(person_res[18]))
        self.jspxText.setText(str(person_res[19]))
        self.jlcfText.setText(str(person_res[20]))
        self.smwtText.setText(str(person_res[21]))
        self.tbrqmEdit.setText(str(person_res[22]))
        self.tbrqEdit.setText(str(person_res[22]))
        self.tbrqEdit.setText(str(person_res[23]))
        self.gsyjEdit.setText(str(person_res[24]))
        self.scrqEdit.setText(str(person_res[25]))
        self.ryxzEdit.setText(str(person_res[26]))
        self.rcsjEdit.setText(str(person_res[27]))
        self.ryztEdit.setText(str(person_res[28]))
        self.bzText.setText(str(person_res[29]))
        szbm = Base_init.Read_bmbm[str(person_res[30])]
        self.szbmEdit.setText(szbm)

        if cygx_res == ():
            self.Mem_relation_Edit_1.setText('')
            self.Mem_xm_Edit_1.setText('')
            self.Mem_job_Edit_1.setText('')
            self.Mem_relation_Edit_2.setText('')
            self.Mem_xm_Edit_2.setText('')
            self.Mem_job_Edit_2.setText('')
            self.Mem_relation_Edit_3.setText('')
            self.Mem_xm_Edit_3.setText('')
            self.Mem_job_Edit_3.setText('')
        elif len(cygx_res) == 1:
            self.Mem_relation_Edit_1.setText(str(cygx_res[0][0]))
            self.Mem_xm_Edit_1.setText(str(cygx_res[0][1]))
            self.Mem_job_Edit_1.setText(str(cygx_res[0][2]))
            self.Mem_relation_Edit_2.setText('')
            self.Mem_xm_Edit_2.setText('')
            self.Mem_job_Edit_2.setText('')
            self.Mem_relation_Edit_3.setText('')
            self.Mem_xm_Edit_3.setText('')
            self.Mem_job_Edit_3.setText('')
        elif len(cygx_res) == 2:
            self.Mem_relation_Edit_1.setText(str(cygx_res[0][0]))
            self.Mem_xm_Edit_1.setText(str(cygx_res[0][1]))
            self.Mem_job_Edit_1.setText(str(cygx_res[0][2]))
            self.Mem_relation_Edit_2.setText(str(cygx_res[1][0]))
            self.Mem_xm_Edit_2.setText(str(cygx_res[1][1]))
            self.Mem_job_Edit_2.setText(str(cygx_res[1][2]))
            self.Mem_relation_Edit_3.setText('')
            self.Mem_xm_Edit_3.setText('')
            self.Mem_job_Edit_3.setText('')
        else:
            self.Mem_relation_Edit_1.setText(str(cygx_res[0][0]))
            self.Mem_xm_Edit_1.setText(str(cygx_res[0][1]))
            self.Mem_job_Edit_1.setText(str(cygx_res[0][2]))
            self.Mem_relation_Edit_2.setText(str(cygx_res[1][0]))
            self.Mem_xm_Edit_2.setText(str(cygx_res[1][1]))
            self.Mem_job_Edit_2.setText(str(cygx_res[1][2]))
            self.Mem_relation_Edit_3.setText(str(cygx_res[2][0]))
            self.Mem_xm_Edit_3.setText(str(cygx_res[2][1]))
            self.Mem_job_Edit_3.setText(str(cygx_res[2][2]))

    # 本页面
    def Person_Query_Button_Event(self):
        zgbm = self.Input_zgbm.text()
        person_res, cygx_res = Base_SQL.SQL_Person_Query(zgbm)
        if person_res == ():
            response = QtGui.QMessageBox.information(self, 'Message',"不存在此人！", QtGui.QMessageBox.Yes)
            # return
        else:
            self.Set_Info(person_res, cygx_res)

    # 非主页的其他页面调用
    def Out_Query_Button_Event(self, zgbm):
        # zgbm = self.Input_zgbm.text()
        person_res, cygx_res = Base_SQL.SQL_Person_Query(zgbm)
        if person_res == ():
            # 出弹框，查询为空
            return
        else:
            self.Set_Info(person_res, cygx_res)


    def Reset_Button_Event(self):
        zgbm = self.zgbmEdit.text()
        xm = self.xmEdit.text()
        xb = self.xbEdit.text()
        mz = self.mzEdit.text()
        csny = self.csnyEdit.text()
        hyzk = self.hyzkEdit.text()
        whcd = self.whcdEdit.text()
        whcd = Base_init.Input_whbm[str(whcd)]
        # print whcd
        jkzk = self.jkzkEdit.text()
        zzmm = self.zzmmEdit.text()
        jg = self.jgEdit.text()
        sfzh = self.sfzhEdit.text()
        byxx = self.byxxEdit.text()
        zytc = self.zytcEdit.text()
        hkszd = self.hkszdEdit.text()
        hkxz = self.hkxzEdit.text()
        xzz = self.xzzEdit.text()
        zw = self.zwEdit.text()
        gzm = self.gzmEdit.text()
        tbrqm = self.tbrqmEdit.text()
        tbrq = self.tbrqEdit.text()
        gsyj = self.gsyjEdit.text()
        scrq = self.scrqEdit.text()
        ryxz = self.ryxzEdit.text()
        rcsj = self.rcsjEdit.text()
        ryzt = self.ryztEdit.text()
        szbm = self.szbmEdit.text()
        szbm = Base_init.Input_bmbm[str(szbm)]
        # print szbm
        zc = self.zcEdit.text()
        zc = Base_init.Input_zcbm[str(zc)]
        # print zc
        jspx = self.jspxText.toPlainText()
        jlcf = self.jlcfText.toPlainText()
        smwt = self.smwtText.toPlainText()
        bz = self.bzText.toPlainText()
        # print xm, xb,mz, csny, hyzk, whcd, jkzk,zzmm,jg,sfzh,byxx,zytc,hkszd,
        # hkxz,xzz,zw,gzm,jspx,jlcf,smwt,tbrqm,tbrq,gsyj,scrq,ryxz,rcsj,ryzt,bz,szbm
        resp = Base_SQL.SQL_Replace(zgbm, xm, xb,mz, csny, hyzk, whcd, jkzk,zzmm,zc,jg,sfzh,byxx,zytc,hkszd,hkxz,xzz,zw,gzm,jspx,jlcf,smwt,tbrqm,tbrq,gsyj,scrq,ryxz,rcsj,ryzt,bz,szbm)
        # if resp == True:
            # response = QtGui.QMessageBox.information(self, 'Message',"重置成功！ ", QtGui.QMessageBox.Yes)
        relation_list = []
        if self.Mem_relation_Edit_1.text() != '':
            Mem_relation_1 = self.Mem_relation_Edit_1.text()
            Mem_xm_1 = self.Mem_xm_Edit_1.text()
            Mem_job_1 = self.Mem_job_Edit_1.text()
            relation_list.append([Mem_relation_1, Mem_xm_1, Mem_job_1])

        if self.Mem_relation_Edit_2.text() != '':
            Mem_relation_2 = self.Mem_relation_Edit_2.text()
            Mem_xm_2 = self.Mem_xm_Edit_2.text()
            Mem_job_2 = self.Mem_job_Edit_2.text()
            relation_list.append([Mem_relation_2, Mem_xm_2, Mem_job_2])

        if self.Mem_relation_Edit_3.text() != '':
            Mem_relation_3 = self.Mem_relation_Edit_3.text()
            Mem_xm_3 = self.Mem_xm_Edit_3.text()
            Mem_job_3 = self.Mem_job_Edit_3.text()
            relation_list.append([Mem_relation_3, Mem_xm_3, Mem_job_3])

        if relation_list != []:
            resp_2 = Base_SQL.SQL_Replace_Relation(zgbm, relation_list)
        else:
            resp_2 = True

        if resp_2 == True and resp == True:
            response = QtGui.QMessageBox.information(self, 'Message',"更新重置成功！", QtGui.QMessageBox.Yes)
        else:
            response = QtGui.QMessageBox.information(self, 'Message',"更新重置失败！", QtGui.QMessageBox.Yes)


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Person_Page()
    ex.initUI()
    ex.setGeometry(500, 300, 750, 800)
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
