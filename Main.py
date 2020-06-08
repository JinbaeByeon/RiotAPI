from RiotAPI import  RiotAPI
from UserData import UserData
from tkinter import *
from tkinter import font


api = RiotAPI()
window = Tk(className=" LoL Search")
window.geometry("280x400")
def process_GetName():
    SummonerName = eName.get()
    print(SummonerName)
    r= api.get_summoner_by_name(SummonerName)
    r2 = api.get_league_by_summonerID(r['id'])
    Information = {
        '자유랭크' :{
            '티어': r2[0]['tier'],
            '랭크': r2[0]['rank'],
            '점수': r2[0]['leaguePoints'],
            '승': r2[0]['wins'],
            '패': r2[0]['losses']
        },
        '솔로랭크':{
            '티어': r2[1]['tier'],
            '랭크': r2[1]['rank'],
            '점수': r2[1]['leaguePoints'],
            '승': r2[1]['wins'],
            '패': r2[1]['losses']
        }
    }

    print(Information)


def InitMainText():
    mFont = font.Font(window, size=20, weight='bold', family='Consolas')
    MainText = Label(window, font=mFont, text="LoL 전적검색")
    MainText.pack()
    MainText.place(x=5, y=5)

mFont = font.Font(window, size=10, weight='bold', family='Consolas')
lName = Label(window, text="소환사명 혹은 챔피언명을 검색하세요",font =mFont)
eName = Entry(window,font=mFont,width=26,borderwidth=12,relief='ridge')
lName.place(x=5, y=60)
eName.pack()
eName.place(x=5, y=90)

bFont = font.Font(window,size=13, weight='bold', family='Consolas')
bGetName = Button(window, font = bFont,text="검색",  command=process_GetName)

bGetName.pack()
bGetName.place(x=220, y=90,width=50,height =40)



InitMainText()
window.mainloop()
