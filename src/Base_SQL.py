 #-*-coding:utf-8-*-
'''
    基本的SQL语句模块
'''
# import MySQLdb
import pymysql
import time
import json

# 获取系统时间 time.strftime('%Y-%m-%d-%H:%M',time.localtime(time.time()))

# conn=MySQLdb.connect(host='localhost',user='root',passwd='1234',port=3306,charset = 'utf8')
# cur=conn.cursor()
# cur.execute("use HR_Manage")

conn =pymysql.connect(host='127.0.0.1', user='root', passwd='1234', charset='utf8')
cur = conn.cursor()

cur.execute("use information_schema")
cur.execute("select COLUMN_NAME from COLUMNS where TABLE_NAME = 'm_dadj';")
m_dadj_column_names = cur.fetchall()
# print str(m_dadj_column_names[0][0])
# print m_dadj_column_names

cur.execute("use HR_Manage")

# 获取所有档案信息，输出； 问题是，存在转意的问题
def SQL_Scan():
    single_dict = {}
    data_dict = {}
    return_dict = {}
    sqlstr = "SELECT * FROM m_dadj";
    count = cur.execute(sqlstr)
    res = cur.fetchall()
    for item in res:
        for i in range(1, len(item)):
            single_dict[str(m_dadj_column_names[i][0])] = i
        zgbm = "%03d"%int(item[0])
        data_dict[zgbm] = single_dict
        single_dict = {}
    return_dict['length'] = int(count)
    return_dict['data'] = data_dict
    print return_dict
    return return_dict


# 1精确， 2 模糊
def SQL_Query_zgbm(zgbm, ttype):
    single_dict = {}
    data_dict = {}
    return_dict = {}
    zgbm = int(zgbm)
    if ttype == '1':
        sqlstr = "SELECT * FROM m_dadj WHERE zgbm = %s" %zgbm
    else:
        sqlstr = "SELECT * FROM m_dadj WHERE zgbm like '%%%s%%'" %zgbm
        print sqlstr
    count = cur.execute(sqlstr)
    res = cur.fetchall()
    for item in res:
        for i in range(1, len(item)):
            single_dict[str(m_dadj_column_names[i][0])] = i
        zgbm = "%03d"%int(item[0])
        data_dict[zgbm] = single_dict
        single_dict = {}
    return_dict['length'] = int(count)
    return_dict['data'] = data_dict
    print return_dict
    return return_dict


# 1精确， 2 模糊
def SQL_Query_xm(xm, ttype):
    single_dict = {}
    data_dict = {}
    return_dict = {}
    if ttype == '1':
        sqlstr = "SELECT * FROM m_dadj WHERE xm = '%s'" %xm
    else:
        sqlstr = "SELECT * FROM m_dadj WHERE xm like '%%%s%%'" %xm
    count = cur.execute(sqlstr)
    res = cur.fetchall()
    for item in res:
        for i in range(1, len(item)):
            single_dict[str(m_dadj_column_names[i][0])] = i
        zgbm = "%03d"%int(item[0])
        data_dict[zgbm] = single_dict
        single_dict = {}
    return_dict['length'] = int(count)
    return_dict['data'] = data_dict
    print return_dict
    return return_dict


def SQL_Count(index):
    count_dict = {}
    if index == 'xb':
        sqlstr_1 = "SELECT DISTINCT(xb),COUNT(*), m_dadj.* FROM m_dadj GROUP BY xb"
    elif index == 'bmbm':
        sqlstr_1 = "SELECT DISTINCT(bmbm),COUNT(*) FROM m_dadj GROUP BY bmbm"
    elif index == 'whcd':
        sqlstr_1 = "SELECT DISTINCT(whcd),COUNT(*) FROM m_dadj GROUP BY whcd"
    elif index == 'zw':
        sqlstr_1 = "SELECT DISTINCT(zw),COUNT(*) FROM m_dadj GROUP BY zw"
    elif index == 'sum':
        sqlstr_1 = "SELECT COUNT(*) FROM m_dadj"
    count = cur.execute(sqlstr_1)
    res = cur.fetchall()
    if index == 'sum':
        count_dict['length'] = 1
        count_dict['sum'] = int(res[0][0])
    else:
        for item in res:
            count_dict[item[0]] = int(item[1])
        count_dict['length'] = int(count)
    print count_dict
    return count_dict



if __name__ == '__main__':
    # Scan_SQL()
    # SQL_Query_zgbm(1, '0')
    # SQL_Query_xm('张', '0')
    SQL_Count('xb')
