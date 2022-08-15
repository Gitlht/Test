import requests


def getTick(num):
    url = f'https://hq.sinajs.cn/list={num}'
    headers = {'Referer': 'https://finance.sina.com.cn/'}
    page = requests.get(url, headers=headers)

    stock_info = page.text
    mt_info = stock_info.split(",")
    print(mt_info)
    tick = [mt_info[0], mt_info[1], mt_info[2]]

    return tick


while 1:
    num = input("请输入您要查询的股票代码：")
    if num == 'esc':
        print("拜拜了您嘞！")
        break
    else:
        last_tick = getTick(num)
        a = 0
        for n in last_tick:
            print(str(a) + ':' + '"' + n + '"' + ',')
            a += 1
