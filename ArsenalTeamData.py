# Feranmi Cornelius Oluwasikun
# 26/06/2022 -
# Getting Arsenals 2022 team data, making data into data frame
# Data - Player, Position, Apps, Mins, G, A, xG

# Import modules and packages
import requests
from bs4 import BeautifulSoup
import json
import pandas as pd


# scrape players info

base_url = "https://understat.com/team/"

# Gets the teams detail from the user
team_name = str(input("Input the team's name: "))
season = str(input("Input the season: "))
season = season[:4]

# creates the url
url = (base_url + team_name + "/" + season)

# gets the url using request
res = requests.get(url)

# parses the content using beautiful soup
soup = BeautifulSoup(res.content,"html.parser")
scripts = soup.find_all('script')

# Get only player data
strings = scripts[3].string



# Strip symbols
start_pos = strings.index("('") + 2
end_pos = strings.index("')")

json_data = strings[start_pos:end_pos]

json_data = json_data.encode('utf8').decode('unicode_escape')


# convert string to json format
data = json.loads(json_data)


#print(json.dumps(data, indent=4, sort_keys=True))

# Gather info in a list
player_name = []
position = []
games_played = []
minutes_played = []
goals = []
assists = []
xg = []

roster_stat = data

for index in range(len(roster_stat)):
    for key in roster_stat[index]:
        if key == 'player_name':
            player_name.append(roster_stat[index][key])
        if key == 'position':
            position.append(roster_stat[index][key])
        if key == 'games':
            games_played.append(roster_stat[index][key])
        if key == 'time':
            minutes_played.append(roster_stat[index][key])
        if key == 'goals':
            goals.append(roster_stat[index][key])
        if key == 'assists':
            assists.append(roster_stat[index][key])
        if key == 'xG':
            xg.append(roster_stat[index][key])


#print(roster_stat)


#for data in roster_stat:
    #print(data)

print(roster_stat)
# create data frame
labels = [player_name,games_played,goals,assists]
df = pd.DataFrame([player_name,games_played,goals,assists],index= labels)

print(df)