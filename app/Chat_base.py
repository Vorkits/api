from app.firebase_init import Firebase
import uuid
import app.firebase as fr
from hashlib import sha256
import time 
class Chat_base(Firebase):
    def create_chat(self,id):
        db=self.db
        db.child('chats').child(id).set({'status':''})
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