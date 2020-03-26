# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 20:00:42 2020

@author: Rémi
"""

URL = {
       'base' : 'https://{proxy}.api.riotgames.com/tft/{url}',
       'base_cont' : 'https://europe.api.riotgames.com/tft/{url}',
       'summoner_by_name':'summoner/v{version}/summoners/by-name/{names}',
       'summoner_by_puuid':'summoner/v{version}/summoners/by-puuid/{puuids}',
       'match_by_puuid':'match/v{version}/matches/by-puuid/{puuids}/ids?count={counts}',
       'match_by_id':'match/v{version}/matches/{matchids}'
       }

API_VERSIONS = {
        'summoner':'1'
        }
REGIONS = {
        'europe_nordic_and_east':'eune',
        'europe_west': 'euw1'
        }
