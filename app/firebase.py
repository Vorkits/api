import pyrebase
import uuid
import os
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

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
storage = firebase.storage()

db = firebase.database()
def create_user(password,email,name,city):
    try:
        auth = firebase.auth()
        db = firebase.database()
        user=auth.create_user_with_email_and_password(email, password)
        auth.send_email_verification(user['idToken'])
        token=uuid.uuid4().hex
        email=email.replace('.','&&')
        photo='standart.jpg'
        photo=storage.child(f"avatars/{photo}").get_url(user['idToken'])
        db.child("users").child(email).set({'name':name,'city':city,'token':token,'score':0,'level':0,'photo':photo})
        db.child("tokens").child(token).set({'user':email})
        return {'status':'success','token':token},200
    except Exception as e:
        print(e)
        return {'status':'error'},401

def sign_in_user(password,email):
    try:
        auth = firebase.auth()
        db = firebase.database()
        user=auth.sign_in_with_email_and_password(email, password)
        email=email.replace('.','&&')
        data=dict(db.child("users").child(email).get().val())
        if data.get('token',False):
            return {'status':'success','token':data['token']},200
        else:
            data['token']=uuid.uuid4().hex
            db.child("users").child(email).set(data)
            db.child("tokens").child(data['token']).set({'user':email})
            return {'status':'success','token':data['token']},200
    except:
        return {'status':'error'},401
    
def send_reset(email):
    try: 
        auth = firebase.auth()
        db = firebase.database()
        user=auth.send_password_reset_email(email)
        email=email.replace('.','&&')
        data=dict(db.child("users").child(email).get().val())
        db.child("tokens").child(data['token']).remove()
        data.pop('token')
        db.child("users").child(email).set(data)
        return {'status':'success'},200
    except:
        return {'status':'error'},401

def logout(token):
    try: 
        auth = firebase.auth()
        db = firebase.database()
       
        d=dict(db.child("tokens").child(token).get().val())
        email=d['user']
        db.child("tokens").child(token).remove()
        data=db.child("users").child(email).get().val()
        data.pop('token')
        db.child("users").child(email).set(data)
        return {'status':'success'},200
    except Exception as e:
        print(e)
        return {'status':'error'},401
def checktoken(token):
    try: 
        auth = firebase.auth()
        db = firebase.database()
       
        d=dict(db.child("tokens").child(token).get().val())
        return {'status':'success'},200
    except Exception as e:
        print(e)
        return {'status':'error'},401

def get_email(token):
    d=dict(db.child("tokens").child(token).get().val())
    email=d['user']
    return email

def set_field(token,field,value):
    try:
        data=get_data(token)
        data[field]=value
        email=get_email(token)
        db.child("users").child(email).set(data)
        return {'status':'success'},200
    except Exception as e:
        print(e)
        return {'status':'error'},401
        
def get_data(token):
    try:
        email=get_email(token)
        data=db.child("users").child(email).get().val()
        return data
    except Exception as e:
        print(e)
        return {'status':'error'},401
        
def upload_photo(token,photo):
    try:
        email=get_email(token)
        data=db.child("users").child(email).get().val()
        
        storage.child("avatars").child(f'{photo}').put(photo)
        os.remove(photo)
        photo_url=storage.child("avatars").child(f'{photo}').get_url('2')
        data['photo']=photo_url
        db.child("users").child(email).set(data)
        return {'status':'success'},200
    except Exception as e:
        print(e)
        return {'status':'error'},401
        



# def check_token(token)
#     try:
#         auth = firebase.auth()
#         user=auth.sign_in_with_email_and_password(email, password)
#         auth.send_email_verification(user['idToken'])
#         return user,200
#     else:
#         return {'status':'error'},401


