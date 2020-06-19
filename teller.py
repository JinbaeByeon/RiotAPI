import telepot
import time
from RiotAPI import RiotAPI
from UserData import UserData
import spam
TOKEN = '1217513157:AAFvzaHyy3zGSTWBcjFtarvX49BkfO9Yfhw'

MAX_MSG_LENGTH = 300

bot = telepot.Bot(TOKEN)
api = RiotAPI()
user = UserData()

def handle(msg):
    content_type,chat_type,chat_id = telepot.glance(msg)
    if content_type != 'text':
        bot.sendMessage(chat_id,'난 텍스트 이외의 메시지는 처리 못해요.')
        return

    text = msg['text']
    args = text.split(' ')

    if text.startswith('검색') and len(args)>1:
        print('전적 검색: ',args[1])
        r = api.get_summoner_by_name(args[1])
        print(api.get_league_by_summonerID(r['id']))
        user.getInfo(api.get_league_by_summonerID(r['id']))

        win = user.Info['솔로랭크']['승']
        lose = user.Info['솔로랭크']['패']
        bot.sendMessage(chat_id,'닉네임: ' + args[1])
        bot.sendMessage(chat_id,
                '솔로랭크' + '\n' +
                str(user.Info['솔로랭크']['티어'] + " " + user.Info['솔로랭크']['랭크'] + " " + str(
                    user.Info['솔로랭크']['점수'])) + '\n' +
                str(str(win + lose) + "전 " + str(win) + "승 " + str(lose) + "패 (" + str(
                    round(spam.percentage(win, lose), 2)) + "%)") + '\n')

        if user.Info['자유랭크']['티어'] != 0:
            win = user.Info['자유랭크']['승']
            lose = user.Info['자유랭크']['패']
            bot.sendMessage(chat_id,
                '자유랭크' + '\n' +
                str(user.Info['자유랭크']['티어'] + " " + user.Info['자유랭크']['랭크'] + " " + str(user.Info['자유랭크']['점수'])) +
                str(str(win + lose) + "전 " + str(win) + "승 " + str(lose) + "패 (" + str(
                    round(spam.percentage(win, lose), 2)) + "%)") + '\n'
            )

    else:
        bot.sendMessage(chat_id, '모르는 명령어입니다.\n 검색 [소환사명]')


bot.message_loop(handle)
print('Listening...')

while(1):
    time.sleep(10)