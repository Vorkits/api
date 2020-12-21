import pyrebase
config = {
    "apiKey": "AIzaSyDYsYC0LnriZt1JxLKpFKV0HIfw2slT1ac",
    "authDomain": "orac-9d788.firebaseapp.com",
    "projectId": "orac-9d788",
    "storageBucket": "orac-9d788.appspot.com",
    "messagingSenderId": "364935870344",
    "appId": "1:364935870344:web:eacf38c9a8f1f53d8eac3d",
   "measurementId": "G-Y9LZYCKM4Y",
   "databaseURL":'https://orac-9d788-default-rtdb.firebaseio.com/'
  }

firebase = pyrebase.initialize_app(config)
def create_user(password,email):
    auth = firebase.auth()
    user=auth.create_user_with_email_and_password(email, password)
    auth.send_email_verification(user['idToken'])
    return user
