import xlrd
import xlwt
import json

# 打开excel表格
workbook = xlrd.open_workbook("test.xls")

# 获取所有sheet名称
sheet_names = workbook.sheet_names()

# 通过name获取第一个sheet对象
sheet1_object = workbook.sheet_by_name(sheet_names[0])

# 获取sheet1中的有效列数
nrows = sheet1_object.nrows

nwb = xlwt.Workbook('utf-8')
nws = nwb.add_sheet('sheet1')

n = 1
c = []
for m in range(0, nrows - 1):
    cell_info = sheet1_object.cell(rowx=n, colx=1).value
    list = json.loads(cell_info)
    for a in list:
        b = {}
        b['lng'] = a['lng']
        b['lat'] = a['lat']
        c.append(b)
    nws.write(n, 1, str(c))
    c.clear()
    n += 1
nwb.save('ttt.xls')
