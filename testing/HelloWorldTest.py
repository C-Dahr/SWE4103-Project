import requests

# print("hello world")

mainUrl = 'http://127.0.0.1:5000'

url = mainUrl + '/HelloWorld'
urlGameSchedule = mainUrl + '/api/game-schedule'
urlTournamentSchedule = mainUrl + '/api/tournament-schedule'
urlGameStats = mainUrl + '/api/game-stats/<game_id>'
urlLeagueStanding = mainUrl + '/api/standings'
urlPlayerStats = mainUrl + '/api/player-stats/'
urlRoster = mainUrl + '/api/roster/<team_id>'
urlLogin = mainUrl + '/api/login'
urlUserCreate = mainUrl + '/api/register'
urlRoot = mainUrl + '/'
urlTeam = mainUrl + '/api/team'

urlUserCreate = 'http://127.0.0.1:5000/api/register'

expectedStatus = 200 #and 201 for successes
expectedText = {"hello": "world"}
print(url)
print("HelloWorld:", requests.get(url).status_code)
assert requests.get(url).status_code == expectedStatus
r = requests.get(url).json()

print("r =",r)
assert r == expectedText


#Team

#Player

#League


#print("UserCreate:",requests.post(urlUserCreate).status_code)
#assert requests.post(urlUserCreate).status_code == expectedStatus

'''
PlayerStats_10 = urlPlayerStats + "10"
print(PlayerStats_10)

print("PlayerStats =",requests.get(PlayerStats_10).status_code)
assert requests.get(PlayerStats_10).status_code == expectedStatus

print(requests.post(urlUserCreate).status_code)
assert requests.post(urlUserCreate).status_code == expectedStatus

print(requests.post(urlUserCreate).status_code)
assert requests.post(urlUserCreate).status_code == expectedStatus

print(requests.post(urlUserCreate).status_code)
assert requests.post(urlUserCreate).status_code == expectedStatus
'''