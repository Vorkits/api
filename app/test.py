# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import auth

# cred = credentials.Certificate("orac-9d788-firebase-adminsdk-2iqe3-61981ebf8f.json")
# firebase_admin.initialize_app(cred)

# for user in auth.list_users().iterate_all():
#     print("Deleting user " + user.uid)
#     auth.delete_user(user.uid)
# # import redis
# r = redis.Redis(host='localhost', port=6379, db=0)
# print(r.lpop('emails'))
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
server = smtplib.SMTP_SSL('in-v3.mailjet.com: 465')
server.login("5a5bb4f22839cc8a1a520bb6b67d7b53", '04cf4551f3d9c96a0bf249da0cd25559')
msg = MIMEMultipart()
password = "Vorkit"
msg['From'] = "euros04@mail.ru"
msg['To'] = 'reazer381@gmail.com'
msg['Subject'] = "Paddle notification"
msg.attach(MIMEText('sdsads', 'plain'))
server.sendmail(msg['From'], msg['To'], msg.as_string())