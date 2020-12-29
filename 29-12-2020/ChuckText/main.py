import requests

#http://api.icndb.com/jokes/random?firstName=John&lastName=Doe

firstname = input()
lastname = input()

req = requests.get("http://api.icndb.com/jokes/random?firstName=" + firstname + "&lastName=" + lastname)
reqJson = req.json()
joke = reqJson['value']['joke']

print(joke)