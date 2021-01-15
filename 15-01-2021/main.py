import requests

# Списки
# Нумерация ВСЕГО и ВСЯ в программировании ведётся с нуля
# s = [0, 4, 3, 2, [3, 5, 8]]
# c = [3, 5, 8]
# print(s[4][1])

# Словари
# a = {
#     'david': 14,
#     'anton': '15',
#     'timofei': 16,
# }
# a['key'] = 'value'
# id = 'david'
# if a.get('dav1id'):
#     print(a['dav1id'])
# else:
#     a['dav1id'] = 17
#     print(a['dav1id'])
#
# print(a)
# request - запрос
# answer - ответ
# url - Uniform Resource Locator - Унифицированный указатель ресурса - ссылка

# Заменить URL на адрес другого API
# https://http.cat/КОД

answer = requests.get("https://official-joke-api.appspot.com/random_joke")

# Узнать названия полей
json = answer.json()

# Изменить вывод под названия полей
print(json)
