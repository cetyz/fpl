# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 23:34:27 2019

@author: Cetyz
"""

import pandas as pd
import numpy as np
from api_functions import FPL
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import seaborn as sns

fpl = FPL()

file_path = 'player_data.csv'

df = pd.read_csv(file_path, encoding='utf-8')
#print(df.head())

# let's do some basic feature engineering
# what i want to do now is somehow convert the season_name variable into some
# sort of 'recency' variable because i'm guessing recent performance will be
# more indicative than compared to past performance
# let's do it on a scale of 0-1 where 1 is the most recent (i.e. 2018/2019)

# let's first convert 2018/19 to simply 2019, etc
df.loc[:, 'latest_year'] = df.loc[:, 'season_name'].str.split('/').str[1].astype(float)
# then calculate our 'recency' variable by dividing by the max
# means out latest season would be 1
# data won't be on an interval scale but i think it's fine for now
# we can do it properly if we have more time
df.loc[:, 'recency'] = df.loc[:, 'latest_year'] / df.loc[:, 'latest_year'].max()

# our final dataset that we want to predict will be the most updated data
# so we need to NOT include 2019 in our model fitting

df_test = df.loc[df['latest_year'] == 19]
df = df.loc[df['latest_year'] != 19]

# our target
target = ['total_points']
# let's identify out features
features = ['minutes', 'goals_scored', 'clean_sheets', 'goals_conceded', 
            'own_goals', 'penalties_saved', 'penalties_missed', 'yellow_cards',
            'red_cards', 'saves', 'influence', 'creativity', 'threat']

# by printing the following we know that 
# type 1 = goalkeepers
# type 2 = defenders
# type 3 = midfielders
# type 4 = forwards
#print(fpl.get_element_types())

# i assume that different roles will have different important features
# so firstly, let's split the elements (players) up

gkp_df = df.loc[df['element_type'] == 1].reset_index(drop=True)
def_df = df.loc[df['element_type'] == 2].reset_index(drop=True)
mid_df = df.loc[df['element_type'] == 3].reset_index(drop=True)
fwd_df = df.loc[df['element_type'] == 4].reset_index(drop=True)

gkp_test_df = df_test.loc[df_test['element_type'] == 1].reset_index(drop=True)
def_test_df = df_test.loc[df_test['element_type'] == 2].reset_index(drop=True)
mid_test_df = df_test.loc[df_test['element_type'] == 3].reset_index(drop=True)
fwd_test_df = df_test.loc[df_test['element_type'] == 4].reset_index(drop=True)

########### FOR GOALKEEPERS

gkp_X, gkp_y = gkp_df[features].values, gkp_df[target].values
gkp_X_test, gkp_y_test = gkp_test_df[features].values, gkp_test_df[target].values
#gkp_X_train, gkp_X_test, gkp_y_train, gkp_y_test = train_test_split(
#        gkp_X, gkp_y, test_size=0.2, random_state=1)

model_gkp = LinearRegression()

#model.fit(gkp_X_train, gkp_y_train)
#predictions = model.predict(gkp_X_test)
#residuals = gkp_y_test - predictions

model_gkp.fit(gkp_X, gkp_y)
gkp_predictions = pd.DataFrame(model_gkp.predict(gkp_X_test))
gkp_results = gkp_test_df.join(gkp_predictions)
gkp_results.to_csv('gkp_results.csv', index=False)

########### FOR DEFENDERS

def_X, def_y = def_df[features].values, def_df[target].values
def_X_test, def_y_test = def_test_df[features].values, def_test_df[target].values

model_def = LinearRegression()
model_def.fit(def_X, def_y)
def_predictions = pd.DataFrame(model_def.predict(def_X_test))
def_results = def_test_df.join(def_predictions)
def_results.to_csv('def_results.csv', index=False)

########### FOR MIDFIELDERS

mid_X, mid_y = mid_df[features].values, mid_df[target].values
mid_X_test, mid_y_test = mid_test_df[features].values, mid_test_df[target].values

model_mid = LinearRegression()
model_mid.fit(def_X, def_y)
mid_predictions = pd.DataFrame(model_mid.predict(mid_X_test))
mid_results = mid_test_df.join(mid_predictions)
mid_results.to_csv('mid_results.csv', index=False)

########### FOR FORWARDS

fwd_X, fwd_y = fwd_df[features].values, fwd_df[target].values
fwd_X_test, fwd_y_test = fwd_test_df[features].values, fwd_test_df[target].values

model_fwd = LinearRegression()
model_fwd.fit(fwd_X, fwd_y)
fwd_predictions = pd.DataFrame(model_fwd.predict(fwd_X_test))
fwd_results = fwd_test_df.join(fwd_predictions)
fwd_results.to_csv('fwd_results.csv', index=False)
