import csv
def hash(s):
    alf = "LabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890:-'."
    h = [alf.index(x) for x in s]
    p = 65
    m = 10**9+9
    hash_s = sum([h[i]*p**i for i in range(0,len(s))])%m
    return hash_s

with open('game.txt', encoding='utf-8') as file:
    data = list(csv.DictReader(file, delimiter='$', quotechar='"'))

with open('game_with_hash.csv','w',newline='', encoding='utf-8') as file:
    w =csv.DictWriter(file, fieldnames=['hash','GameName', 'characters', 'nameError', 'date'])
    w.writeheader()
    for i in data:
        s1 = ''
        s = i['GameName']+i['characters']
        for j in s:
            if j == ' ':
                continue
            else:
                s1 +=j
        w.writerow({'hash': hash(s1), 'GameName': i["GameName"], 'characters': i['characters'], 'nameError': i['nameError'], 'date':i['date']})
