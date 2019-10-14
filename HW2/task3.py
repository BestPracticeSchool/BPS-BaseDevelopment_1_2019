# Задача 3. Уровень - полиглот.
# Условие: Вам необходимо написать программу, 
# которая определяет языки запросов по буквам их слов. Сначала для каждого слова 
# запроса (слова разделяются пробелами) определите его язык, 
# посчитав для каждого языка количество букв на этом языке (буквы языков будут 
# также передаваться на вход) и выбрав язык с наибольшим результатом. 
# Далее языки запроса — это множество языков входящих в него слов.

# Если при определении языка слова несколько языков получили одинаковый 
# максимальный результат, выберите тот, который идет раньше по алфавиту. 
# Языки запроса выводите в алфавитном порядке и без повторений.
# Принадлежность букв к языку не должна зависеть от регистра.

# Входные данные: входные данные состоят из двух блоков, разделенных двойным переносом строки.
# Первый блок описывает языки и входящие в них буквы. 
# В каждой строке сначала идет название языка (буквы без пробелов), 
# потом пробел, потом все буквы языка (без пробелов).
# Второй блок описывает запросы — на каждой строке находится один запрос.

# Выходные данные: для каждого запроса выведите на отдельной строке языки 
# этого запроса через пробел.

# Если какой-то запрос полностью состоит из символов, 
# которых нет ни в одном языке, то для него нужно вывести пустую строку.


# Пример:
# Ввод                                               Вывод
#en abcdefghijklmnopqrstuvwxyz
#ru абвгдеёжзиклмнопрстуфхцчшщъыьэюя
#
#привет мир
#привет мир на Python
#abcйуцкен xyzфывапр                                 
#                                                    ru
#                                                    en ru
#                                                    ru