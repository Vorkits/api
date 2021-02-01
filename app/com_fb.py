from app.firebase_class import Firebase
import uuid
import app.firebase as fr
class Command_base(Firebase):
    
    def create_command(self,player1,player2,name):
        try:
            db=self.db
            command_data={}
            owner_data=dict(db.child('users').child(player1).get().val())
            player2_data=dict(db.child('users').child(player2).get().val())
            command_data['city']=owner_data['city']
            owner_level=int(owner_data['level'])
            player2_level=int(player2_data['level'])
            command_data['score']=(owner_data['score']+player2_data['score'])//2
            command_data['level']=(owner_level+player2_level)//2
            command_data['player1']=player1
            command_data['player2']=player2
            command_data['owner']=player1
            command_data['matches']={}
            command_data['name']=name
            id=uuid.uuid4().hex
            db.child('commands').child(id).set(command_data)
            db.child('cityes').child(owner_data['city']).child('commands').child(id).set(command_data)
            self.set_command(player1,id)
            self.set_command(player2,id)
            return {'data':command_data},200
        except:
            return {'status':'error'},401
    def get_command(self,id):
        try:
            db=self.db
            data=dict(db.child('commands').child(id).get().val())
            data['player1']=fr.get_user(data['player1'])
            data['player2']=fr.get_user(data['player2'])
            return {'data':dict(data)}
        except:
            return {'status':'error'},401
    def set_field(self,id,field,value):
        try:
            db=self.db
            data=self.get_command(id)['data']
            data[field]=value
            db.child('commands').child(id).set(data)
        except:
            return {'status':'error'},401
    def get_by_city(self,city):
        try:
            db=self.db
            data=dict(db.child('cityes').child(city).child('commands').get().val())
            return {'data':data}
                
        except:
            return {'status':'error'},401
    def set_command(self,player,command_id):
        db=self.db
        data=db.child('users').child(player).child('commands').get().val()
        data=dict(data) if data else {}
        data[command_id]=command_id
        db.child('users').child(player).set(data)
        return True
     
        