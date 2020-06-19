from RiotAPI import  RiotAPI
from UserData import UserData
from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
import spam

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
smtpHost = "smtp.gmail.com"
port = "587"

import telepot
bot = telepot.Bot('1217513157:AAFvzaHyy3zGSTWBcjFtarvX49BkfO9Yfhw')

IMAGE = {
    'IRON': 'Emblem_Iron.png',
    'BRONZE' : 'Emblem_Bronze.png',
    'SILVER':'Emblem_Silver.png',
    'GOLD':'Emblem_Gold.png',
    'PLATINUM':'Emblem_Platinum.png',
    'DIAMOND':'Emblem_Diamond.png',
    'MASTER':'Emblem_Master.png',
    'GRANDMASTER':'Emblem_Grandmaster.png',
    'CHALLENGER':'Emblem_Challenger.png',
}

user = UserData()
api = RiotAPI()
window = Tk(className=" LoL Search")
window.geometry("280x400")

def process_GetName():
    SummonerName = eName.get()
    print(SummonerName)
    r= api.get_summoner_by_name(SummonerName)
    print(api.get_league_by_summonerID(r['id']))
    user.getInfo(api.get_league_by_summonerID(r['id']))

    TextSolo.configure(text = "솔로랭크")
    SoloLabel.configure(text=str(user.Info['솔로랭크']['티어']+" "+user.Info['솔로랭크']['랭크']+" "+str(user.Info['솔로랭크']['점수'])))
    win = user.Info['솔로랭크']['승']
    lose = user.Info['솔로랭크']['패']
    WinRateSolo.configure(text= str(str(win+lose)+"전 "+str(win)+"승 "+str(lose)+"패\n (" + str(round(spam.percentage(win,lose),2))+"%)"))

    imgSolo = Image.open(IMAGE[user.Info['솔로랭크']['티어']])  # IMAGE[user.Info['자유랭크']['티어']]
    imgSolo = imgSolo.resize((100, 100), Image.ANTIALIAS)
    imageSolo = ImageTk.PhotoImage(imgSolo)
    TearSoloImg.configure(image=imageSolo)
    TearSoloImg.image = imageSolo

    f = open('전적.txt','a')
    f.write('닉네임: '+ eName.get()+'\n'+
            '솔로랭크'+'\n'+
            str(user.Info['솔로랭크']['티어'] + " " + user.Info['솔로랭크']['랭크'] + " " + str(user.Info['솔로랭크']['점수']))+ '\n'+
            str(str(win + lose) + "전 " + str(win) + "승 " + str(lose) + "패 (" + str(
                round(spam.percentage(win, lose), 2)) + "%)") + '\n')

    if user.Info['자유랭크']['티어'] != 0:
        TextTeam.configure(text="자유랭크")
        TeamLabel.configure(text=str(user.Info['자유랭크']['티어']+" "+user.Info['자유랭크']['랭크']+" "+str(user.Info['자유랭크']['점수'])))
        win = user.Info['자유랭크']['승']
        lose = user.Info['자유랭크']['패']
        WinRateTeam.configure(text=str(str(win + lose) + "전 " + str(win) + "승 " + str(lose) + "패\n (" + str(
            round(spam.percentage(win,lose), 2)) + "%)"))

        imgTeam = Image.open(IMAGE[user.Info['자유랭크']['티어']])
        imgTeam = imgTeam.resize((100, 100), Image.ANTIALIAS)
        imageTeam = ImageTk.PhotoImage(imgTeam)
        TearTeamImg.configure(image=imageTeam)
        TearTeamImg.image = imageTeam

        f.write(
            '자유랭크' + '\n' +
            str(user.Info['자유랭크']['티어'] + " " + user.Info['자유랭크']['랭크'] + " " + str(user.Info['자유랭크']['점수'])) +
            str(str(win + lose) + "전 " + str(win) + "승 " + str(lose) + "패 (" + str(
                round(spam.percentage(win, lose), 2)) + "%)") + '\n'
        )
    else:
        TextTeam.configure(text="")
        TeamLabel.configure(text="")
        WinRateTeam.configure(text="")
        TearTeamImg.configure(image = None)
        TearTeamImg.image=None


    f.write('\n')
    f.close()

    print(user.Info)

def process_SendEmail():
        title = str(eName.get()+"님의 전적 검색 내용입니다.")
        senderAddr = str(input('sender email address :'))
        recipientAddr = str(input('recipient email address :'))
        passwd = str(input(' input your password of gmail account :'))

        score_solo=str(user.Info['솔로랭크']['티어'] + " " + user.Info['솔로랭크']['랭크'] + " " + str(user.Info['솔로랭크']['점수']))
        win = user.Info['솔로랭크']['승']
        lose = user.Info['솔로랭크']['패']
        record_solo =str(str(win + lose) + "전 " + str(win) + "승 " + str(lose) + "패 (" + str(round(spam.percentage(win,lose), 2)) + "%)")

        msgSolo = str("솔로랭크: " + score_solo +"\n"+ record_solo)

        score_team=str(user.Info['자유랭크']['티어'] + " " + user.Info['자유랭크']['랭크'] + " " + str(user.Info['자유랭크']['점수']))
        win = user.Info['자유랭크']['승']
        lose = user.Info['자유랭크']['패']
        record_team =str(str(win + lose) + "전 " + str(win) + "승 " + str(lose) + "패 (" + str(round(spam.percentage(win,lose), 2)) + "%)")
        msgTeam = str("자유랭크: " + score_team+'\n'+record_team)

        msg = MIMEMultipart('alternative')

        msg['Subject'] = title  # set message
        msg['From'] = senderAddr
        msg['To'] = recipientAddr
        msgPart = MIMEText(msgSolo, 'plain')
        InfoPart = MIMEText(msgTeam,_charset='utf-8')
        msg.attach(msgPart)
        msg.attach((InfoPart))
        print("connect smtp server ... ")
        s = smtplib.SMTP(smtpHost, port)  # python3.6에서는 smtplib.SMTP(host,port)
        # s.set_debuglevel(1)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(senderAddr, passwd)  # 로그인
        s.sendmail(senderAddr, [recipientAddr], msg.as_string())
        s.close()
        print("Mail sending complete!!!")



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
bSendEmail = Button(window,font = bFont,text = "eMail", command = process_SendEmail)

bGetName.pack()
bGetName.place(x=220, y=90,width=50,height =40)

bSendEmail.pack()
bSendEmail.place(x=200,y=10,width=70,height=30)

rFont = font.Font(window,size = 10,weight='bold')

TextSolo = Label(window,font = rFont)
TextSolo.pack()
TextSolo.place(x=45,y=170)
TearSoloImg = Label(window)
TearSoloImg.pack()
TearSoloImg.place(x=20, y=200)
SoloLabel = Label(window,font = rFont)
SoloLabel.pack()
SoloLabel.place(x=20, y=310)
WinRateSolo = Label(window,font = rFont)
WinRateSolo.pack()
WinRateSolo.place(x=10,y=330)

TextTeam = Label(window,font = rFont)
TextTeam.pack()
TextTeam.place(x=170,y=170)
TearTeamImg = Label(window)
TearTeamImg.pack()
TearTeamImg.place(x=150,y=200)
TeamLabel = Label(window,font=rFont)
TeamLabel.pack()
TeamLabel.place(x=150,y=310)
WinRateTeam = Label(window,font = rFont)
WinRateTeam.pack()
WinRateTeam.place(x=150,y=330)

InitMainText()
window.mainloop()
