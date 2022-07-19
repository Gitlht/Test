"""
def aaa(name, age):
    msg1 = "他的名字是：" + name
    msg2 = "他的年龄是：" + age
    return msg1 + "\n" + msg2
def bbb(msg):
    n = msg[6:-9]
    a = msg[-2:]
    return n + "\n" + a

print(bbb(aaa('刘慧涛','18')))
"""

var1 = [33, ['我的名字', '黑羽白月'], 'hello world!']
var1.append('你好')
print(var1)
var1.insert(0, '你好')
print(var1)
var1.insert(2, '你好')
print(var1)
str1 = '大家好，我的名字叫：黑羽白月'
line = str1.find('黑羽白月')
print(str1[line:])
print(str1.split('：')[1])

sex = input('请输入您的性别：').replace(' ', '')
hight = input('请输入您的身高（厘米）：').replace(' ', '').replace('厘米', '')
weight = input('请输入您的体重（公斤）：').replace(' ', '').replace('公斤', '')
nan = (int(hight) - 100) * 0.9
nv = (int(hight) - 100) * 0.9 - 2.5
if sex == "男":
    if int(weight) > nan + 5:
        print('用户体重高于标准')
    elif nan + 5 >= int(weight) >= nan - 5:
        print('用户体重标准')
    elif int(weight) < nan - 5:
        print('用户体重低于标准')
elif sex == "女":
    if int(weight) > nan + 5:
        print('用户体重高于标准')
    elif nan + 5 >= int(weight) >= nan - 5:
        print('用户体重标准')
    elif int(weight) < nan - 5:
        print('用户体重低于标准')
