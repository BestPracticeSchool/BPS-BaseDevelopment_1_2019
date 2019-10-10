'''
Условие: напишите программу, которая для данного текста подсчитывает частоты всех символов в нем. 
Регистр не важен. То есть символы 'А' и 'а' - эквивалентны.
Входные данные: произвольный текст.
Выходные данные: таблица с частотами символов. 
Таблица должна быть отсортирована по убыванию частот, в случае равных частот — в алфавитном порядке. 
Если в тексте нет алфавитных символов - выводим перенос строки.
'''
import string
ALLBUKOVI = set()
BUKOVI = dict()
S = input().lower()
for C in S:
    if C in string.punctuation or C == ' ':
        pass
    elif not C in ALLBUKOVI:
        ALLBUKOVI.add(C)
        BUKOVI.update({C:1})
    else:
        BUKOVI[C] += 1
while BUKOVI:
    MAS = list()
    VAL = max(BUKOVI.values())
    for KEY in BUKOVI.keys():
        if BUKOVI[KEY] == VAL:
            MAS.append(KEY)
    for KEY in MAS:
        BUKOVI.pop(KEY)
    MAS.sort()
    for I in MAS:
        print(str(I) + ': ' + str(VAL))
    if ALLBUKOVI == {}:
        print("\n")
