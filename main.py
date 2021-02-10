class RosterEdits:
    def __init__(self):
        self.hometeam_players = []
        self.awayteam_players = []
        self.home_team_pd = {}
        self.away_team_pd = {}

    @property
    def HomePlayerRecords(self):
        c = None
        while c != '0':
            c = input('1 - Enter Home Team Name and Abrev.\n2 - Enter Home Team Players\n0 - Finished\n')
            if c =='0':
                pass
            elif c == '1':
                team_name = input('Enter Name\n')
            team_ID = input('Enter Team Abreviation (example: Clarkson = CLK)\n')
            else:
            name = input('Enter Player Name:\n')
            number = input('Enter Player Number:\n')
            self.home_team_pd = {}
            self.home_team_pd['PlayerName'] = name
            self.home_team_pd['PlayerNumber'] = number
            self.home_team_pd['Player_Team'] = team_name
            self.home_team_pd['Team_ID'] = team_ID

            self.hometeam_players.append(self.home_team_pd)
        return self.hometeam_players

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
                self.away_team_pd['PlayerName'] = name
                self.away_team_pd['PlayerNumber'] = number
                self.away_team_pd['Player_Team'] = team_name
                self.away_team_pd['Team_ID'] = team_ID

                self.awayteam_players.append(self.away_team_pd)
        return self.awayteam_players

    def displayPlayerRecords(self):
        n = 1
        h = ''
        a = ''
        if len(self.hometeam_players) == 0:
            print("No Players in Home Team Roster")
        for items in self.hometeam_players:
            if 'PlayerName' in items.keys() and 'PlayerNumber' in items.keys():
                h += "===Home Team Members===\n" + str(n) + " " + items['PlayerName'] + ": " + "No." + items[
                    'PlayerNumber'] + "\n"
            else:
                h += str(n) + ".) -invalid item data-\n"
            n += 1

        if len(self.awayteam_players) == 0:
            print("No Players in Away Team Roster")
        for items in self.awayteam_players:
            if 'PlayerName' in items.keys() and 'PlayerNumber' in items.keys():
                a += "===Away Team members===\n" + str(n) + " " + items['PlayerName'] + ": " + "No." + items[
                    'PlayerNumber'] + "\n"
            else:
                a += str(n) + ".) -invalid item data-\n"
            n += 1
        return h + a

    def RosterOperations(self):
        v = None
        while v != '0':
            v = input(
                '1 - Enter Team Names\n2 - Enter Home Team Roster\n3 - Enter Away Team Roster\n0 - Finished Editing Roster\n')
            if v == '0':
                pass
            if v == '1':
                self.teamNames()
            if v == '2':
                self.HomePlayerRecords
            if v == '3':
                self.AwayPlayerRecords()


r = RosterEdits()
c = None
while c != '0':
    c = input('3 - Enter Player records\n4 - DisplayPlayerRecords\n0 - Exit()\n')
    if c == '3':
        r.RosterOperations()
    elif c == '4':
        print(r.displayPlayerRecords())
    elif c == '5':
        r.saveRoster()
    elif c == '0':
        break
    else:
        print('Invalid Command')

    print('Exited')

