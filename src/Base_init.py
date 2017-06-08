 #-*-coding:utf-8-*-
import sys

SQL_column_name = ['zgbm', 'xm', 'xb','mz', 'csny', 'hyzk', 'whcd', 'jkzk','zzmm','zcbm','jg','sfzh','byxx','zytc','hkszd','hkxz','xzz','zw','gzm','jspx','jlcf','smwt','tbrqm','tbrq','gsyj','scrq','ryxz','rcsj','ryzt','bz','bmbm']

column_name = ['职工编码', '姓名','性别','民族','出生年月','婚姻状况','文化程度编码','健康状况','政治面貌','职称编码','籍贯','身份证号码','毕业学校','专业或特长','户口所在地','户口性质','现住址','职务','工种名','何时技术培训','何时奖励和处分','需要说明问题','填表人签名','填表日期','公司审查意见','审查日期','人员性质','入厂时间','人员状态','备注','部门编码']
dict_Map = {}
for i in range(len(column_name)):
    dict_Map[column_name[i]] = SQL_column_name[i]


def NameTOSQLname(name):
    return dict_Map[name]
