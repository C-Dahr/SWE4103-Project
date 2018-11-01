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

urlUserCreate = 'http://127.0.0.1:5000/api/register'

#Tests
urlLeague = mainUrl + '/api/league'
urlTeam = mainUrl + '/api/team'
urlPlayer = mainUrl + '/api/player'




#League
leagueCheck = True
leagueGet_code = requests.get(urlLeague).status_code
leaguePost_code = requests.post(urlLeague).status_code
print("League - Get and Post")
if leagueGet_code != 200:
    print('League Get =', leagueGet_code)
    leagueCheck = None
if leaguePost_code != 201:
    print('League Post =', leaguePost_code)
    leagueCheck = None
if leagueCheck:
    print('success')

#Team
teamCheck = True
teamGet_code = requests.get(urlTeam).status_code
teamPost_code = requests.post(urlTeam).status_code
print("Test - Get and Post")
if teamGet_code != 200:
    print('Team Get =', teamGet_code)
    teamCheck = None
if teamPost_code != 201:
    print('Team Post =', teamPost_code)
    teamCheck = None
if teamCheck:
    print('success')

#Player
playerCheck = True
playerGet_code = requests.get(urlPlayer).status_code
playerPost_code = requests.post(urlPlayer).status_code
print("Player - Get and Post")
if playerGet_code != 200:
    print('Player Get =', playerGet_code)
    playerCheck = None
if playerPost_code != 201:
    print('Player Post =', playerPost_code)
    playerCheck = None
if playerCheck:
    print('success')




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

'''
expectedStatus = 200 #and 201 for successes
expectedText = {"hello": "world"}
print(url)
print("HelloWorld:", requests.get(url).status_code)
assert requests.get(url).status_code == expectedStatus
r = requests.get(url).json()

print("r =",r)
assert r == expectedText
'''