# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 15:24:09 2020

@author: Rémi
Cle du 25/03
"""
from RiotAPI import RiotAPI
import plotly.graph_objects as go
import json
from plotly.subplots import make_subplots
import plotly.io as pio

def main():
    i=0
    dicMatch = {}
    pio.renderers.default = 'browser'
    api = RiotAPI('RGAPI-b25354b0-d371-46cd-bf1b-3a8ccc3292d9')
    r = api.get_summoner_by_name('wardmisp')
    t = api.get_matches_by_puuid(r['puuid'],1)
    y = api.get_match_by_id(t[0])
    dicJoueur = {}
    for element in y['metadata']['participants']:
        nom = api.get_summoner_by_puuid(element)
        dicMatch[element] = api.get_matches_by_puuid(element,10)
        dicGame = {}
        for matchId in dicMatch[element]:
            dicChamp = {}
            dicTrait = {}
            i = i + 1
            u = api.get_match_by_id(matchId)
            if 'metadata' in u:
                    i = u['metadata']['participants'].index(element)
                    answer = u['info']['participants'][i]
                    traits = answer['traits']
                    for elem in traits:
                        dicTrait[elem['name']]=elem['tier_current']
                    classement = answer['placement']
                    unites = answer['units']
                    for elem in unites:
                        dicChamp[elem['character_id']]=elem['tier']
                        dicGame[matchId]={'Classement':classement,'Champion':dicChamp,'Trait':dicTrait}
        dicJoueur[nom['name']] = dicGame
    dicJoueur = json.dumps(dicJoueur)
    fichier = open("data.json", "w")
    fichier.write(dicJoueur)
    fichier.close()
    pio.show(create_graph_from_json('data.json'))
    return (dicJoueur)

def create_graph(dico,donnee,summoner,figure,row,col):
    fig = figure.add_trace(go.Scatterpolar(name=donnee + ' ' + summoner, r=[elem for elem in dico.values()], theta=[key for key in dico.keys()]),row=row,col=col)

def create_graph_from_json(datapath):
    with open(datapath) as json_data:
        data_dict = json.load(json_data)
        AveR={}
    row = 1
    fig = make_subplots(rows=8,cols=2,specs=[[{'type': 'polar'}]*8]*2)
    for key,val in data_dict.items():
        col = 1
        Champs =  { "TFT3_Poppy":0,
                      "TFT3_Zoe":0,
                      "TFT3_Ahri":0,
                      "TFT3_XinZhao":0,
                      "TFT3_Syndra":0,
                      "TFT3_Ashe":0,
                      "TFT3_VelKoz":0,
                      "TFT3_Fiora": 0,
                      "TFT3_Graves": 0,
                      "TFT3_Darius": 0,
                      "TFT3_Lucian": 0,
                      "TFT3_Jayce": 0,
                      "TFT3_Vi": 0,
                      "TFT3_Irelia": 0,
                      "TFT3_Gangplank": 0,
                      "TFT3_Leona": 0,
                      "TFT3_JarvanIV": 0,
                      "TFT3_Mordekaiser": 0,
                      "TFT3_Shaco": 0,
                      "TFT3_Lux": 0,
                      "TFT3_Jhin": 0,
                      "TFT3_Neeko": 0,
                      "TFT3_Karma": 0,
                      "TFT3_Malphite": 0,
                      "TFT3_KhaZix": 0,
                      "TFT3_Yasuo": 0,
                      "TFT3_KaiSa": 0,
                      "TFT3_Sona": 0,
                      "TFT3_MasterYi": 0,
                      "TFT3_Jinx": 0,
                      "TFT3_Kayle": 0,
                      "TFT3_TwistedFate": 0,
                      "TFT3_Caitlyn": 0,
                      "TFT3_Shen": 0,
                      "TFT3_Ezreal": 0,
                      "TFT3_WuKong": 0,
                      "TFT3_Thresh": 0,
                      "TFT3_Soraka": 0,
                      "TFT3_AurelionSol": 0,
                      "TFT3_Fizz": 0,
                      "TFT3_Ekko": 0,
                      "TFT3_MissFortune": 0,
                      "TFT3_Annie": 0,
                      "TFT3_Ziggs": 0,
                      "TFT3_Blitzcrank": 0,
                      "TFT3_ChoGath": 0,
                      "TFT3_Lulu": 0,
                      "TFT3_Xayah": 0,
                      "TFT3_Rumble": 0,
                      "TFT3_Rakan": 0,
                      "TFT3_Kassadin": 0,
                      "TFT3_Tresh": 0
           }
        Traits = {"Protector":0,
                     "Sniper":0,
                     "StarGuardian":0,
                     "Vanguard":0,
                     "Blaster": 0,
                     "Cybernetic": 0,
                     "Demolitionist": 0,
                     "ManaReaver": 0,
                     "Mercenary": 0,
                     "SpacePirate": 0,
                     "Set3_Blademaster": 0,
                     "Set3_Brawler": 0,
                     "Set3_Celestial": 0,
                     "Set3_Sorcerer": 0,
                     "Set3_Void": 0,
                     "DarkStar": 0,
                     "Infiltrator": 0,
                     "Set3_Mystic": 0,
                     "Rebel": 0,
                     "Valkyrie": 0,
                     "Chrono": 0,
                     "Starship": 0,
                     "MechPilot": 0
                     }
        AveRank = 0
        for valu in val.values():
            AveRank += valu['Classement']
            for cle,elem in valu['Champion'].items():
                if (cle in Champs):
                    Champs[cle] += elem
            for cle,elem in valu['Trait'].items():     
                if (cle in Traits):
                    Traits[cle] += elem
        AveR[key] = AveRank
        create_graph(Champs,'Champions',key,fig,col,row)
        col += 1
        create_graph(Traits,'Traits',key,fig,col,row)
        row += 1
    return(fig)
        
        

if __name__ == "__main__":
    main()