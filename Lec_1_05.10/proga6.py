def my_func(a,b,c):
    print(a+b+c)
    #return a,b 


a = my_func(2,3,4)
print(a)
b = my_func 
print(type(b))


print(dir(b))
print( b.__sizeof__())



print((lambda x,y: x**2 + y**2)(2,3))

q = lambda a, b = 2: a+b**2
print( q(1))