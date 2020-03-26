# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 15:06:52 2020

@author: Rémi
"""
import requests
import RiotConsts as Consts

class RiotAPI(object):
    
    def __init__(self, api_key, region=Consts.REGIONS['europe_west']):
        self.api_key = api_key
        self.region = region
        
    def _request(self, api_url, params={}):
        args = {'api_key': self.api_key}
        for key,value in params.items():
            if key not in args:
                args[key] = value
        response = requests.get(
            Consts.URL['base'].format(
                    proxy=self.region,
                    url=api_url
                    ),
                params=args
                )
        return response.json()
    
    def _request_cont(self, api_url, params={}):
        args = {'api_key': self.api_key}
        for key,value in params.items():
            if key not in args:
                args[key] = value
        response = requests.get(
            Consts.URL['base_cont'].format(
                    url=api_url
                    ),
                params=args
                )
        return response.json()
        
    
    def get_summoner_by_name(self, name):
        api_url = Consts.URL['summoner_by_name'].format(
                version=Consts.API_VERSIONS['summoner'],
                names=name
                )
        return self._request(api_url)
    
    def get_summoner_by_puuid(self, puuid):
        api_url = Consts.URL['summoner_by_puuid'].format(
                version=Consts.API_VERSIONS['summoner'],
                puuids=puuid
                )
        return self._request(api_url)
    
    def get_matches_by_puuid(self, puuid, count):
        api_url = Consts.URL['match_by_puuid'].format(
                version=Consts.API_VERSIONS['summoner'],
                puuids=puuid,
                counts=count
                )
        return self._request_cont(api_url)
    
    def get_match_by_id(self, match_id):
        api_url = Consts.URL['match_by_id'].format(
                version=Consts.API_VERSIONS['summoner'],
                matchids=match_id
                )
        return self._request_cont(api_url)
    