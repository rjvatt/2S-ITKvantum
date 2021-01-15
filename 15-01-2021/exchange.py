import requests

# Перевод евро в рубли
# По умолчанию, без указания ключа from, мы получаем курс к ЕВРО.
# Чтобы не получать курс всех валют, указываем ключ to=RUB, благодаря которому получаем только курс евро к рублю
req = requests.get("https://api.frankfurter.app/latest?to=RUB")
json = req.json()
euroToRuble = json['rates']['RUB']

euros = int(input("Введите количество ЕВРО: "))

print(euros, 'евро стоит', euroToRuble * euros, 'рублей')

# Перевод долларов в мексиканские песо (MXN)
# Указываем в to - песо, а в from - доллары
req = requests.get("https://api.frankfurter.app/latest?to=MXN&from=USD")
json = req.json()
usdToMXN = json['rates']['MXN']

usd = int(input("Введите количество долларов: "))

print(usd, 'долларов стоит', usdToMXN * usd, 'песо')