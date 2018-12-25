# #coding:UTF-8
# import time
# from openpyxl import Workbook
#
# timestamp = 1175731200
#
# #转换成localtime
# time_local = time.localtime(timestamp)
# print(time_local)
# #转换成新的时间格式(2016-05-05 20:28:54)
# dt = time.strftime("%Y-%m-%d",time_local)
# print(dt)
from openpyxl import Workbook
import sqlite3
wb = Workbook()
sheet = wb.active

timestamp = 1175731200

db = sqlite3.connect('aaaa.db')
db.execute('CREATE TABLE IF NOT EXISTS tests (时间 date)')
db.execute('INSERT INTO tests VALUES(?)',(timestamp,))
db.commit()
data = db.execute('SELECT 时间 FROM tests')
d = db.execute('SELECT DATE(%s)'%data)
print(data)
#
#
# data = db.execute('SELECT * FROM tests')
# for i in data:
#     sheet.append(i)
#
# wb.save('aaaa.xlsx')
