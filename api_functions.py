# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 23:10:50 2019

@author: Cetyz
"""

import requests
import json

url = 'https://fantasy.premierleague.com/api/bootstrap-static/'

r = requests.get(url).text
response = json.loads(r)

#for key in response:
#    print(key)
    
events = response['events'] # info regarding the game (e.g. deadlines and highscores)
game_settings = response['game_settings'] # settings for the game (e.g. how many leagues you can join)
phases = response['phases'] # not sure, seems like different months
teams = response['teams'] # teams and their names and stats (like attack power, defence power)
total_players = response['total_players'] # an int for the total number of players in FPL
elements = response['elements'] # each "element" in elements is a player
element_stats = response['element_stats'] # list of some fields available per element
element_types = response['element_types'] # element can be goalkeeper, defender, midfielder, or forward

#for team in teams:
#    print(team)
    
team_hist_url = 'https://fantasy.premierleague.com/api/entry/20/history/' # where the 20 is the team id

player_hist_url = 'https://fantasy.premierleague.com/api/element-summary/1' # where 1 is the element(player) id

r = requests.get(player_hist_url).text
response = json.loads(r)

for key in response:
    print(key)