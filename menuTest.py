import pymysql
import datetime


class databaseOperations:
    def __init__(self):
        self.conn = None
        self.cur = None
        self.gameTitle = ''
        
    def connect(self):
        self.conn = pymysql.connect(host='mysql.clarksonmsda.org', port=3306, user= 'phelpsjt',
                                passwd='Mbj909698!', db= 'phelpsjt_Basketball', autocommit = True)
        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)
    
    def close(self):
        self.cur.close()
        self.conn.close()
    
    def createRoster(self):
        self.connect()
        global date_today
        date_today = datetime.date.today().strftime("%Y_%m_%d")
        
        first_team = input('Provide the home team name\n')
        second_team = input('Provide the away team name\n')
        self.gameTitle = date_today + "_" + first_team + "_vs_" + second_team
        sql = "CREATE TABLE " + self.gameTitle + " (Player_Name VARCHAR(30), Player_Number VARCHAR(2), Player_Team VARCHAR(30), Team_ID VARCHAR(5));"    
        self.cur.execute(sql)
        self.close()
        return True

    def saveRoster(self, listA, listB): #single argument (roster)
        #listA = roster.hometeam_players
        #listB = roster.awayteam_players
        self.connect()
        sql = "INSERT INTO " + self.gameTitle + "(`Player_Name`, `Player_Number`, `Player_Team`, `Team_ID`) VALUES (%s,%s,%s,%s);"
        for row in listA:
            self.cur.execute(sql,(row['Player_Name'], row['Player_Number'], row['Player_Team'], row['Team_ID']))
        self.close()
        self.connect()
        sql = "INSERT INTO " + self.gameTitle + "(`Player_Name`, `Player_Number`, `Player_Team`, `Team_ID`) VALUES (%s,%s,%s,%s);"
        for row in listB:
            self.cur.execute(sql,(row['Player_Name'], row['Player_Number'], row['Player_Team'], row['Team_ID']))
        self.close()
        return True
        

        
#do = databaseOperations()
#do.finalizeRoster()
#do.saveRoster()


    
class RosterEdits:
    def __init__(self):
        self.hometeam_players = []
        self.awayteam_players = []
        self.home_team_pd = {}
        self.away_team_pd = {}
        
    def HomePlayerRecords(self):
        c = None
        while c != '0':
            c = input('1 - Enter Home Team Name and Abrev.\n2 - Enter Home Team Players\n0 - Finished\n')
            if c == '0':
                pass
            elif c == '1':
                team_name = input('Enter Name\n')
                team_ID = input('Enter Team Abreviation (example: Clarkson = CLK)\n')
            else:
                name = input('Enter Player Name:\n')
                number = input('Enter Player Number:\n')
                self.home_team_pd = {}
                self.home_team_pd['Player_Name'] = name
                self.home_team_pd['Player_Number'] = number
                self.home_team_pd['Player_Team'] = team_name
                self.home_team_pd['Team_ID'] = team_ID

                self.hometeam_players.append(self.home_team_pd)
        

    def AwayPlayerRecords(self):
        c = None
        while c != '0':
            c = input('1 - Enter Away Team Name and Abrev.\n2 - Enter Away Team Players\n0 - Finished\n')
            if c == '0':
                pass
            elif c == '1':
                team_name = input('Enter Name\n')
                team_ID = input('Enter Team Abreviation (example: Clarkson = CLK)\n')
            else:
                name = input('Enter Player Name:\n')
                number = input('Enter Player Number:\n')
                self.away_team_pd = {}
                self.away_team_pd['Player_Name'] = name
                self.away_team_pd['Player_Number'] = number
                self.away_team_pd['Player_Team'] = team_name
                self.away_team_pd['Team_ID'] = team_ID
                
                self.awayteam_players.append(self.away_team_pd)


    def displayPlayerRecords(self):
        n = 1
        h = ''
        a = ''
        if len(self.hometeam_players) == 0:
            print("No Players in Home Team Roster")
        for items in self.hometeam_players:
            if 'Player_Name' in items.keys() and 'Player_Number' in items.keys():
                h +=  str(n) + " " + items['Player_Name'] + ": " + "No." + items['Player_Number'] + " --" + items['Team_ID'] + "\n"
            else:
                h += str(n) + ".) -invalid item data-\n"
            n += 1
        
        if len(self.awayteam_players) == 0:
            print("No Players in Away Team Roster")
        for items in self.awayteam_players:
            if 'Player_Name' in items.keys() and 'Player_Number' in items.keys():
                a += str(n) + " " + items['Player_Name'] + ": " + "No." + items['Player_Number'] + " --" + items['Team_ID'] + "\n"
            else:
                a += str(n) + ".) -invalid item data-\n"
            n += 1
        return h + a
        
                
        
    def RosterOperations(self):
        v = None
        while v != '0':
            v = input('1 - Home Team Roster\n2 -  Away Team Roster\n0 - Finished Editing Roster\n')
            if v == '0':
                pass
            if v == '1':
                self.HomePlayerRecords()
            if v == '2':
                self.AwayPlayerRecords()
        
    
r = RosterEdits()
do = databaseOperations()
c = None
while c != '0':
    c = input('3 - Enter Team Records/Build Rosters\n4 - Display Player Records\n5 - Submit Created Roster\n6 - Save Roster\n0 - Exit()\n')
    if c == '3':
        r.RosterOperations()        
    elif c == '4':
        print(r.displayPlayerRecords())
    elif c == '5':
        do.createRoster()
    elif c == '6':
        do.saveRoster(r.hometeam_players, r.awayteam_players)
        print('Team Records saved\n')
    elif c == '0':
        break
    else:
        print('Invalid Command')
        
    print('Exited')
    
    
    
    
    
    
    