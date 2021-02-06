import pyrebase
import uuid
import os
import app.firebase as fr

firebase = pyrebase.initialize_app(config)

class Firebase:
    def __init__(self):
        
        
        self.auth = firebase.auth()
        self.storage = firebase.storage()
        self.db = firebase.database()
        print('call')
        