#my_dict = {}

#for k in range(0,10000):
#    my_dict[(k, k+1, k**2)] = [k**2 + k**3 + k**4, k]

my_dict = {(k, k+1, k ** 2) : [k**2 + k**3 + k**4, k]  for k in range(10000)}




t = 0 
for k,v in my_dict.items():
    print(k , v) 
    t += 1

    if t > 20:
        break
