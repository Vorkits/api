import pyrebase
import uuid
import os
import app.firebase as fr
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
system_score={1:{'win':3,'lose':-1},
              2:{'win':3,'lose':-1},
              3:{'win':3,'lose':-1},
              4:{'win':3,'lose':-1.5},
              5:{'win':3,'lose':-1.5}}
firebase = pyrebase.initialize_app(config)
class Firebase:
    def __init__(self):
        
        
        self.auth = firebase.auth()
        self.storage = firebase.storage()
        self.db = firebase.database()
        print('call')
        
    
    
class Games_base(Firebase):
    
    def create_match(self,player1,player2,time,coart=False,t=1,hour=False):
        db=self.db
        match_id=uuid.uuid4().hex
        t= 'pair' if type==2 else 'single'
        match_data={
            'time':time,
            'coart':coart,
            'player1':fr.get_user(player1),
            'player2':fr.get_user(player2),
            'type':t,
            'status':'start',
            'winner':'',
            'score1':'',
            'score2':'',
            'hours':hour}
        
        db.child('matches').child(match_id).set(match_data)
        self.set_match_to_user(player1,match_id)
        self.set_match_to_user(player2,match_id)
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
            winner=data['player1'] if score1>score2 else data['player2']
            data['winner']=winner['id']
            print('before user')
            print(winner)   
            winner_data=dict(db.child('users').child(winner['id']).get().val())
            print('after')
            score=winner_data['score']
            score+=3
            
            level=score//20
            
            winner_data['score']=score
            winner_data['level']=level
            (db.child('users').child(winner['id']).set(winner_data))
            #         user_form={'name':name,'city':city,'token':token,'score':0,'level':0,'photo':photo}
            loose_data={}
            looser=''
            print(data['player2'])
            if winner==data['player1']:
                loose_data=dict(db.child('users').child(data['player2']['id']).get().val())
                looser='player2'
            else:
                loose_data=dict(db.child('users').child(data['player1']['id']).get().val())
                looser='player1'
            score=loose_data['score']
            score+=3
            level=score//20
            if score>20:
                loose_data['score']=score
                loose_data['level']=level
            db.child('users').child(looser).set(loose_data)
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
            return dict(db.child('matches').child(match_id).get().val())
        except:
            return {}
    def get_users_match(self,user):
        db=self.db
        try:
            data=dict(db.child('users').child(user).child('matches').get().val())
            for i in data.keys():
                data[i]=self.get_match(i)
            return data
        except:
            return {}
        
    def set_match_to_user(self,player,match_id):
        db=self.db
        
        userdata=db.child('users').child(player).child('matches').get().val()
        if userdata:
            userdata=dict(userdata)
            userdata[match_id]=match_id
        else:
            userdata={}
            userdata[match_id]=match_id
        db.child('users').child(player).child('matches').set(userdata)
        return True
