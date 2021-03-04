from app.firebase_init import Firebase
import uuid
import app.firebase as fr
from hashlib import sha256
import time 
import json
from threading import Thread
class Chat_base(Firebase):
    def create_chat(self,id,users,name=''):
        db=self.db
        users=json.loads(users)
        print(users)
        chat_name=''
        users_array=[]
        for i in users:
            user_db=dict(db.child('users').child(i).get().val())
            try:
                chats=user_db['chats']
            except:
                chats={}
            chats[id]={'id':id,'new_messages':False}
            users_array.append(i)
            user_db['chats']=chats
            chat_name+=user_db['name']+','
            db.child('users').child(i).set(user_db)

        db.child('chats').child(id).set({'id':id,'status':'','chat_name':name,'users':chat_name,'users_id':users_array})
        return {'status':'success'}
    def add_chat(self,id,user):
        db=self.db    
        user_db=dict(db.child('users').child(user).get().val())
        try:
            chats=user_db['chats']
        except:
            chats={}
        chats[id]=id
        user_db['chats']=chats
        db.child('users').child(user).set(user_db)
        chat_db=dict(db.child('chats').child(id).get().val())
        chat_db['users_id'].append(user)
        chat_db['users']+=user_db['name']+','
        db.child('chats').child(id).set(chat_db)
        return {'status':'success'}
    def get_chat(self,id,user_id):
        db=self.db
        data=db.child('chats').child(id).get().val()
        if not data:
            data={}
        thread = Thread(target=self.set_read_status,args=(id,user_id))
        thread.start()
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
        thread = Thread(target=self.set_unread_status,args=(id,True))
        thread.start()
        return {'status':'success'}

    def set_unread_status(self,chat_id,status):
        db=self.db
        print()
        chat_db=dict(db.child('chats').child(chat_id).get().val())
        users=chat_db['users_id']
        users_db=dict(db.child('users').get().val())
        for i in users:
            user_db=users_db[i]
            user_db['chats'][chat_id]['new_messages']=status
            db.child('users').child(i).set(user_db)
            
    def set_read_status(self,chat_id,user):
        db=self.db
        print(user)
        user_db=dict(db.child('users').child(user).get().val())
        user_db['chats'][chat_id]['new_messages']=False
        db.child('users').child(user).set(user_db)
        