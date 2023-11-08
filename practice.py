import requests

api_key = 'c5b30146-19bd-4b3a-aa54-3510b3261dfb'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

print(definitions)