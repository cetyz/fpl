# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 23:10:50 2019

@author: Cetyz
"""

import requests
import json

class FPL():
    def __init__(self):
        self.bootstrap_url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
        self.team_hist_url_front = 'https://fantasy.premierleague.com/api/entry/'
        self.team_hist_url_back = '/history/'
        self.player_hist_url = 'https://fantasy.premierleague.com/api/element-summary/'

    # info regarding the game (e.g. deadlines and highscores)
    def get_events(self):
        url = self.bootstrap_url
        r = json.loads(requests.get(url).text)
        data = r['events']
        return(data)
    
    # settings for the game (e.g. how many leagues you can join)
    def get_game_settings(self):
        url = self.bootstrap_url
        r = json.loads(requests.get(url).text)
        data = r['game_settings']
        return(data)
    
    # not sure, seems like different months    
    def get_phases(self):
        url = self.bootstrap_url
        r = json.loads(requests.get(url).text)
        data = r['phases']
        return(data)
    
    # teams and their names and stats (like attack power, defence power)    
    def get_teams(self):
        url = self.bootstrap_url
        r = json.loads(requests.get(url).text)
        data = r['teams']
        return(data)
    
    # an int for the total number of players in FPL    
    def get_total_players(self):
        url = self.bootstrap_url
        r = json.loads(requests.get(url).text)
        data = r['total_players']
        return(data)
    
    # each "element" in elements is a player    
    def get_elements(self):
        url = self.bootstrap_url
        r = json.loads(requests.get(url).text)
        data = r['elements']
        return(data)
    
    # list of some fields available per element    
    def get_element_stats(self):
        url = self.bootstrap_url
        r = json.loads(requests.get(url).text)
        data = r['element_stats']
        return(data)
    
    # element can be goalkeeper, defender, midfielder, or forward    
    def get_element_types(self):
        url = self.bootstrap_url
        r = json.loads(requests.get(url).text)
        data = r['element_types']
        return(data)
    
    def get_team_history(self, team_id = 1):
        url = self.team_hist_url_front + str(team_id) + self.team_hist_url_back
        r = json.loads(requests.get(url).text)
        data = r
        return(data)
        
    def get_player_history(self, player_id = 1):
        url = self.player_hist_url + str(player_id)
        r = json.loads(requests.get(url).text)
        data = r
        return(data)



