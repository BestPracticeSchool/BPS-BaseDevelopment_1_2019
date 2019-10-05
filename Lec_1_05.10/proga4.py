n = 0

while n < 10:
    print(n)
    n+=1

while True:
    name = input()
    if name != "Joe":
        continue 
    else:
        break 

# RANGE BASED FOR
for i in range(1, 200):
    print(i)