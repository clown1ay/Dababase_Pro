 #-*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

SQL_column_name = ['zgbm', 'xm', 'xb','mz', 'csny', 'hyzk', 'whcd', 'jkzk','zzmm','zcbm','jg','sfzh','byxx','zytc','hkszd','hkxz','xzz','zw','gzm','jspx','jlcf','smwt','tbrqm','tbrq','gsyj','scrq','ryxz','rcsj','ryzt','bz','bmbm']

column_name = ['职工编码', '姓名','性别','民族','出生年月','婚姻状况','文化程度','健康状况','政治面貌','职称编码','籍贯','身份证号码','毕业学校','专业或特长','户口所在地','户口性质','现住址','职务','工种名','何时技术培训','何时奖励和处分','需要说明问题','填表人签名','填表日期','公司审查意见','审查日期','人员性质','入厂时间','人员状态','备注','部门']
dict_Map = {}
for i in range(len(column_name)):
    dict_Map[column_name[i]] = SQL_column_name[i]

Read_bmbm = {'PXB':'培训部', 'WLB':'外联部', 'XMB':'项目部', 'RSB':'人事部', 'CWB':'财务部'}
Read_whbm = {'BK': '本科','DZ': '大专', 'SS': '硕士', 'BS': '博士', 'BSH': '博士后'}
Read_zcbm = {'CZ':'处长','JZ':'局长', 'KZ':'科长','KY':'科员', 'SX':'实习'}

Input_bmbm = {'培训部': 'PXB', '外联部': 'WLB', '项目部': 'XMB', '人事部': 'RSB', '财务部': 'CWB'}
Input_whbm = {'本科': 'BK', '大专': 'DZ', '硕士': 'SS', '博士': 'BS', '博士后': 'BSH'}
Input_zcbm = {'处长': 'CZ','局长': 'JZ', '科长':'KZ', '科员': 'KY', '实习': 'SX'}
# whbm 6
# zcbm 9
# bmbm 30





# 汉字名称转化为字段名
def NameTOSQLname(name):
    return dict_Map[name]
