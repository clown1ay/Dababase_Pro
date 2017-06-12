 #-*-coding:utf-8-*-
'''
    基本的SQL语句模块
'''
# import MySQLdb
import pymysql
import time
import Base_init
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 获取系统时间 time.strftime('%Y-%m-%d-%H:%M',time.localtime(time.time()))

# conn=MySQLdb.connect(host='localhost',user='root',passwd='1234',port=3306,charset = 'utf8')
# cur=conn.cursor()
# cur.execute("use HR_Manage")

conn =pymysql.connect(host='127.0.0.1', user='root', passwd='1234', charset='utf8')
cur = conn.cursor()

cur.execute("use information_schema")
cur.execute("select COLUMN_NAME from COLUMNS where TABLE_NAME = 'm_dadj';")
m_dadj_column_names = cur.fetchall()

cur.execute("use HR_Manage")

# 获取所有档案信息，输出； 问题是，存在转意的问题
def SQL_Scan():
    single_dict = {}
    data_dict = {}
    return_dict = {}
    sqlstr = "SELECT * FROM m_dadj";
    count = cur.execute(sqlstr)
    res = cur.fetchall()
    # print res
    '''
    for item in res:
        for i in range(1, len(item)):
            single_dict[str(m_dadj_column_names[i][0])] = i
        zgbm = "%03d"%int(item[0])
        data_dict[zgbm] = single_dict
        single_dict = {}
    '''
    return_dict['length'] = int(count)
    return_dict['data'] = res
    # print len(return_dict['data'][0])
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
    '''
    for item in res:
        for i in range(1, len(item)):
            single_dict[str(m_dadj_column_names[i][0])] = i
        zgbm = "%03d"%int(item[0])
        data_dict[zgbm] = single_dict
        single_dict = {}
    '''
    return_dict['length'] = int(count)
    return_dict['data'] = res
    print return_dict
    return return_dict


# 1精确， 2 模糊
def SQL_Query_xm(xm, ttype):
    single_dict = {}
    data_dict = {}
    return_dict = {}
    print ttype
    if ttype == '1':
        sqlstr = "SELECT * FROM m_dadj WHERE xm = '%s'" %xm
    else:
        sqlstr = "SELECT * FROM m_dadj WHERE xm like '%%%s%%'" %xm
    print sqlstr
    count = cur.execute(sqlstr)
    res = cur.fetchall()
    '''
    for item in res:
        for i in range(1, len(item)):
            single_dict[str(m_dadj_column_names[i][0])] = i
        zgbm = "%03d"%int(item[0])
        data_dict[zgbm] = single_dict
        single_dict = {}
    '''
    return_dict['length'] = int(count)
    return_dict['data'] = res
    print return_dict
    return return_dict


# 个人档案查询
def SQL_Person_Query(zgbm):
    sqlstr = "SELECT * FROM m_dadj WHERE zgbm = %s" %zgbm
    person_count = cur.execute(sqlstr)
    if person_count != 0:
        person_res = cur.fetchone()
    else:
        person_res = ()
    sqlstr = "SELECT Brgx,xm,job FROM cygx WHERE zgbm = %s" %zgbm
    cygx_count = cur.execute(sqlstr)
    if cygx_count != 0:
        cygx_res = cur.fetchall()
    else:
        cygx_res = ()
    print person_res, cygx_res
    return person_res, cygx_res



# 统计功能
def SQL_Count(index):
    return_dict = {}
    if index == 'xb':
        sqlstr_1 = "SELECT DISTINCT(xb),COUNT(*) FROM m_dadj GROUP BY xb"
    elif index == 'bmbm':
        sqlstr_1 = "SELECT DISTINCT(bmbm),COUNT(*) FROM m_dadj GROUP BY bmbm"
    elif index == 'whcd':
        sqlstr_1 = "SELECT DISTINCT(whcd),COUNT(*) FROM m_dadj GROUP BY whcd"
    elif index == 'zcbm':
        sqlstr_1 = "SELECT DISTINCT(zcbm),COUNT(*) FROM m_dadj GROUP BY zcbm"
    elif index == 'sum':
        sqlstr_1 = "SELECT COUNT(*) FROM m_dadj"
    count = cur.execute(sqlstr_1)
    print count
    res = cur.fetchall()
    print res
    if index == 'sum':
        return_dict['length'] = int(count)
        return_dict['data'] = [('sum', res[0][0])]
    else:
        return_dict['length'] = int(count)
        return_dict['data'] = res
    print return_dict
    return return_dict


# 删除某条档案记录
def SQL_Del(zgbm):
    try:
        sqlstr = "DELETE FROM m_dadj WHERE zgbm = %s" %zgbm
        print sqlstr
        cur.execute(sqlstr)
        conn.commit()
        print '删除成功！ '
        return 1
    except Exception, e:
        print str(e.message)
        print '-------------------------------'
        return 0


# 修改档案记录
def SQL_Update(zgbm, column_name, update_content):
    update_content = str(update_content)
    if column_name == 'zcbm':
        update_content = Base_init.Input_zcbm[update_content]
    elif column_name == 'bmbm':
        update_content = Base_init.Input_bmbm[update_content]
    elif column_name == 'whcd':
        update_content = Base_init.Input_whbm[update_content]
    try:
        sqlstr = "UPDATE m_dadj SET %s = '%s' WHERE zgbm = %s" %(column_name, update_content, zgbm)
        # print sqlstr
        cur.execute(sqlstr)
        conn.commit()
        print '修改成功！ '
        return 1
    except Exception, e:
        print str(e.message)
        return 0

