# REST

# 1) Запрос не зависит от другого запроса
# 2) Сервер только знает про текующий запрос, ничего не знает о предыдущих



######## PROJECT ENDPOINTS MAP #######

# POST --- получить данные
# GET --- послть данные клиенту

# RES 1 /
# GET / --homepage of stores marketplace

# RES 2 /store
# POST /store data:{name:}
# GET /store/<string:name>
# POST /store/<string:name>/item {name:, price:}
# GET /store/<string:name>/item

# RES 3 /stores
# GET /stores