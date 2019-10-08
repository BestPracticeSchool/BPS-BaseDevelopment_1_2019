a = input()
b = input()
znak = input()
try:
    a = float(a)
    b = float(b)
    res = {
        '+': lambda a,b: a + b,
        '-': lambda a,b: a - b,
        '*': lambda a,b: a * b,
        '/': lambda a,b: a / b
    }[znak](a,b)
    print(res)
except: print('ЫЫЫЫЫЫ')