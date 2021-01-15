import requests

# request - запрос
# answer - ответ
# url - Uniform Resource Locator - Унифицированный указатель ресурса - ссылка

# Заменить URL на адрес другого API
# Добавить переменную name, которая будет вводиться с клавиатуры пользователем
# Выполнить запрос к Agify, где вместо Anton - введённое имя
# https://api.agify.io/?name=Anton


answer = requests.get("https://api.agify.io/?name=")

# Узнать названия полей
json = answer.json()

# Изменить вывод под названия полей
print(json)

