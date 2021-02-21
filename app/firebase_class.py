import pyrebase
import uuid
import os
import app.firebase as fr
from app.com_fb import Command_base
from app.firebase_init import Firebase
from app.Chat_base import Chat_base
import redis
import time as tm
r = redis.Redis(host='localhost', port=6379, db=0)

system_score={1:{'win':3,'lose':-1},
              2:{'win':3,'lose':-1},
              3:{'win':3,'lose':-1},
              4:{'win':3,'lose':-1.5},
              5:{'win':3,'lose':-1.5}}


    
    
class Games_base(Firebase):
    
    def create_match(self,player1,player2,time,coart=False,t=1,hour=False,place=''):
        db=self.db
        match_id=uuid.uuid4().hex
        match_data={}
        
        Chat_base().create_chat(match_id)
        if t==1:
            player1=fr.get_user(player1)
            player2=fr.get_user(player2)
            match_data={
                'time':time,
                'coart':coart,
                'player1':player1,
                'player2':player2,
                'type':t,
                'place':place,
                'status':'start',
                'winner':'',
                'score1':'',
                'score2':'',
                'hours':hour}
            print(player1,player2)
            p1=player1['id'].replace('&&','.')
            p2=player2['id'].replace('&&','.')
            timenow=1
            r.rpush('emails',f"{p1}:{timenow}:{time}:command_match_owner:{place}:{player2['name']}")
            # r.rpush('emails',f"{p2}:{timenow}:{time}:start_match:{place}:{player1['name']}")
            self.set_match_to_user(player1['id'],match_id)
            self.set_match_to_user(player2['id'],match_id,note=True)
        elif t==2:
            command1=Command_base().get_command(player1)['data']
            command2=Command_base().get_command(player2)['data']
            match_data={
                'time':time,
                'coart':coart,
                'player1':command1,
                'player2':command2,
                'type':t,
                'status':'start',
                'place':place,
                'winner':'',
                'score1':'',
                'score2':'',
                'hours':hour}
            p1=command1['player1']['id'].replace('&&','')
            p2=command2['player1']['id'].replace('&&','')
            timenow=1
            r.rpush('emails',f"{p1}:{timenow}:{time}:command_match_owner:{place}:{command2['name']}")
            # r.rpush('emails',f"{p2}:{timenow}:{time}:command_match:{place}:{command1['name']}")
            self.set_match_to_user(command1['player1']['id'],match_id)
            self.set_match_to_user(command1['player2']['id'],match_id)
            self.set_match_to_user(command2['player1']['id'],match_id,note=True)
            self.set_match_to_user(command2['player2']['id'],match_id,note=True)
            self.set_match_to_command(player1,match_id)
            self.set_match_to_command(player2,match_id)
        db.child('matches').child(match_id).set(match_data)
        return (match_id,match_data)
    def change_field(self,field,value,match_id):
        db=self.db
        data=dict(db.child('matches').child(match_id).get().val())
        data[field]=value
        db.child('matches').child(match_id).set(data)
        return True         

    def finish_match(self,score1,score2,match_id):
        db=self.db
        data=dict(db.child('matches').child(match_id).get().val())
        if data['status']=='finished':
            raise Exception('match was played')
        else:
            type=int(data['type'])
            winner=data['player1'] if score1>score2 else data['player2']
            data['winner']=winner['id']
            print('before user')
            print(winner)  
            if type==1:
                winner_data=dict(db.child('users').child(winner['id']).get().val())
            else:
                winner_data=dict(db.child('commands').child(winner['id']).get().val())
            print('after')
            score=winner_data['score']
            score+=3
            
            level=score//20
            
            winner_data['score']=score
            winner_data['level']=level
            if type==1:
                (db.child('users').child(winner['id']).set(winner_data))
            else:
                (db.child('commands').child(winner['id']).set(winner_data))
            #         user_form={'name':name,'city':city,'token':token,'score':0,'level':0,'photo':photo}
            loose_data={}
            looser=''
            print(data['player2'])
            if winner==data['player1']:
                
                looser='player2'
            else:
                looser='player1'
            if type==1:
                loose_data=dict(db.child('users').child(data[looser]['id']).get().val())
            else:
                loose_data=dict(db.child('commands').child(data[looser]['id']).get().val())
            score=loose_data['score']
            score+=3
            level=score//20
            if score>20:
                loose_data['score']=score
                loose_data['level']=level
            
            if type==1:
                db.child('users').child(data[looser]['id']).set(loose_data)
            else:
                db.child('commands').child(data[looser]['id']).set(loose_data)
            data['status']='finished'
            data['score1']=score1
            data['score2']=score2
            db.child('matches').child(match_id).set(data)
            return True
    def get_matches(self):
        print('getget')

        db=self.db
        print('getget')
        try:
            return dict(db.child('matches').get().val())
        except:
            return {}
    def get_match(self,match_id):
        db=self.db
        try:
            data=dict(db.child('matches').child(match_id).get().val())
            data['id']=match_id
            return data
        except:
            return {}
    def get_users_match(self,user):
        db=self.db
        try:
            data=dict(db.child('users').child(user).child('matches').get().val())
            matches=dict(db.child('matches').get().val())
            for i in data.keys():
                data[i]=matches(i)
            return data
        except:
            return {}
        
    def set_match_to_user(self,player,match_id,note=False):
        db=self.db
        print(player)
        userdata=db.child('users').child(player).child('matches').get().val()
        
        if userdata:
            userdata=dict(userdata)
            userdata[match_id]=match_id
        else:
            userdata={}
            userdata[match_id]=match_id
        db.child('users').child(player).child('matches').set(userdata)
        if note:
            notes=db.child('users').child(player).child('notes').child('games').get().val()
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
            notes[match_id]={"confirmed":False,'id':match_id}
            db.child('users').child(player).child('notes').child('games').set(notes)
        return True
    def set_match_to_command(self,player,match_id):
            db=self.db
        
            userdata=db.child('commands').child(player).child('matches').get().val()
            if userdata:
                userdata=dict(userdata)
                userdata[match_id]=match_id
            else:
                userdata={}
                userdata[match_id]=match_id
            db.child('commands').child(player).child('matches').set(userdata)
            return True
        
