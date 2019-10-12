a = []
nums = 1_000_000

for i in range(0, nums): 
    if i % 2 == 0: 
        a.append(i**2)
    else:
        a.append(i**3)
    

print(a[:20])


a_new = [ q ** 2 if q % 2 == 0 else q ** 3 for q in range(0,nums)]
print(a_new[:20])