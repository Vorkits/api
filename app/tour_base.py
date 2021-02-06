from app.firebase_init import Firebase
import uuid
import app.firebase as fr
from app.com_fb import Command_base
from app.Chat_base import Chat_base
class Tournament_base(Firebase):
    def create(self,date,count,owner,t,place):
        db=self.db
        t_data={}
        t_data['date']=date
        t_data['owner']=owner
        t_data['status']='created'
        t_data['place']=place
        t_data['commands']=[]
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
    
                        f'player1': { 'id': f"{player_id}", 'name': f"{player_id}", 'winner': False },
                        f'player2': { 'id': f"{player_id+1}", 'name': f"{player_id}", 'winner': True },
                    })
                else:
                    games.append({
    
                        f'player1': { 'id': f"{player_id}", 'name': f"Winner of {count*2}", 'winner': False },
                        f'player2': { 'id': f"{player_id+1}", 'name': f"Winner of {count*2}", 'winner': True },
                    })
                player_id+=2
            count=count//2
            prev+=1
            r['games']=games
            branch_data.append(r)
        t_data['bracket']=branch_data
        t_id=uuid.uuid4().hex
        t_data['id']=t_id
        Chat_base().create_chat(t_id)
        db.child('tournaments').child(t_id).set(t_data)
        return {'status':'success','data':t_data}
    
    def join_command(self,tournament_id,t,command_id,place=0,group_id=0,bracket_id=0):
        db=self.db
        t=int(t)
        data=dict(db.child('tournaments').child(tournament_id).get().val())
        bracket=data['bracket'][0]['games']
        if t==1:
            match=int(bracket_id)
            place='player'+str(place+1)
            winner=False if place%2==0 else True
            c=Command_base().get_command(command_id)['data']
            bracket[match][place]=={ 'id': command_id, 'name': c['name'], 'winner': winner }
        elif t==2:
            match=group_id
            place=str(place)
            group_id=str(group_id)
            c=Command_base().get_command(command_id)['data']
            print(data['group'])
            data['group'][int(group_id)][int(place)]={'id':command_id,'name':c['name']}
        try:
            data['commands'].append(command_id)
        except:
            data['commands']=[]
            data['commands'].append(command_id)
        data=db.child('tournaments').child(tournament_id).set(data)
        return {'status':'success','data':data}
    def get_t(self,tournament_id):
        db=self.db
        
        data=db.child('tournaments').child(tournament_id).get().val()
        return {'status':'success','data':dict(data)}
    def finish_t(self,tornament_id,winner):
        db=self.db
        data=db.child('tournaments').child(tornament_id).get().val()
        w_id=winner
        winner=Command_base().get_command(winner)['data']
        data['winner']={'id':w_id,'name':winner['name'],'photo':winner['photo']}
        return {'status':'success','data':dict(data)}
       
            
            
                
                
                

            
    