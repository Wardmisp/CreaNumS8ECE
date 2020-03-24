from RiotAPI import RiotAPI
import json


def main():
    i = 0
    dicMatch = {}
    api = RiotAPI('RGAPI-fba081d8-5304-4b01-b2d8-e06529a1b8bf')
    r = api.get_summoner_by_name('wardmisp')
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
                classement = answer['placement']
                unites = answer['units']
                for elem in unites:
                    dicChamp[elem['character_id']] = elem['tier']
                    dicGame[matchId] = {'Classement': classement, 'Champion': dicChamp, 'Trait': dicTrait}
        dicJoueur[nom['name']] = dicGame

    dicJoueur = json.dumps(dicJoueur)
    fichier = open("data.json", "w")
    fichier.write(dicJoueur)
    fichier.close()
    return (dicJoueur)


if __name__ == "__main__":
    main()