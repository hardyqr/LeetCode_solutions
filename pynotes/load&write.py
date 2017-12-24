#1. 写入并生成csv文件
# coding: utf-8

import csv

csvfile = open('csv_test.csv', 'wb')
writer = csv.writer(csvfile)
writer.writerow(['姓名', '年龄', '电话'])

data = [
    ('小河', '25', '1234567'),
    ('小芳', '18', '789456')
]
writer.writerows(data)

csvfile.close()

#wb中的w表示写入模式，b是文件模式
#写入一行用writerow
#多行用writerows

#2. 读取csv文件
# coding: utf-8

import csv

csvfile = open('csv_test.csv', 'rb')
reader = csv.reader(csvfile)

for line in reader:
    print line

csvfile.close()

#3.读取txt
f = open('test.txt', 'r')
print f.read()

f.seek(0)
print f.read(14)

f.seek(0)
print f.readline()
print f.readline()

f.seek(0)
print f.readlines()

f.seek(0)
for line in f:
    print line,

f.close()
#4.写入txt

f = open('test.txt', 'r+')
f.truncate()
f.write('0123456789abcd')

f.seek(3)
print f.read(1)
print f.read(2)
print f.tell()

f.seek(3, 1)
print f.read(1)

f.seek(-3, 2)
print f.read(1)

f.close()
