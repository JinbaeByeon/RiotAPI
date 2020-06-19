




class UserData(object):
    def __init__(self):
        self.Info = {
            '솔로랭크' :{
                '티어',
                '랭크',
                '점수',
                '승',
                '패'
            },
            '자유랭크':{
                '티어',
                '랭크',
                '점수',
                '승',
                '패'
            }

    }


    def getInfo(self,r):
        try:
            self.Info = {
                '솔로랭크': {
                    '티어': r[0]['tier'],
                    '랭크': r[0]['rank'],
                    '점수': r[0]['leaguePoints'],
                    '승': r[0]['wins'],
                    '패': r[0]['losses']
                },
                '자유랭크': {
                    '티어': r[1]['tier'],
                    '랭크': r[1]['rank'],
                    '점수': r[1]['leaguePoints'],
                    '승': r[1]['wins'],
                    '패': r[1]['losses']
                }
            }
        except:
            self.Info = {
                '솔로랭크': {
                    '티어': r[0]['tier'],
                    '랭크': r[0]['rank'],
                    '점수': r[0]['leaguePoints'],
                    '승': r[0]['wins'],
                    '패': r[0]['losses']
                },
                '자유랭크': {
                    '티어': 0,
                    '랭크': 0,
                    '점수': 0,
                    '승': 0,
                    '패': 0
                }
            }




    def show(self):
        print(self.Info)