# 插入新的档案记录
def SQL_Insert(zgbm, xm, xb,mz, csny, hyzk, whcd, jkzk,zzmm,zc,jg,sfzh,byxx,zytc,hkszd,hkxz,xzz,zw,gzm,jspx,jlcf,smwt,tbrqm,tbrq,gsyj,scrq,ryxz,rcsj,ryzt,bz,szbm):
    sqlstr = "INSERT INTO m_dadj(zgbm,xm, xb,mz,csny,hyzk,whcd, jkzk,zzmm,zcbm,jg,sfzh,byxx,zytc,hkszd,hkxz,xzz,zw,gzm,jspx,jlcf,smwt,tbrqm,tbrq,gsyj,scrq,ryxz,rcsj,ryzt,bz,bmbm) VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');"%(zgbm, xm, xb,mz, csny, hyzk, whcd, jkzk,zzmm,zc,jg,sfzh,byxx,zytc,hkszd,hkxz,xzz,zw,gzm,jspx,jlcf,smwt,tbrqm,tbrq,gsyj,scrq,ryxz,rcsj,ryzt,bz,szbm)

    print sqlstr
    try:
        cur.execute(sqlstr)
        conn.commit()
        print '插入成功！'
        return 1
    except:
        return 0

def SQL_Insert_Realtion(zgbm, relation_list):
    for record in relation_list:
        sqlstr = "INSERT INTO cygx(zgbm,Brgx,xm,job) VALUES(%s,'%s','%s','%s')" %(zgbm, record[0], record[1], record[2])
        cur.execute(sqlstr)
    conn.commit()
    print '成员关系插入成功！'


# 查看存在外键的表
def SQL_Scan_Tables(ttype):
    return_data = {}
    if ttype == 'whcd':
        sqlstr = "SELECT * FROM bm_wh"
    elif ttype == 'bm':
        sqlstr = "SELECT * FROM bm_bm"
    elif ttype == 'zc':
        sqlstr = "SELECT * FROM bm_zc"
    count = cur.execute(sqlstr)
    res = cur.fetchall()
    return_data['length'] = count
    return_data['data'] = res
    return return_data


def SQL_Update_Tables(ttype, column_bm, column, update_content):
    if ttype == 'whcd':
        if column == 0:
            sqlstr = "UPDATE bm_wh SET whbm = '%s' WHERE whbm = '%s'" %(update_content, column_bm)
        else:
            sqlstr = "UPDATE bm_wh SET whcd = '%s' WHERE whbm = '%s'" %(update_content, column_bm)
    elif ttype == 'bm':
        if column == 0:
            sqlstr = "UPDATE bm_bm SET bmbm = '%s' WHERE bmbm = '%s'" %(update_content, column_bm)
        else:
            sqlstr = "UPDATE bm_bm SET bmm = '%s' WHERE bmbm = '%s'" %(update_content, column_bm)
    elif ttype == 'zc':
        if column == 0:
            sqlstr = "UPDATE bm_zc SET zcbm = '%s' WHERE zcbm = '%s'" %(update_content, column_bm)
        else:
            sqlstr = "UPDATE bm_zc SET zcmc = '%s' WHERE zcbm = '%s'" %(update_content, column_bm)
    cur.execute(sqlstr)
    conn.commit()
    print '修改成功！ '
    return 1


# 编码表信息插入
def SQL_Insert_Tables(ttype, new_bm, new_name):
    if ttype == 'whcd':
        sqlstr = "INSERT INTO bm_wh(whbm,whcd) VALUES('%s','%s')" %(new_bm, new_name)
    elif ttype == 'bm':
        sqlstr = "INSERT INTO bm_bm(bmbm,bmm) VALUES('%s','%s')" %(new_bm, new_name)
    elif ttype == 'zc':
        sqlstr = "INSERT INTO bm_zc(zcbm,zcmc) VALUES('%s','%s')" %(new_bm, new_name)
    try:
        cur.execute(sqlstr)
        conn.commit()
        print '插入成功!'
    except Exception, e:
        print e
        return 0


# 编码表记录删除
def SQL_Del_Tables(ttype, column_bm):
    if ttype == 'whcd':
        sqlstr = "DELETE FROM  bm_wh WHERE whbm = '%s'" %column_bm
    elif ttype == 'bm':
        sqlstr = "DELETE FROM bm_bm WHERE bmbm = '%s'" %column_bm
    elif ttype == 'zc':
        sqlstr = "DELETE FROM bm_zc WHERE zcbm = '%s'" %column_bm
    try:
        cur.execute(sqlstr)
        conn.commit()
        print '删除成功！ '
        return 1
    except Exception, e:
        print e
        return 0




if __name__ == '__main__':
    # SQL_Scan()
    # SQL_Query_zgbm(1, '1')
    # SQL_Query_xm('张', '0')
    # SQL_Count('sum')
    SQL_Person_Query('6')
