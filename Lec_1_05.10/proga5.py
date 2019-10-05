#Collections

#Array
a_list = list()
b_list = []

c_list = [1,2,3,5, "asfdg", True]
d_list = [2,2,2,2,2]
d_list.append(200)

print(c_list + d_list)
print("qwety" + "123412")

#print( dir(c_list))
"""
too
many

"""

# Tuple
a_tuple = (1,2,3,4)
c_tuple = (1,)

#a_tuple[4] = 3

a_list = [1,2,3,4]

print("list ", a_list.__sizeof__())
print("tuple", a_tuple.__sizeof__())


#Set

a = set([2,2,2,2,23,4,5,6,6,6])
#print(a[1])
print(a)


# Dict

d_dict = {"one":1, "two":[123,123], True :[123], None :[123,123], 123213 : [123213,123], (1,2,3) :[123]}
#print(d_dict[[1,2,3]])

for key, _ in d_dict.items():
    print( key)

for j in (1,2,3,4):
    print(j)













