from RiotAPI import  RiotAPI
from UserData import UserData
from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
smtpHost = "smtp.gmail.com"
port = "587"

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
<<<<<<< HEAD
    user.getInfo(api.get_league_by_summonerID(r['id']))

    imgSolo = Image.open(IMAGE[user.Info['솔로랭크']['티어']])  # IMAGE[user.Info['자유랭크']['티어']]
    imgSolo = imgSolo.resize((100, 100), Image.ANTIALIAS)
    imageSolo = ImageTk.PhotoImage(imgSolo)
    TearSoloLabel.configure(image=imageSolo)
    TearSoloLabel.image = imageSolo
    imgTeam = Image.open(IMAGE[user.Info['자유랭크']['티어']])  # IMAGE[user.Info['자유랭크']['티어']]
    imgTeam = imgTeam.resize((100, 100), Image.ANTIALIAS)
    imageTeam = ImageTk.PhotoImage(imgTeam)
    TearTeamLabel.configure(image=imageTeam)
    TearTeamLabel.image = imageTeam


    print(user.Info)

def process_SendEmail():
        title = str(input('Title: '))
        senderAddr = str(int)
        senderAddr = str(input('sender email address :'))
        recipientAddr = str(input('recipient email address :'))
        msgtext = str(input('write message :'))
        passwd = str(input(' input your password of gmail account :'))
        msgInfo = str(user.Info)
        msg = MIMEMultipart('alternative')
        msg['Subject'] = title  # set message
        msg['From'] = senderAddr
        msg['To'] = recipientAddr
        msgPart = MIMEText(msgtext, 'plain')
        InfoPart = MIMEText(msgInfo,_charset='utf-8')
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

=======
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
>>>>>>> ca74edd411edc75934c15acf982f31ca56596dab


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


TearSoloLabel = Label(window)
TearSoloLabel.pack()
TearSoloLabel.place(x=20, y=200)
TearTeamLabel = Label(window)
TearTeamLabel.pack()
TearTeamLabel.place(x=140,y=200)

InitMainText()
window.mainloop()
