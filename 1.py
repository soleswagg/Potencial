import csv
with open('game.txt', encoding='utf-8') as f:
    data = [list(map(str, ''.join(x).split('$'))) for x in f]

for i in range(len(data)):
    if '55' in data[i][2]:
        print(f'У персонажа {data[i][1]} в игре {data[i][0]} нашлась ошибка с кодом:= {data[i][2]}. Дата фиксации: {data[i][3]}')
        data[i][2] = 'Done'
        data[i][3] = '0000-00-00'
    else:
        data[i][3] = data[i][3][:-1]

with open('game_new.csv', 'w', newline='', encoding='utf8') as file:
    w = csv.writer(file, delimiter=',')
    w.writerows(data)
