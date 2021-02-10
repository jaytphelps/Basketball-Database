import pymysql
global list
global players
list = []
hometeam_players = []
awayteam_players = []

def connect():
    conn = pymysql.connect(host='mysql.clarksonmsda.org', port=3306, user='phelpsjt',
                                passwd='Mbj909698!', db='phelpsjt_IS437', autocommit=True)
    cur = conn.cursor(pymysql.cursors.DictCursor)

def close():
    cur.close()
    conn.close()

#``` Left 3's
# L3DW = Left 3pt Deep Wing
# L3HW = Left 3pt High Wing
# L3LW = Left 3pt Low Wing
# L3BL = Left 3pt Base Line
#``` Left 2's
# L2E = Left 2pt Elbow
# L2S = Left 2pt Short
# L2M = Left 2pt Mid Range
# L2SC = Left 2pt Short Corner
# L2BL = Left 2pt Base Line
# L2FT = Left 2pt Free Throw
# L2PS = Left 2pt Paint Shot
# L2RC = Left 2pt Restricted Circle



def playerRecords():
    if len(players) > 0:
        while c != '0':
            input('1 - Enter Home Team Players\n2 - Enter Away Team Players\n')
            if c == '0':
                pass
            if c == '1':
                name = input('Enter Player Name:\n')
                number = input('Enter Player Number:\n')
                home_team_pd = {}
                home_team_pd['PlayerName'] = name
                home_team_pd['PlayerNumber'] = number

                hometeam_players.append(home_team_pd)
            if c == '2':
                name = input('Enter Player Name:\n')
                number = input('Enter Player Number:\n')
                away_team_pd = {}
                away_team_pd['PlayerName'] = name
                away_team_pd['PlayerNumber'] = number

                awayteam_players.append(away_team_pd)
            else:
                print('Nothing')
    return hometeam_players
    return awayteam_players

def displayPlayerRecords(players):
    n = 1
    s = ''
    if len(hometeam_players) == 0:
        return "-No Items-"
    for items in players:
        if 'PlayerName' in items.keys() and 'PlayerNumber' in items.keys():
            s += "===Home Team Members===\n" + str(n) + " " + items['PlayerName'] + ": " + "No." + items['PlayerNumber'] + "\n"
        else:
            s += str(n) + ".) -invalid item data-\n"
        n += 1
    if len(awayteam_players) == 0:
        return "-No Items-"
    for items in players:
        if 'PlayerName' in items.keys() and 'PlayerNumber' in items.keys():
            s += "===Away Team members===\n" + str(n) + " " + items['PlayerName'] + ": " + "No." + items['PlayerNumber'] + "\n"
        else:
            s += str(n) + ".) -invalid item data-\n"
        n += 1
    return s



def CreateShotRecord(list):
    v = None
    while v != '0':
        v = input("1 - Enter Shot Attempt\n0 - Done()\n")
        if v == '0':
            pass
        else:
            print(displayPlayerRecords(players))
            player = input("Player:\n")
            shot_status = input("Make/Miss:\n")
            location = input("Location:\n")
            clock = ''

            d = {}
            d['Player'] = player
            d['Shot Status'] = shot_status
            d['Shot Location'] = location
            d['Time of Shot'] = clock

            list.append(d)
    return list




c = None
while c != '0':
    c = input("1 - Enter Shot Tracker Menu\n2 - View Game Shot Records\n3 - Enter Team Rosters\n0 - Exit()\n")
    if c == '1':
        print('===Record Shot Attempts===')
        list = CreateShotRecord(list)
    elif c == '2':
        print('===Remove Record===')
        list = RemoveRecord(list)
    elif c == '3':
        playerRecords()
    elif c == '0':
        break
    else:
        print('Invalid command')
    print('Exited')



