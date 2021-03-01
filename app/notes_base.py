from app.firebase_init import Firebase
import uuid
import app.firebase as fr
import redis
import time as tm
r = redis.Redis(host='localhost', port=6379, db=0)

class Notes_base(Firebase):
    
    def send_message(self,f,t,text):
        db=self.db
        message_id=uuid.uuid4().hex
        
        notes=db.child('users').child(t).child('notes').child('messages').get().val()
        if notes:
            notes=dict(notes)
            if len(notes)>50:
                notes={}
            try:
                notes['count']+=1
            except:
                notes['count']=1
        else:
            notes={}
            notes['count']=1
            
        notes[message_id]={'from':f,'text':text}
        db.child('users').child(t).child('notes').child('messages').set(notes)
        return {'status':'success'}
    def check_messages(self,id):
        db=self.db
        notes=db.child('users').child(id).child('notes').child('messages').get().val()
        if notes:
            notes={}

        else:
            notes={}
        notes['count']=0
        db.child('users').child(id).child('notes').child('messages').set(notes)
        return {'status':'success'}
    
    def confirm_game(self,game_id,id,confirm=True):
        db=self.db
        notes=db.child('users').child(id).child('notes').child('games').get().val()
        if notes:
            notes=dict(notes)
            notes['count']-=1
            notes.pop(game_id)
        else:
            notes={}
            notes['count']=0
        db.child('users').child(id).child('notes').child('games').set(notes)
        if confirm:
            m_data=db.child('matches').child(game_id).get().val()
            try:
                m_data=dict(m_data)
            except:
                m_data={}            
            m_data['status']='confirm'
            db.child('matches').child(game_id).set(m_data)
            p1=m_data['player1']['id'].replace('&&','.')
            timenow=int(tm.time())
            place='place'
            r.rpush('emails',f"{p1}:{timenow}:{m_data['time']}:confirm_match:{place}:{m_data['player2']['name']}:{id}")
        else:
            m_data=dict(db.child('matches').child(game_id).get().val())
            db.child('matches').child(game_id).remove()
            data=dict(db.child('users').child(id).child('matches').get().val())
            data.pop(game_id)
            db.child('users').child(id).child('matches').set(data)
            p1=m_data['player1']['id'].replace('&&','.')
            timenow=int(tm.time())
            place='place'
            r.rpush('emails',f"{p1}:{timenow}:{m_data['time']}:reject_match:{place}:{m_data['player2']['name']}:{id}")
        return {'status':'success'}
    
    def confirm_command(self,command_id,id,confirm=True):
        db=self.db
        notes=db.child('users').child(id).child('notes').child('commands').get().val()
        print(notes)
        if notes:
            notes=dict(notes)
            notes['count']-=1
            notes.pop(command_id)
        else:
            notes={}
            notes['count']=0
        db.child('users').child(id).child('notes').child('commands').set(notes)
        if confirm:
            m_data=db.child('commands').child(command_id).get().val()
            try:
                m_data=dict(m_data)
            except:
                m_data={}
            m_data['status']='confirm'
            db.child('commands').child(command_id).set(m_data)
            p1=m_data['player1'].replace('&&','.')
            timenow=int(tm.time())
            place='place'
            r.rpush('emails',f"{p1}:{timenow}:time:confirm_command:{place}:name:{id}")
        else:
            db.child('commands').child(command_id).remove()
            data=dict(db.child('users').child(id).child('commands').get().val())
            data.pop(command_id)
            db.child('users').child(id).child('commands').set(data)
            p1=m_data['player1'].replace('&&','.')
            timenow=int(tm.time())
            place='place'
            r.rpush('emails',f"{p1}:{timenow}:time:confirm_command:{place}:name:{id}")
        return {'status':'success'}
    def get(self,id):
        db=self.db
        notes=db.child('users').child(id).child('notes').get().val()
        try:
            notes=dict(notes)
        except:
            notes={}
        return {'status':'success','data':notes}