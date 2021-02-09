from app.firebase_init import Firebase
import uuid
import app.firebase as fr
class Notes_base(Firebase):
    
    def send_message(self,f,t,text):
        db=self.db
        message_id=uuid.uuid4().hex
        
        notes=db.child('users').child(t).child('notes').child('messages').get().val()
        if notes:
            notes=dict(notes)
            if len(notes>50):
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
    
    def confirm_game(self,game_id,id):
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
        
        m_data=db.child('matches').child(game_id).get().val()
        try:
            m_data=dict(m_data)
        except:
            m_data={}            
        m_data['status']='confirm'
        db.child('matches').child(game_id).set(m_data)
        return {'status':'success'}
    
    def confirm_command(self,command_id,id):
        db=self.db
        notes=db.child('users').child(id).child('notes').child('commands').get().val()
        if notes:
            notes=dict(notes)
            notes['count']-=1
            notes.pop(command_id)
        else:
            notes={}
            notes['count']=0
        db.child('users').child(id).child('notes').child('commands').set(notes)
        
        m_data=db.child('matches').child(command_id).get().val()
        try:
            m_data=dict(m_data)
        except:
            m_data={}
        m_data['status']='confirm'
        db.child('matches').child(command_id).set(m_data)
        return {'status':'success'}
    def get(self,id):
        db=self.db
        notes=db.child('users').child(id).child('notes').get().val()
        try:
            notes=dict(notes)
        except:
            notes={}
        return {'status':'success','data':notes}