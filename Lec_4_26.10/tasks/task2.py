
#TFD - test first development
Resource --- ItemList
#GET /items ----- список всех вещей в каталоге


Resource --- Item
#GET /item/<name> ---- вернуть информацию о предмете <name>.
#POST /item/<name> ---- добавить информацию о НОВОМ предмете <name>
#PUT /item/<name> ---- обновить информацию о СУЩЕСТВУЮЩЕМ предмете
#DELETE /item/<name> ---- удалить всю информацию о предмете <name>

