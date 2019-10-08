def nod(a,b):
     if b > a: a, b = b, a
     while b:
          a,b = b, a % b
     return a

n = int(input())
drob = list()

for i in range(0,n):
     drob.append([])
     c = int(input())
     drob[i].append(c)
     c = int(input())
     drob[i].append(c)
znamen = 1
chisl = 0
for i in range(0,n):
     znamen *= drob[i][1]
for i in range(0,n):     
     chisl += drob[i][0] * (znamen / drob[i][1])

print(str(int(chisl / nod(chisl,znamen))) + ' / ' + str(int(znamen / nod(chisl,znamen))))