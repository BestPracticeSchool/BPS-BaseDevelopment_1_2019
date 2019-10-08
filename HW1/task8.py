import string
ALLbukovi = set()
bukovi = dict()

s = input().lower()

for c in s:
    if c in string.punctuation or c == ' ':
        pass
    elif not(c in ALLbukovi):
        ALLbukovi.add(c)
        bukovi.update({c:1})
    else:
        bukovi[c] += 1

while bukovi:
    mas = list()
    val = max(bukovi.values())
    for key in bukovi.keys():
        if bukovi[key] == val:
            mas.append(key)
    
    for key in mas: 
        bukovi.pop(key)

    mas.sort()
    for i in mas:
        print(str(i) + ': ' + str(val))