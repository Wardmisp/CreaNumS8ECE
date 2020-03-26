from RiotAPI import RiotAPI
import json
import matplotlib.pyplot as plt
import ast
import json
from plotly.subplots import make_subplots
import plotly.io as pio
from math import pi

def main():
    i = 0
    dicTraitTotal = {"Protector":0,
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
                     "MechPilot": 0,
                     }
    dicChampTotal = { "TFT3_Poppy":0,
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
                      "TFT3_Tresh": 0,
           }
    pio.renderers.default = 'browser'
    dicMatch = {} #RGAPI-54db36cb-3ce3-41f1-a32c-7ab3a4857a97
    api = RiotAPI('RGAPI-54db36cb-3ce3-41f1-a32c-7ab3a4857a97')
    r = api.get_summoner_by_name('Laö Tseu')
    t = api.get_matches_by_puuid(r['puuid'], 1)
    y = api.get_match_by_id(t[0])

    dicJoueur = {}
    for element in y['metadata']['participants']:
        nom = api.get_summoner_by_puuid(element)
        dicMatch[element] = api.get_matches_by_puuid(element, 10)
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
                    dicTrait[elem['name']] = elem['tier_current']

                    if elem['name'] == 'Protector' and elem['tier_current'] >= 1:
                        dicTraitTotal['Protector'] = dicTraitTotal['Protector'] + 1

                    elif elem['name'] == 'Sniper' and elem['tier_current'] >= 1:
                        dicTraitTotal['Sniper'] = dicTraitTotal['Sniper'] + 1

                    elif elem['name'] == 'StarGuardian' and elem['tier_current'] >= 1:
                        dicTraitTotal['StarGuardian'] = dicTraitTotal['StarGuardian'] + 1

                    elif elem['name'] == 'Vanguard' and elem['tier_current'] >= 1:
                        dicTraitTotal['Vanguard'] = dicTraitTotal['Vanguard'] + 1

                    elif elem['name'] == 'Blaster' and elem['tier_current'] >= 1:
                        dicTraitTotal['Blaster'] = dicTraitTotal['Blaster'] + 1

                    elif elem['name'] == "Cybernetic" and elem['tier_current'] >= 1:
                        dicTraitTotal["Cybernetic"] = dicTraitTotal["Cybernetic"] + 1

                    elif elem['name'] == "Demolitionist" and elem['tier_current'] >= 1:
                        dicTraitTotal["Demolitionist"] = dicTraitTotal["Demolitionist"] + 1

                    elif elem['name'] == "ManaReaver" and elem['tier_current'] >= 1:
                        dicTraitTotal["ManaReaver"] = dicTraitTotal["ManaReaver"] + 1

                    elif elem['name'] == "Mercenary" and elem['tier_current'] >= 1:
                        dicTraitTotal["Mercenary"] = dicTraitTotal["Mercenary"] + 1

                    elif elem['name'] == "SpacePirate" and elem['tier_current'] >= 1:
                        dicTraitTotal["SpacePirate"] = dicTraitTotal["SpacePirate"] + 1

                    elif elem['name'] == "Set3_Blademaster" and elem['tier_current'] >= 1:
                        dicTraitTotal["Set3_Blademaster"] = dicTraitTotal["Set3_Blademaster"] + 1

                    elif elem['name'] == "Set3_Brawler" and elem['tier_current'] >= 1:
                        dicTraitTotal["Set3_Brawler"] = dicTraitTotal["Set3_Brawler"] + 1

                    elif elem['name'] == "Set3_Celestial" and elem['tier_current'] >= 1:
                        dicTraitTotal["Set3_Celestial"] = dicTraitTotal["Set3_Celestial"] + 1

                    elif elem['name'] == "Set3_Sorcerer" and elem['tier_current'] >= 1:
                        dicTraitTotal["Set3_Sorcerer"] = dicTraitTotal["Set3_Sorcerer"] + 1

                    elif elem['name'] == "Set3_Void" and elem['tier_current'] >= 1:
                        dicTraitTotal["Set3_Void"] = dicTraitTotal["Set3_Void"] + 1

                    elif elem['name'] == "DarkStar" and elem['tier_current'] >= 1:
                        dicTraitTotal["DarkStar"] = dicTraitTotal["DarkStar"] + 1

                    elif elem['name'] == "Infiltrator" and elem['tier_current'] >= 1:
                        dicTraitTotal["Infiltrator"] = dicTraitTotal["Infiltrator"] + 1

                    elif elem['name'] == "Set3_Mystic" and elem['tier_current'] >= 1:
                        dicTraitTotal["Set3_Mystic"] = dicTraitTotal["Set3_Mystic"] + 1

                    elif elem['name'] == "Rebel" and elem['tier_current'] >= 1:
                        dicTraitTotal["Rebel"] = dicTraitTotal["Rebel"] + 1

                    elif elem['name'] == "Valkyrie" and elem['tier_current'] >= 1:
                        dicTraitTotal["Valkyrie"] = dicTraitTotal["Valkyrie"] + 1

                    elif elem['name'] == "Chrono" and elem['tier_current'] >= 1:
                        dicTraitTotal["Chrono"] = dicTraitTotal["Chrono"] + 1

                    elif elem['name'] == "Starship" and elem['tier_current'] >= 1:
                        dicTraitTotal["Starship"] = dicTraitTotal["Starship"] + 1

                    elif elem['name'] == "MechPilot" and elem['tier_current'] >= 1:
                        dicTraitTotal["MechPilot"] = dicTraitTotal["MechPilot"] + 1

                classement = answer['placement']
                unites = answer['units']
                for elem in unites:
                    dicChamp[elem['character_id']] = elem['tier']
                    dicGame[matchId] = {'Classement': classement, 'Champion': dicChamp, 'Trait': dicTrait}
                    if elem['character_id'] == "TFT3_Zoe":
                        dicChampTotal["TFT3_Zoe"] = dicChampTotal["TFT3_Zoe"] + 1

                    elif elem['character_id'] == "TFT3_Poppy":
                        dicChampTotal["TFT3_Poppy"] = dicChampTotal["TFT3_Poppy"] + 1

                    elif elem['character_id'] == "TFT3_XinZhao":
                        dicChampTotal["TFT3_XinZhao"] = dicChampTotal["TFT3_XinZhao"] + 1

                    elif elem['character_id'] == "TFT3_Ahri":
                        dicChampTotal["TFT3_Ahri"] = dicChampTotal["TFT3_Ahri"] + 1

                    elif elem['character_id'] == "TFT3_Syndra":
                        dicChampTotal["TFT3_Syndra"] = dicChampTotal["TFT3_Syndra"] + 1

                    elif elem['character_id'] == "TFT3_Ashe":
                        dicChampTotal["TFT3_Ashe"] = dicChampTotal["TFT3_Ashe"] + 1

                    elif elem['character_id'] == "TFT3_VelKoz":
                        dicChampTotal["TFT3_VelKoz"] = dicChampTotal["TFT3_VelKoz"] + 1

                    elif elem['character_id'] == "TFT3_Fiora":
                        dicChampTotal["TFT3_Fiora"] = dicChampTotal["TFT3_Fiora"] + 1

                    elif elem['character_id'] == "TFT3_Graves":
                        dicChampTotal["TFT3_Graves"] = dicChampTotal["TFT3_Graves"] + 1

                    elif elem['character_id'] == "TFT3_Darius":
                        dicChampTotal["TFT3_Darius"] = dicChampTotal["TFT3_Darius"] + 1

                    elif elem['character_id'] == "TFT3_Lucian":
                        dicChampTotal["TFT3_Lucian"] = dicChampTotal["TFT3_Lucian"] + 1

                    elif elem['character_id'] == "TFT3_Jayce":
                        dicChampTotal["TFT3_Jayce"] = dicChampTotal["TFT3_Jayce"] + 1

                    elif elem['character_id'] == "TFT3_Vi":
                        dicChampTotal["TFT3_Vi"] = dicChampTotal["TFT3_Vi"] + 1

                    elif elem['character_id'] == "TFT3_Irelia":
                        dicChampTotal["TFT3_Irelia"] = dicChampTotal["TFT3_Irelia"] + 1

                    elif elem['character_id'] == "TFT3_Gangplank":
                        dicChampTotal["TFT3_Gangplank"] = dicChampTotal["TFT3_Gangplank"] + 1

                    elif elem['character_id'] == "TFT3_Leona":
                        dicChampTotal["TFT3_Leona"] = dicChampTotal["TFT3_Leona"] + 1

                    elif elem['character_id'] == "TFT3_JarvanIV":
                        dicChampTotal["TFT3_JarvanIV"] = dicChampTotal["TFT3_JarvanIV"] + 1

                    elif elem['character_id'] == "TFT3_Mordekaiser":
                        dicChampTotal["TFT3_Mordekaiser"] = dicChampTotal["TFT3_Mordekaiser"] + 1

                    elif elem['character_id'] == "TFT3_Shaco":
                        dicChampTotal["TFT3_Shaco"] = dicChampTotal["TFT3_Shaco"] + 1

                    elif elem['character_id'] == "TFT3_Lux":
                        dicChampTotal["TFT3_Lux"] = dicChampTotal["TFT3_Lux"] + 1

                    elif elem['character_id'] == "TFT3_Jhin":
                        dicChampTotal["TFT3_Jhin"] = dicChampTotal["TFT3_Jhin"] + 1

                    elif elem['character_id'] == "TFT3_Neeko":
                        dicChampTotal["TFT3_Neeko"] = dicChampTotal["TFT3_Neeko"] + 1

                    elif elem['character_id'] == "TFT3_Karma":
                        dicChampTotal["TFT3_Karma"] = dicChampTotal["TFT3_Karma"] + 1

                    elif elem['character_id'] == "TFT3_Malphite":
                        dicChampTotal["TFT3_Malphite"] = dicChampTotal["TFT3_Malphite"] + 1

                    elif elem['character_id'] == "TFT3_KhaZix":
                        dicChampTotal["TFT3_KhaZix"] = dicChampTotal["TFT3_KhaZix"] + 1

                    elif elem['character_id'] == "TFT3_Yasuo":
                        dicChampTotal["TFT3_Yasuo"] = dicChampTotal["TFT3_Yasuo"] + 1

                    elif elem['character_id'] == "TFT3_KaiSa":
                        dicChampTotal["TFT3_KaiSa"] = dicChampTotal["TFT3_KaiSa"] + 1

                    elif elem['character_id'] == "TFT3_Sona":
                        dicChampTotal["TFT3_Sona"] = dicChampTotal["TFT3_Sona"] + 1

                    elif elem['character_id'] == "TFT3_MasterYi":
                        dicChampTotal["TFT3_MasterYi"] = dicChampTotal["TFT3_MasterYi"] + 1

                    elif elem['character_id'] == "TFT3_Jinx":
                        dicChampTotal["TFT3_Jinx"] = dicChampTotal["TFT3_Jinx"] + 1

                    elif elem['character_id'] == "TFT3_Kayle":
                        dicChampTotal["TFT3_Kayle"] = dicChampTotal["TFT3_Kayle"] + 1

                    elif elem['character_id'] == "TFT3_TwistedFate":
                        dicChampTotal["TFT3_TwistedFate"] = dicChampTotal["TFT3_TwistedFate"] + 1

                    elif elem['character_id'] == "TFT3_Caitlyn":
                        dicChampTotal["TFT3_Caitlyn"] = dicChampTotal["TFT3_Caitlyn"] + 1

                    elif elem['character_id'] == "TFT3_Shen":
                        dicChampTotal["TFT3_Shen"] = dicChampTotal["TFT3_Shen"] + 1

                    elif elem['character_id'] == "TFT3_Ezreal":
                        dicChampTotal["TFT3_Ezreal"] = dicChampTotal["TFT3_Ezreal"] + 1

                    elif elem['character_id'] == "TFT3_WuKong":
                        dicChampTotal["TFT3_WuKong"] = dicChampTotal["TFT3_WuKong"] + 1

                    elif elem['character_id'] == "TFT3_Thresh":
                        dicChampTotal["TFT3_Thresh"] = dicChampTotal["TFT3_Thresh"] + 1

                    elif elem['character_id'] == "TFT3_Soraka":
                        dicChampTotal["TFT3_Soraka"] = dicChampTotal["TFT3_Soraka"] + 1

                    elif elem['character_id'] == "TFT3_AurelionSol":
                        dicChampTotal["TFT3_AurelionSol"] = dicChampTotal["TFT3_AurelionSol"] + 1

                    elif elem['character_id'] == "TFT3_Fizz":
                        dicChampTotal["TFT3_Fizz"] = dicChampTotal["TFT3_Fizz"] + 1

                    elif elem['character_id'] == "TFT3_Ekko":
                        dicChampTotal["TFT3_Ekko"] = dicChampTotal["TFT3_Ekko"] + 1

                    elif elem['character_id'] == "TFT3_MissFortune":
                        dicChampTotal["TFT3_MissFortune"] = dicChampTotal["TFT3_MissFortune"] + 1

                    elif elem['character_id'] == "TFT3_Annie":
                        dicChampTotal["TFT3_Annie"] = dicChampTotal["TFT3_Annie"] + 1

                    elif elem['character_id'] == "TFT3_Ziggs":
                        dicChampTotal["TFT3_Ziggs"] = dicChampTotal["TFT3_Ziggs"] + 1

                    elif elem['character_id'] == "TFT3_Blitzcrank":
                        dicChampTotal["TFT3_Blitzcrank"] = dicChampTotal["TFT3_Blitzcrank"] + 1

                    elif elem['character_id'] == "TFT3_ChoGath":
                        dicChampTotal["TFT3_ChoGath"] = dicChampTotal["TFT3_ChoGath"] + 1

                    elif elem['character_id'] == "TFT3_Lulu":
                        dicChampTotal["TFT3_Lulu"] = dicChampTotal["TFT3_Lulu"] + 1

                    elif elem['character_id'] == "TFT3_Xayah":
                        dicChampTotal["TFT3_Xayah"] = dicChampTotal["TFT3_Xayah"] + 1

                    elif elem['character_id'] == "TFT3_Rumble":
                        dicChampTotal["TFT3_Rumble"] = dicChampTotal["TFT3_Rumble"] + 1

                    elif elem['character_id'] == "TFT3_Rakan":
                        dicChampTotal["TFT3_Rakan"] = dicChampTotal["TFT3_Rakan"] + 1

                    elif elem['character_id'] == "TFT3_Kassadin":
                        dicChampTotal["TFT3_Kassadin"] = dicChampTotal["TFT3_Kassadin"] + 1

                    elif elem['character_id'] == "TFT3_Tresh":
                        dicChampTotal["TFT3_Tresh"] = dicChampTotal["TFT3_Tresh"] + 1

        dicJoueur[nom['name']] = dicGame

    print(dicTraitTotal)
    print(dicChampTotal)

    dicTraitTotal = json.dumps(dicTraitTotal)
    fichierTrait = open("dataTraitTotal.json", "w")
    fichierTrait.write(dicTraitTotal)
    fichierTrait.close()

    dicChampTotal = json.dumps(dicChampTotal)
    fichierChamp = open("dataChampTotal.json", "w")
    fichierChamp.write(dicChampTotal)
    fichierChamp.close()    
    
    dicJoueur = json.dumps(dicJoueur)
    fichier = open("data.json", "w")
    fichier.write(dicJoueur)
    fichier.close()
    
    validDictTraitTotal = ast.literal_eval(dicTraitTotal)
    listTraitKeys = [ k for k in validDictTraitTotal.keys() ]
    #print(listTraitKeys)

    listTraitValues = [ k for k in validDictTraitTotal.values() ]
     # But we need to repeat the first value to close the circular graph:
    listTraitValues.append(listTraitValues[0])
    #print(listTraitValues)

    
    validDictChampTotal = ast.literal_eval(dicChampTotal)
    listChampKeys = [ k for k in validDictChampTotal.keys() ]
    #print(listChampKeys)

    listChampValues = [ k for k in validDictChampTotal.values() ]
    listChampValues.append(listChampValues[0])
    #print(listChampValues)

    # number of variable
    L = len(listTraitKeys)
    
    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(L) * 2 * pi for n in range(L)]
    angles += angles[:1]


    fig = plt.figure()
    fig.subplots_adjust(hspace=0.5, wspace=0.5)
    fig.set_size_inches(18.5, 10.5)
    
    # Initialise the spider plot
    ax = fig.add_subplot(121, polar=True)

    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], listTraitKeys, color='grey', size=8)

    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([10, 20, 30], ["10", "20", "30"], color="grey", size=7)
    plt.ylim(0, 40)
    #plt.title('the compositions played on the last 10 games of each participant')
    ax.set_title('The compositions played on the last 10 games of each participant', pad=20)
    # Plot data
    ax.plot(angles, listTraitValues, linewidth=1, linestyle='solid')

    # Fill area
    ax.fill(angles, listTraitValues, 'b', alpha=0.1)
    
    # delete the last one
    listTraitValues.pop()
    
    
    
     # number of variable
    Lo = len(listChampKeys)
    
    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(Lo) * 2 * pi for n in range(Lo)]
    angles += angles[:1]

    # Initialise the spider plot
    bx = fig.add_subplot(122, polar=True)

    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], listChampKeys, color='grey', size=8)

    # Draw ylabels
    bx.set_rlabel_position(0)
    plt.yticks([10, 20, 30], ["10", "20", "30"], color="grey", size=7)
    plt.ylim(0, 30)
    bx.set_title('The champions played on the last 10 games of each participant', pad=20)
    # Plot data
    bx.plot(angles, listChampValues, linewidth=1, linestyle='solid')

    # Fill area
    bx.fill(angles, listChampValues, 'g', alpha=0.1)
    
    # delete the last one
    listChampValues.pop()
    pio.show(create_graph_from_json('data.json'))
    return (dicJoueur)

def create_graph(dico,donnee,summoner,figure,row,col):
    fig = figure.add_trace(go.Scatterpolar(name=donnee + ' ' + summoner, r=[elem for elem in dico.values()], theta=[key for key in dico.keys()]),row=row,col=col)

def create_graph_from_json(datapath):
    with open(datapath) as json_data:
        data_dict = json.load(json_data)
        AveR={}
    row = 1
    fig = make_subplots(rows=2,cols=8,specs=[[{'type': 'polar'}]*8]*2)
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