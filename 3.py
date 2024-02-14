import csv
with open('game.txt', encoding='utf-8') as file:
    data = list(csv.DictReader(file, delimiter='$', quotechar='"'))
while True:
    a = input()
    l = []
    f = 0
    if a == 'game':
        break
    else:
        for i in data:
            if i['characters']==a and f==0 and i['GameName'] not in l:
                print(f'Персонаж {a} встречается в играх:')
                print(i['GameName'])
                l.append(i['GameName'])
                f+=1
            elif i['characters']==a and 5>f>0 and i['GameName'] not in l:
                print(i['GameName'])
                l.append(i['GameName'])
                f+=1
            elif i['characters']==a and f==5 and i['GameName'] not in l:
                print('и др.')
                break
        if f == 0:
            print('Этого персонажа не существует')

