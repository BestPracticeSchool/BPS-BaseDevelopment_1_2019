def kek(*args):
    print(args)
    print(type(args))

print(1,2,3,4,45,None,2,1,123)

kek()

def lol(**kwargs):
    print(kwargs)
    print(type(kwargs))

lol(name = "Jhon", sruname = "Snow", age = 52)


def lolkek(*args, **kwargs):
    print(args)
    print(kwargs)

lolkek(1,2,3,4,5,6,7,8, name = "Bob",age = 23)