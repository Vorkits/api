import pyrebase
import uuid
import os
# import app.firebase as fr
config = {
    "apiKey": "AIzaSyDYsYC0LnriZt1JxLKpFKV0HIfw2slT1ac",
    "authDomain": "orac-9d788.firebaseapp.com",
    "projectId": "orac-9d788",
    "storageBucket": "orac-9d788.appspot.com",
    "messagingSenderId": "364935870344",
    "appId": "1:364935870344:web:eacf38c9a8f1f53d8eac3d",
   "measurementId": "G-Y9LZYCKM4Y",
   "databaseURL":'https://orac-9d788-default-rtdb.firebaseio.com/',
   "serviceAccount": "orac-9d788-firebase-adminsdk-2iqe3-d7e78188c5.json"
  }
firebase = pyrebase.initialize_app(config)

class Firebase:
    def __init__(self):
        
        
        self.auth = firebase.auth()
        self.storage = firebase.storage()
        self.db = firebase.database()
        print('call')
        
        
