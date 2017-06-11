 #-*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import Base_init

# {'length': 3, 'data': ((u'BK', 3), (u'DZ', 1), (u'SS', 1))}
Headers = Base_init.column_name
def Gene_file(filename, data_list):
    try:
        string = ''
        for title in Headers:
             string = string + title + '\t'
        string = string[:len(string) - 1] + '\n'
        for record in data_list:
            for item in record:
                string = string + str(item) + '\t'
            string = string[:len(string) - 1] + '\n'
        string = string[:len(string) - 1]
        w_file = open('/home/carrie/cuishiyao/' + filename + '.ods', 'w')
        w_file.write(string)
        w_file.close()
        print '导出成功！'
        return 1
    except:
        return 0
