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

    def saveRoster(self, listA, listB):
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
        
do = databaseOperations()
#do.createRoster()


home_team = [{'Player_Name': 'Ja Phelps', 'Player_Number': '12', 'Player_Team': 'Clarkson', 'Team_ID': 'CLK'},
            {'Player_Name': 'Joe Lucas', 'Player_Number': '0', 'Player_Team': 'Clarkson', 'Team_ID': 'CLK'}]
            
away_team = [{'Player_Name': 'Blake Hildman', 'Player_Number': '21', 'Player_Team': 'Vassar', 'Team_ID': 'VSR'},
            {'Player_Name': 'Josh Hipwell', 'Player_Number': '10', 'Player_Team': 'Vassar', 'Team_ID': 'VSR'}]
            
do.createRoster()
do.saveRoster(home_team, away_team)            








        
        