from app.firebase_init import Firebase
import uuid
import app.firebase as fr
import os
r = redis.Redis(host='localhost', port=6379, db=0)

class Command_base(Firebase):
    
    def create_command(self,player1,player2,name):
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
            command_data['status']='non confirm'
            command_data['photo']='https://firebasestorage.googleapis.com/v0/b/orac-9d788.appspot.com/o/avatars%2Fstandart.jpg?alt=media&token=eyJhbGciOiJSUzI1NiIsImtpZCI6IjljZTVlNmY1MzBiNDkwMTFiYjg0YzhmYWExZWM1NGM1MTc1N2I2NTgiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vb3JhYy05ZDc4OCIsImF1ZCI6Im9yYWMtOWQ3ODgiLCJhdXRoX3RpbWUiOjE2MTIxOTk3NDEsInVzZXJfaWQiOiJVODBuN1R1MHBaTzRLazNaTmNtSHVrSDU0bzcyIiwic3ViIjoiVTgwbjdUdTBwWk80S2szWk5jbUh1a0g1NG83MiIsImlhdCI6MTYxMjE5OTc0MSwiZXhwIjoxNjEyMjAzMzQxLCJlbWFpbCI6InJlYXplcjM5MjMyQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJyZWF6ZXIzOTIzMkBnbWFpbC5jb20iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJwYXNzd29yZCJ9fQ.N0D1eBdd7ar8KLvisVWtQSqJwP-gKX6nTxrJ13pPfrnhNT6otIDgBX7QXFzWkIa8MeXtnMSkDRW2SBIYP9jedyGvsJALJv9KMrbdfBNvf5WY2mTvQguqEdtaNg0bwlKTVhJglntb6py7_bNPLZBgKVLolHy3Yh-ye5QHN2vMCKUlXfRWkB4qeX4UEtpRF-TyBg0VB-d47CjaHQP3GmeFNcHeRtYu0Z2kOtMY1AW2YjPRYuCUJ1GU8HIQZmWGun_Nvl-AwM_IB5RgVecnUEIfbeuhPkMEROPTbPMI-Js81IrbcLTgC4ItSnk3_zob3OzQS4Jho27wXVzucjvMIQCE8A'
            id=uuid.uuid4().hex
            command_data['id']=id
            db.child('commands').child(id).set(command_data)
            db.child('cityes').child(owner_data['city']).child('commands').child(id).set(command_data)
            self.set_command(player1,id)
            self.set_command(player2,id)
            self.set_note(player2,command_data['id'],player1)
            p1=player1.replace('&&','.')
            timenow=1
            time=1
            place='place'
            r.rpush('emails',f"{p1}:{timenow}:{time}:command_owner:{place}:name:{player1}")
            return {'data':command_data},200
    
    
    def set_note(self,player,command_id,player1):
        db=self.db
        notes=db.child('users').child(player).child('notes').child('commands').get().val()
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
            
        notes[command_id]={"confirmed":False,'id':command_id,'owner':player1}
        db.child('users').child(player).child('notes').child('commands').set(notes)
    def get_command(self,id):
        try:
            db=self.db
            data=dict(db.child('commands').child(id).get().val())
            data['player1']=fr.get_user(data['player1'])
            data['player2']=fr.get_user(data['player2'])
            return {'data':dict(data)}
        except:
            return {'status':'error'},401
    def delete_command(self,id):
        try:
            db=self.db
            data=db.child('commands').child(id).remove()
            print('delete')
            return {'status':'success'}
        except:
            return {'status':'error'},401
    def get_commands(self,ids):
        # try:
            db=self.db
            players_data={}
            r_data={}
            all_data=dict(db.child('commands').get().val())
            for i in ids:
                try:
                    data=all_data[i]
                    if not players_data.get(data['player1']):
                        
                        p_data=fr.get_user(data['player1'])
                        
                        players_data[data['player1']]=p_data
                        data['player1']=p_data
                    else:
                        data['player1']=players_data[data['player1']]
                        
                    if not players_data.get(data['player2']):
                        p_data=fr.get_user(data['player2'])
                        
                        players_data[data['player2']]=p_data
                        data['player2']=p_data
                    else:
                        data['player2']=players_data[data['player2']]
                    r_data[i]=data
                except:
                    pass
                
                
            print(r_data)
            return {'data':dict(r_data)} 
        # except:
        #     return {'status':'error'},401
    def set_field(self,id,field,value):
        try:
            db=self.db
            data=dict(db.child('commands').child(id).get().val())
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
            return {'data':{}},200
    def set_command(self,player,command_id):
        db=self.db
        data=dict(db.child('users').child(player).get().val())
        commands=data.get('commands') if data.get('commands') else {}
        commands[command_id]=command_id
        data['commands']=commands
        db.child('users').child(player).set(data)
        return True
    def photo(self,command_id,photo):
        
        storage=self.storage
        storage.child("commands").child(f'{photo}').put(photo)
        os.remove(photo)  
        photo_url=storage.child("commands").child(f'{photo}').get_url('2')
        self.set_field(command_id,'photo',photo_url)
        return {'status':'success'}

        