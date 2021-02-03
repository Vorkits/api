from app.firebase_init import Firebase
import uuid
import app.firebase as fr
from hashlib import sha256

class Chat_base(Firebase):
    def create_chat(self,id):
        db=self.db
        db.child('chats').child(id).set({})
        return {'status':'success'}
    def get_chat(self,id):
        db=self.db
        data=db.child('chats').child(id).get().val()
        if not data:
            data={}
        return {'status':'success','data':dict(data),'hex':sha256(str(dict(data)).encode()).hexdigest()}
    def send_message(self,id,message,owner):
        db=self.db
        message_id=uuid.uuid4().hex
        message_data={'owner':owner,'message':message}
        data=db.child('chats').child(id).child(message_id).set(message_data)
        return {'status':'success'}