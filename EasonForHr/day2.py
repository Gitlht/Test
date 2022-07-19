"""# 字符串编码

print('你好'.encode('utf8'))  # 输出 b'\xe4\xbd\xa0\xe5\xa5\xbd'
print('你好'.encode('gbk'))  # 输出 b'\xc4\xe3\xba\xc3'

# 字节串解码

print(b'\xe5\x88\x98\xe6\x85\xa7\xe6\xb6\x9b'.decode('utf8'))

f = open("main.txt", 'br')
content = f.read()
print(len(content))
print(content)
f.close()
"""
import xlrd

book = xlrd.open_workbook("power.xlsx", 'br')
sheet = book.sheet_names()
sheet_object = xlrd.workbook.sheet_by_name(sheet)
ncols = sheet_object.ncols
col_values = sheet_object.col_values(colx=1)
print(col_values)
