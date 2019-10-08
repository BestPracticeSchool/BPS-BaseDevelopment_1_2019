a = int(input())
res = list()

for i in range(1, a + 1):
    if (a % i == 0):
      res.append(i)  

for i in res: print(str(i), end =' ')

if (res == [1, a]):
     print("ACHTUNG")