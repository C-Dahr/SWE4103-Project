import requests

# print("hello world")

mainUrl = 'http://127.0.0.1:5000'

url = mainUrl + '/HelloWorld'
urlGameSched = mainUrl + '/api/game-schedule'
urlTournSched = mainUrl + '/api/tournament-schedule'
urlGameStats = mainUrl + '/api/game-stats/<game_id>'
urlStandings = mainUrl + '/api/standings'
urlPlayerStats = mainUrl + '/api/player-stats/<player_id>'
urlRoster = mainUrl + '/api/roster/<team_id>'
urlLogin = mainUrl + '/api/login'
urlUserCreate = mainUrl + '/api/register'
urlRoot = mainUrl + '/'

urlUserCreate = 'http://127.0.0.1:5000/api/register'

expectedStatus = 200
expectedText = {"hello": "world"}

print(requests.get(url).status_code)
assert requests.get(url).status_code == expectedStatus
r = requests.get(url).json()
print(r)
assert r == expectedText

print(requests.post(urlUserCreate).status_code)
assert requests.post(urlUserCreate).status_code == expectedStatus

'''
print(requests.post(urlUserCreate).status_code)
assert requests.post(urlUserCreate).status_code == expectedStatus

print(requests.post(urlUserCreate).status_code)
assert requests.post(urlUserCreate).status_code == expectedStatus

print(requests.post(urlUserCreate).status_code)
assert requests.post(urlUserCreate).status_code == expectedStatus
'''