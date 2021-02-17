# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import auth

# cred = credentials.Certificate("orac-9d788-firebase-adminsdk-2iqe3-61981ebf8f.json")
# firebase_admin.initialize_app(cred)

# for user in auth.list_users().iterate_all():
#     print("Deleting user " + user.uid)
#     auth.delete_user(user.uid)

import redis
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import time
r = redis.Redis(host='localhost', port=6379, db=0)
while True:
     print(r.lpop('emails'))