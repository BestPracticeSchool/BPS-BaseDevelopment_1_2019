# 2. Создаем проблемы как Безос

А теперь пришло время сотворить свой первый шедевр. Итак, что нужно - внимательно ознакомиться с техническим заданием и реализовать все методы и пункты.

Вам предлагается создать REST Api книжного магазина (привет, Амазон) со следующими требованиями.

1. Необходимо наличие следующих ресурсов в Api:
* Book
* Author
* Books
* Authors
* UserRegister

а также аутентификацию пользователя. Необходимая пользовательская информация включает в себя ```username``` и ```password```. Требуется, чтобы все ```username```  были различны и ```username``` больше 5 символов. ```password``` - содержит минимум 1 символ латиницы, минимум 1 цифру и пароль длиньше 8 символов. В случае, если требования не выполняются, нужно сообщить об этом пользователю и выдать ошибку аутентификации 401.


2. Структура ресурса ```Book```. Все методы защищены меткой JWT и требуют аутентификации.

```get()``` (```/book/<name>```) получить информацию о книге. 
Информация о книге отображается в виде ```.json``` объекта со структурой:
* bookTitle - название книги
* author - автор книги
* price - цена книги

```post()``` (```/book/<name>```)добавить книгу с названием ```<name>```. Добавочный ```.json``` содержит ```author``` и ```price```.

```put() (```/book/<name>```)``` обновить информацию о книге с названием ```<name>```. Добавочный ```.json``` содержит ```author``` и ```price```.

```delete()``` (```/book/<name>```) удалить книгу с названием ```<name>```.

3. Структура ресурса ```Books```. 

```get()``` (```/books```) получить все книги (всю информацию о книгах), имеющиеся в магазине на данный момент.

4. Структура ресурса ```Author```.

```get()``` (```/author/<name>```)получить информацию об авторе ```<name>``` (все книги автора).

5. Структура ресурса ```Authors```.

```get()``` (```/authors```) вернуть всех авторов, чьи книги присуствуют в магазине на данный момент.


6. Структура ресурса ```UserRegister```.

```post()``` (```/register```)   зарегестрировать пользователя. Добавочный ```.json``` содержит ```username``` и ```password``` со всеми требваниями, которые были изложены в пункте 1.

Все завязано на базе ```data.db```. База включает в себя 2 таблицы :
* users с полями (id, username, password).
* books с полями (title, author, price).

Это все:) Вперед!