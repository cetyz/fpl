# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 00:09:14 2019

@author: Cetyz
"""

from api_functions import FPL
import csv
import os

fpl = FPL()

# let's create a dataset of elements (players)
elements = fpl.get_elements()

# what will our data look like?
# each row will be a historical season of each element?
# so number of rows would be the sum of the number of seasons played by each player

# get some descriptors in
# like player name, what team they are on, how much they cost now, their position
# and also the data like goals conceded, goals scored, assists, etc

# manually take a look at available fields
all_fields_from_element = elements[0].keys()

# uncomment to view
#print(all_fields_from_element)

# manually look at available historical fields
player_history = fpl.get_player_history()
all_fields_from_player_history = player_history['history_past'][0].keys()
# uncomment to view
#print(all_fields_from_player_history)


headers = []
# and now we add them
# we can start small and expand if necessary    
selected_fields_from_element_data = ['id', 'first_name', 'second_name',
                                     'element_type', 'team', 'team_code', 
                                     'now_cost',]
# questions:
# 1. difference between team and team_code?

selected_fields_from_historical_data = ['season_name', 'total_points', 
                   'minutes', 'goals_scored', 'clean_sheets', 'goals_conceded',
                   'own_goals', 'penalties_saved', 'penalties_missed',
                   'yellow_cards', 'red_cards', 'saves', 'influence',
                   'creativity', 'threat']

headers = selected_fields_from_element_data + selected_fields_from_historical_data


# create the empty csv and write headers
if 'player_data.csv' not in os.listdir():
    with open('player_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)

with open('player_data.csv', 'a', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    for element in elements:
        element_id = element['id']
        element_historical_seasons = fpl.get_player_history(element_id)['history_past']
        for season in element_historical_seasons:
            row = []
            for field in selected_fields_from_element_data:
                row.append(str(element[field]))
            for field in selected_fields_from_historical_data:
                row.append(str(season[field]))
            print('Writing data for', element['first_name'], element['second_name'], 'Season', season['season_name'])
#            row = [s.encode('ascii', 'replace') if type(s) is str else s for s in row]
            writer.writerow(row)
