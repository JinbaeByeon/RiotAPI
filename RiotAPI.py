
import json
import requests

URL = {
    'base': 'https://{region}.api.riotgames.com/{url}',
    'summoner_by_name_lol': 'lol/summoner/v{version}/summoners/by-name/{names}',
    'league_by_summonerID' : 'lol/league/v{version}/entries/by-summoner/{summonerID}'
}

API_VERSIONS = {
    'summoner_lol': '4',
    'league' : '4'
}

class RiotAPI(object):
    def __init__(self):
<<<<<<< HEAD
        self.api_key = "RGAPI-54e3bbb0-47aa-4fae-b2a5-1338ba80f83e"
=======
        self.api_key = "RGAPI-61ec6f0f-96bd-4ab2-ba36-55e1e8d6a784"
>>>>>>> ca74edd411edc75934c15acf982f31ca56596dab
        self.region = "kr"

    def _request(self,api_url,params={}):
        args = {'api_key':self.api_key}
        for key, value in params.items():
            if key not in args:
                args[key] = value
        response = requests.get(
            URL['base'].format(
                region = self.region,
                url = api_url
            ),
            params=args
        )
        print(response.url)
        return response.json()

    def get_summoner_by_name(self, name):
        api_url = URL['summoner_by_name_lol'].format(
            version = API_VERSIONS['summoner_lol'],
            names = name
        )
        return self._request(api_url)

    def get_league_by_summonerID(self,summonerID):
        api_url = URL['league_by_summonerID'].format(
            version = API_VERSIONS['league'],
            summonerID = summonerID
        )
        return self._request(api_url)
