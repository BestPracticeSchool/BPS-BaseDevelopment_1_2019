# Задание 7. Уровень - знаток алгоритмов.
# Условие: Напишите программу, которая проверяет, является ли скобочная последовательность правильной 
#(https://ru.wikipedia.org/wiki/Правильная_скобочная_последовательность).

#Под скобками понимается следующие символы: "(", ")", "{", "}", "[", "]".

#Входные данные: в первой строке идет число n, а потом идет n строк, в каждой из них — скобочная последовательность.

#Выходные данные: для каждой скобочной последовательности на отдельной строке выведите "yes" если
# она является правильной и "no" в противном случае.

# Замечание: реализовать решение при помощи стэка.


# Пример:
# Ввод:                                        # Вывод:
# 4
# ][                                           no
# [({})]                                       yes
# [(])                                         no
# ()                                           yes