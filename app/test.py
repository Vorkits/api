import pyrebase
import uuid
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
auth = firebase.auth()
storage = firebase.storage()
print(storage.child("avatars").child('11b9f9b0de234f6695c5eb1b97341bbd.jpg').get_url('2'))