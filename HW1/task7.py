'''
Условие: Напишите программу, которая проверяет, является ли скобочная последовательность правильной 
(https://ru.wikipedia.org/wiki/Правильная_скобочная_последовательность).
Под скобками понимается следующие символы: "(", ")", "{", "}", "[", "]".
Входные данные: в первой строке идет число n, а потом идет n строк, в каждой из них — скобочная последовательность.
Выходные данные: для каждой скобочной последовательности на отдельной строке выведите "yes" если
она является правильной и "no" в противном случае.
Замечание: реализовать решение при помощи стэка.
'''
SKOBOCHKI = {')':'(', ']':'[', '}':'{'}
 
def Proverochka(s):
    STECK = []
    for SYMBOL in s:
        if SYMBOL in SKOBOCHKI.values():
            STECK.append(SYMBOL)
        elif SYMBOL in SKOBOCHKI.keys():
            if not (STECK and SKOBOCHKI[SYMBOL] == STECK.pop()):
                return False
    return True

N = int(input())
for i in range(0, N): 
     s = input() 
     if (Proverochka(s) == True): 
          print("yes")
     else: 
          print("no")
          