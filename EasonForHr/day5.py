with open('main.txt', encoding='utf8') as f:
    lines = f.read().splitlines()

oldPeople = []
for line in lines:
    # 去掉行中的空格
    line = line.replace(' ', '')

    # 如果是空格，跳过
    if not line:
        continue

    name, age = line.split(':')
    if int(age) > 50:
        oldPeople.append(name)

oldPeopleStr = ','.join(oldPeople)
appendText = f'\n\n大于50岁的人有：{oldPeopleStr}'

with open('main.txt', 'a', encoding='utf8') as f:
    f.write(appendText)
