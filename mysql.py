#!/usr/bin/python
# _*_ coding: utf-8 _*_

import pymysql

db = pymysql.connect(host='39.97.179.164',port=3306,user='root',passwd='Nice_521258',charset='utf8')
cursor = db.cursor()
cursor.execute("select version()")
data = cursor.fetchone()
print(data)

