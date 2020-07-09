# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 15:41:07 2020

@author: 48572
"""

import pymysql
import fund
db=pymysql.connect(host='127.0.0.1'
                     ,user='root'
                     ,passwd='1154515863'
                     ,port= 3306 # 端口，默认为3306
                     ,db='cailh' # 数据库名称
                     ,charset='utf8' # 字符编码
    )
fon=fund.fond()
profit,date=fon.main()
data = {
    'date': date,
    'profit': "12",
}
table = 'my_table'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))
sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
cursor = db.cursor()
try:
   cursor.execute(sql, tuple(data.values()))
   print('Successful')
   db.commit()
except:
   print('Failed')
   db.rollback()
cursor.close() # 关闭游标
db.close() # 关闭连接
