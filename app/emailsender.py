import redis
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import time
from smtplib import SMTPException
import redis
r = redis.Redis(host='localhost', port=6379, db=0)
domain = 'http://82.146.45.20'
server = smtplib.SMTP_SSL('smtp.yandex.ru: 465')
server.login("reazer37@yandex.ru", 'spore0005')


def safe_list_get(l, idx, default):
    try:
        return l[idx]
    except IndexError:
        return default


templates = {
    'start': f"""Hello, you have registered for the tournament on    Confirmation mail
Dear user, you’ve just signed up for the tournament
The tournament will take place the #place# , #date# 
Best regards

Mail di conferma
Caro User, hai appena preso parte al torneo da noi organizzato
Il torneo avrà luogo #place# , #date#
Distinti saluti 
""",
    '1day': """Dear user, you paddle tournament will start today at #date# , #place# 
Kinds regards

Caro User, il tuo torneo di padel comincerà oggi  #date# , #place# 
Distinti saluti 
""",
    'command_match_owner': """Dear user, you sent a message to #user# in order to have  a match the day #date# , #place#  
You will be informed when your opponent will accept or not your invitation, in order to organize a match the day you both agreed for . 
Kinds regards 

Caro User, hai appena inviato un invito per un match all’user #user# una proposta di match per #date# , #place# 
Riceverai una mail di conferma quando il tuo avversario risponderà e potrete organizzare il vostro match il giorno e la data da voi scelti
Distinti saluti
""",
    'reject_match': f"""Dear User, 
Unfortunately your opponent refused to have a match with you
Send him a message to propose another timeframe 
{domain}/OtherProfile/:#user_id#
Or find another player to our site.
{domain}/players
Best regards.

Caro User, 
Sfortunatamente il tuo avversario ha rifiutato l’orario ed il girono da te proposti
Contattalo per pattuire un altro giorno ed ora
{domain}/OtherProfile/:#user_id#
Oppure organizza un altro match con un altro player
{domain}/players
Distinti saluti 
""",
    'confirm_match': f"""Dear user,
Great news, your opponent has just accepted the invite you sent him 
Contact him in order to coordinate where having the match 
Best regards 
{domain}/OtherProfile/:#user_id#
Caro User, 
Ottime notizie, il tuo avversario ha appena accettato di avere un match con te
Contattato per fissare dove avere il match
Distinti saluti 
{domain}/OtherProfile/:#user_id#
""",'validation': f"""Dear user, you have registered in paddle platform, please confirm your email by link.
    #user#
"""
,



 'command_owner': f"""Dear user, you sent a message to {domain}/OtherProfile/:#user_id# in order to have a couple
You will be informed when your opponent will accept or not your invitation, in order to organize a match the day you both agreed for . 
Kinds regards 

Caro User, hai appena inviato un invito per un match all’user {domain}/OtherProfile/:#user_id# una proposta di couple
Riceverai una mail di conferma quando il tuo avversario risponderà e potrete organizzare il vostro match il giorno e la data da voi scelti
Distinti saluti
""",
    'reject_command': f"""Dear User, 
Unfortunately your opponent refused to have a couple with you
Send him a message to propose another timeframe 
{domain}/OtherProfile/:#user_id#
Or find another player to our site.
{domain}/players
Best regards.

Caro User, 
Sfortunatamente il tuo avversario ha rifiutato l’orario ed il girono da te proposti
Contattalo per pattuire un altro giorno ed ora
{domain}/OtherProfile/:#user_id#
Oppure organizza un altro match con un altro player
{domain}/players
Distinti saluti 
""",
    'confirm_command': f"""Dear user,
Great news, your opponent has just accepted the couple
{domain}/OtherProfile/:#user_id#
Caro User, 
Ottime notizie, il tuo avversario ha appena accettato di avere un match con te
Contattato per fissare dove avere il match
Distinti saluti 
{domain}/OtherProfile/:#user_id#
""",}

while True:
    # try:
        time.sleep(1)
        letter = r.lindex('emails', 0)
        print(letter)
        try:
            letter = letter.decode('utf-8').split(':')
        except:
            continue
        email = letter[0]
        # print(letter)
        now = time.time()
        timeout = int(letter[1])
        t_date = letter[2] 
        addr = letter[4]
        user = letter[5].replace('*',':')
        user_id = safe_list_get(letter, 6, '')
        letter = templates[letter[3]]

        print(user, user_id)
        # print(addr,t_date,timeout)
        if timeout < now:
            try:
                date = datetime.fromtimestamp(int(t_date))
            except:
                date=''
            letter = letter.replace('#date#', str(date)).replace('#place#', str(
                'place')).replace('#user#', str(user)).replace('#user_id#', str(user_id))
            msg = MIMEMultipart()
            password = "Vorkit"
            msg['From'] = "reazer37@yandex.ru"
            msg['To'] = email
            msg['Subject'] = "Paddle notification"
            msg.attach(MIMEText(letter, 'plain'))
            try:
                server.sendmail(msg['From'], msg['To'], msg.as_string())
            except Exception as e:
                    print(e,'probleeem')
                    server.close()
                    server = smtplib.SMTP_SSL('smtp.yandex.ru: 465')
                    server.login("reazer37@yandex.ru", 'spore0005')
                    server.sendmail(msg['From'], msg['To'], msg.as_string())
                    continue
            r.lpop('emails')
    # except Exception as e:
    #     print(e)
    #     r.lpop('emails')
