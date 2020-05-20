from RiotAPI import  RiotAPI
from UserData import UserData
from tkinter import *
from tkinter import font


api = RiotAPI()
window = Tk()
window.geometry("250x400")

def process_GetName():
    SummonerName = eName.get()
    print(SummonerName)
    r= api.get_summoner_by_name(SummonerName)
    r2 = api.get_league_by_summonerID(r['id'])
    print(r2)


def InitText():
    mFont = font.Font(window, size=20, weight='bold', family='Consolas')
    MainText = Label(window, font=mFont, text="LoL 전적검색")
    MainText.pack()
    MainText.place(x=30, y=10)

lName = Label(window, text="소환사명")
eName = Entry(window)
bGetName = Button(window, text="검색", command=process_GetName)

SummonerName = str

lName.place(x=5, y=55)
eName.pack()
eName.place(x=60, y=55)
bGetName.pack()
bGetName.place(x=210, y=50)

InitText()
window.mainloop()
