import csv

def alf(s):
    alfabet = ".'-:ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 "
    s = [alfabet.index(x) for x in s]
    return s

alfs = []
with open('game.txt', encoding='utf-8') as file:
    data = list(csv.DictReader(file, delimiter='$', quotechar='"'))

for i in data:
    alfs.append([alf(i['GameName']),i['GameName'], i['characters'],i['nameError'],i['date']])
print(alfs )




