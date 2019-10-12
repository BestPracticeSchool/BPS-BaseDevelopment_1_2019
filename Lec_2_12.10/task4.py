# HTTP 

# HTTPS

# 1. API - application programming interface
# API - ЭТО НАБОР МЕТОДОВ (ИСНТРУКЦИЯ) ОБЩАЯ ДЛЯ ВСЕХ КОМПУХТЕРОВ В СЕТИ

# 2. HTTP - Hyper TEXT Transfer Protocol
# 2.1 LINKER
# https://www.google.com/ --- PROTOCOL://?.SERVICE.HOSTNAME/PATH

# 2.2 HTTP VERBS
# GET (request) - запрос на получение каких-либо данных
# Example1: GET /catalog HTTP/1.1  --- HTTP_VERB PATH PROTOCOL_VERSION

# POST (request)  - запрос на первичное добавление каких-либо данных
# Example2: POST /cataloh HTTP/1.1 + JSON  --- HTTP_VERB PATH PROTOCOL_VERSION + DATA 


# PUT (request) --- запрос на обновление каких-либо данных
# Example3: PUT /cataloh HTTP/1.1 + JSON  --- HTTP_VERB PATH PROTOCOL_VERSION + DATA 

# DELETE (request) --- запрос на удаление каких-либо данных
# Example4: DELETE /catalog HTTP/1.1  --- HTTP_VERB PATH PROTOCOL_VERSION

#GET /login_page HTTP/1.1
#POST /login_page HTTP/1.1 + JSON{
#    "NAME" : "evgeny",
#    "SURNAME": "vlasov",
#    "CRETIDNUM": "123456789"
#}