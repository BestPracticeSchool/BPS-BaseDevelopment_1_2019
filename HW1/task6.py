'''
Условие: вы создали игру в жанре шутер. Теперь ваш дизайнер придумал новое неизвестное никому оружее - дробовик.
Известно, что дробовики стреляют дробью (внезапно, правда?). Ваша задача - рассчитать суммарный урон, наненсенный 
выстрелом из дробовика.
Входные данные : Сначала вводится количество дробинок.
Затем урон от каждой дробинки. Урон от каждой дробинки выражается простой дробью, 
её числитель и знаменатель вводятся на отдельных строках.
Выходные данные : Суммарный урон, выраженный простой несократимой дробью с дробной 
чертой между числителем и знаменателем.
'''

def NOD(a, b):
     if b > a: a, b = b, a
     while b:
          a, b = b, a % b
     return a

N = int(input())
DROB = list()
for i in range(0,N):
     DROB.append([])
     INPUT_NUMBER = int(input())
     DROB[i].append(INPUT_NUMBER)
     INPUT_NUMBER = int(input())
     DROB[i].append(INPUT_NUMBER)
ZNAMENATEL = 1
CHISLITEL = 0
for i in range(0, N):
     ZNAMENATEL *= DROB[i][1]
for i in range(0, N):
     CHISLITEL += DROB[i][0] * (ZNAMENATEL / DROB[i][1])

print(str(int(CHISLITEL / NOD(CHISLITEL, ZNAMENATEL))) \
     + ' / ' + str(int(ZNAMENATEL / NOD(CHISLITEL, ZNAMENATEL))))
     