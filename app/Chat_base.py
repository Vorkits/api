from app.firebase_init import Firebase
import uuid
import app.firebase as fr
from hashlib import sha256
import time 
class Chat_base(Firebase):
    def create_chat(self,id):
        db=self.db
        db.child('chats').child(id).set({})
        return {'status':'success'}
    def get_chat(self,id):
        db=self.db
        data=db.child('chats').child(id).order_by_key().get().val()
        if not data:
            data={}
        return {'status':'success','data':dict(data),'hex':sha256(str(dict(data)).encode()).hexdigest()}
    def send_message(self,id,message,owner):
        db=self.db
        id=uuid.uuid4().hex
        ts = str(int(time.time()))
        message_id=ts+id
        data=dict(db.child('users').child(owner).get().val())
        message_data={'owner':owner,'message':message,'name':data['name'],'photo':data['photo']}
        db.child('chats').child(id).child(message_id).set(message_data)
        return {'status':'success'}