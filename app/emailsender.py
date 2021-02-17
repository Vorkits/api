import redis
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import time
r = redis.Redis(host='localhost', port=6379, db=0)

server = smtplib.SMTP_SSL('smtp.mail.ru: 465')
server.login("euros04@mail.ru", 'Spore005')

templates={
    'start':'Hello, you have registered for the tournament on #date# , #place#',
    '1day':'Hello, do not forget that you have registered for the tournament in #date# , #place#'
}
while True:
    try:
        letter=r.lindex('emails',0).decode('utf-8').split(':')
        email=letter[0]
        now=time.time()
        timeout=int(letter[1])
        t_date=letter[2]
        addr=letter[4]
        letter=templates[letter[3]]
        
        # print(addr,t_date,timeout)
        if timeout<now:
            date=datetime.fromtimestamp(int(t_date))
            letter=letter.replace('#date#',str(date)).replace('#place#',str(addr))
            msg = MIMEMultipart()
            password = "Vorkit"
            msg['From'] ="euros04@mail.ru"
            msg['To'] = email
            msg['Subject'] = "Tournament notification"
            msg.attach(MIMEText(letter, 'plain'))
            server.sendmail(msg['From'], msg['To'], msg.as_string())
            r.lpop('emails')
    except:
        r.lpop('emails')
    
    
    