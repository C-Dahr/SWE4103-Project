import random
from itertools import combinations
from random import shuffle
from common.Scheduler import create_matches

teamList = [5,12,76,13,98,45]  # get this from Nathan's rotation algorithm
anonTeamList = [i for i in range(0,len(teamList))]
matchList = create_matches(anonTeamList)
print(matchList)

dateList = [1, 1, 1, 3, 4, 4, 5, 6, 6, 8, 9, 9, 9, 10,10]
print(len(dateList))

def findNextValid(matchList, dateList):
    try:
        (team1, team2, day)
    except NameError:
        team1 = matchList[0][0]
        team2 = matchList[0][1]
        day = dateList[0]
        yield matchList.pop(0), dateList.pop(0)  # init state
    while matchList:
        for idx, i in enumerate(matchList):
            if day == dateList[idx]:
                pass
            else:
                team1 = i[0]
                team2 = i[1]
                day = dateList[idx]
                matchList.pop(idx)
                yield i, dateList.pop(idx)
        team1 = matchList[0][0]
        team2 = matchList[0][1]
        yield matchList.pop(0), dateList.pop(0)


gen = findNextValid(matchList, dateList)
for i in range(15):
    print(next(gen))


