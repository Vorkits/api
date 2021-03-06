from app.firebase_init import Firebase
import uuid
import app.firebase as fr
from app.com_fb import Command_base
from app.Chat_base import Chat_base
import redis
import time
r = redis.Redis(host='localhost', port=6379, db=0)
class Tournament_base(Firebase):
    def create(self,date,count,owner,t,place,name,price):
        db=self.db
        t_data={}
        t_data['date']=date
        t_data['price']=price
        t_data['owner']=owner
        t_data['status']='created'
        t_data['place']=place
        t_data['commands']=[]
        t_data['count']=count
        t_data['type']=t
        t_data['name']=name
        count=int(count)
        t=int(t)
        if t==2:
            group_data={}
            for i in range(count//4):
                value="free"
                group_data[str(i)]={str(key): value for key in range(4)}
            t_data['group']=group_data
            count=count//2
        branch_data=[]
        player_id=1
        count=count//2
        prev=0
        while count>0:
            r={}
            games=[]
            
            for i in range(count):
                if prev==0:
                    games.append({
    
                        f'player1': { 'id': f"{player_id}", 'name': f"Command {player_id}", 'winner': False },
                        f'player2': { 'id': f"{player_id+1}", 'name': f"Command {player_id+1}", 'winner': True },
                    })
                else:
                    games.append({
    
                        f'player1': { 'id': f"{player_id}", 'name': f"Winner of 1/{count*2}", 'winner': False },
                        f'player2': { 'id': f"{player_id+1}", 'name': f"Winner of 1/{count*2}", 'winner': True },
                    })
                player_id+=2
            count=count//2
            prev+=1
            r['games']=games
            branch_data.append(r)
        t_data['bracket']=branch_data
        t_id=uuid.uuid4().hex
        t_data['id']=t_id
        Chat_base().create_chat(t_id,f"""["{owner}"]""",f'tournament {t_id}')
        db.child('tournaments').child(t_id).set(t_data)
        return {'status':'success','data':t_data}
    
    
    
    def join_command(self,tournament_id,t,command_id):
        db=self.db
        t=int(t)
        с={}
        data=dict(db.child('tournaments').child(tournament_id).get().val())
        status='success'
        allow=True
        try:
            for i in data['commands']:
                if i['id']==command_id:
                    allow=False
        except:
            pass
        if not data['status']=='created':
            status='finished'
        elif allow==False:
            return {'status':'command already joined'},402
        else:
            c=dict(db.child('commands').child(command_id).get().val())
            timenow=int(time.time())
            
            p1=c['player1'].replace('&&','.')
            p2=c['player2'].replace('&&','.')
            t=int(t)
            addr=data['place']
            tournament_date=int(data['date'])
            print(tournament_date)
            r.rpush('emails',f'{p1}:{timenow}:{tournament_date}:start:{addr}:user')
            r.rpush('emails',f'{p2}:{timenow}:{tournament_date}:start:{addr}:user')
            r.rpush('emails',f'{p1}:{tournament_date-25200}:{tournament_date}:1day:{addr}:user')
            r.rpush('emails',f'{p2}:{tournament_date-25200}:{tournament_date}:1day:{addr}:user')
            bracket=data['bracket'][0]['games']
            if t==1:
                m_key=''
                p_key=''
                p_index=0
                for index,match in enumerate( bracket):
                    for index2,players in enumerate( match):
                        if len(bracket[index][players]['id'])<3:
                            m_key=index
                            p_key=players
                            p_index=index2
                            break
                
                winner=False if p_index%2==0 else True
                
                bracket[m_key][p_key]={ 'id': command_id, 'name': c['name'], 'winner': winner }
            elif t==2:
                
                place=''
                group_id=''
                
                
                for  index,group in enumerate(data['group']):
                    for index2,p in enumerate(group) :
                        if p=='free':
                            place=index2
                            group_id=index
                            break
                data['group'][int(group_id)][int(place)]={'id':command_id,'name':c['name']}
            try:
                data['commands'].append(c)
            except:
                data['commands']=[]
                data['commands'].append(c)
            if len(data['commands'])>=int(data['count']):
                data['status']='finished'
            data=db.child('tournaments').child(tournament_id).set(data)
        return {'status':status,'data':data}
    def get_t(self,tournament_id):
        db=self.db
        
        data=db.child('tournaments').child(tournament_id).get().val()
        return {'status':'success','data':dict(data)}
    def get_all(self):
        db=self.db
        
        data=db.child('tournaments').get().val()
        return {'status':'success','data':dict(data)}
    def finish_t(self,tornament_id,winner):
        db=self.db
        data=db.child('tournaments').child(tornament_id).get().val()
        w_id=winner
        winner=Command_base().get_command(winner)['data']
        data['status']='end'
        data['winner']={'id':w_id,'name':winner['name'],'photo':winner['photo']}
        data=db.child('tournaments').child(tornament_id).set(data)
        return {'status':'success','data':dict(data)}
       
            
            
                
                
                

            
    