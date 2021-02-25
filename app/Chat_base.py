from app.firebase_init import Firebase
import uuid
import app.firebase as fr
from hashlib import sha256
import time 
import json

class Chat_base(Firebase):
    def create_chat(self,id,users):
        db=self.db
        users=json.loads(users)
        print(users)
        for i in users:
            user_db=dict(db.child('users').child(i).get().val())
            try:
                chats=user_db['chats']
            except:
                chats={}
            chats[id]=id
            user_db['chats']=chats
            db.child('users').child(i).set(user_db)
        db.child('chats').child(id).set({'status':''})
        return {'status':'success'}
    def add_chat(self,id,user):
        db=self.db
        users=json.loads(users)
    
        user_db=dict(db.child('users').child(user).get().val())
        try:
            chats=user_db['chats']
        except:
            chats={}
        chats[id]=id
        user_db['chats']=chats
        db.child('users').child(user).set(user_db)
        # chat_db=dict(db.child('chats').child(id).get().val())

        return {'status':'success'}
    def get_chat(self,id):
        db=self.db
        data=db.child('chats').child(id).get().val()
        if not data:
            data={}
        return {'status':'success','data':dict(data),'hex':sha256(str(dict(data)).encode()).hexdigest()}
    def send_message(self,id,message,owner):
        db=self.db
        # m_id=uuid.uuid4().hex
        # ts = str(int(time.time()))
        message_id=len(db.child('chats').child(id).get().val())
        data=dict(db.child('users').child(owner).get().val())
        # print(data)
        
        message_data={'owner':owner,'message':message,'name':data['name'],'photo':data['photo']}
        db.child('chats').child(id).child(message_id).set(message_data)
        return {'status':'success'}