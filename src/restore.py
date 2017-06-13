 #-*-coding:utf-8-*-
'''
    基本的SQL语句模块
'''
import MySQLdb
# import pymysql
import time
import Base_init
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

r_file = open('/home/carrie/cuishiyao/Database_Pro/HR_backup.sql.sql')
lines = r_file.readlines()
r_file.close()

# content = content.replace('\n', '')
sql = ''
for line in lines:
    line = line.strip()
    if line[:2] == '--' or line[:2] == '/*' or line == '\n' or line == '':
        continue
    sql = sql + line
    if line[len(line)-1] == ';':
        print sql
        sql = ''
