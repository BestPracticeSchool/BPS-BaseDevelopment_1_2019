'''
Условие: необходимо написать программу, которая считывает с клавиатуры одно за другим два вещестенных числа A и B, 
и затем строку. Если эта строка является обозначением одной из четырёх 
основных математических операций (+, -, * или /), то выведите результат применения этой 
операции к введенным ранее числам, в противном случае выведите «ЫЫЫЫЫЫ». 
Также «ЫЫЫЫЫЫ» следует вывести, если пользователь захочет поделить на ноль.
'''
NUMBER1 = input()
NUMBER2 = input()
ZNAK = input()
try:
    NUMBER1 = float(NUMBER1)
    NUMBER2 = float(NUMBER2)
    RESULT = {
        '+': lambda NUMBER1, NUMBER2: NUMBER1 + NUMBER2,
        '-': lambda NUMBER1, NUMBER2: NUMBER1 - NUMBER2,
        '*': lambda NUMBER1, NUMBER2: NUMBER1 * NUMBER2,
        '/': lambda NUMBER1, NUMBER2: NUMBER1 / NUMBER2
    }[ZNAK](NUMBER1, NUMBER2)
    print(RESULT)
except:
    print('ЫЫЫЫЫЫ')
