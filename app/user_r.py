from flask import Blueprint, render_template, abort,request
import app.firebase as f
from os.path import join, dirname, realpath
from werkzeug.utils import secure_filename
import uuid
from PIL import Image
import os
from app.com_fb import Command_base
user_route = Blueprint('user_route', __name__)
UPLOADS_PATH = join(dirname(realpath(__file__)), 'img')
rpath=dirname(realpath(__file__))
@user_route.route('/upload_photo',methods=['POST'])
def upload_photo():
    form=dict(request.form)
    token=form.get('token',False)
    if request.files:
        image = request.files[list(request.files.keys())[0]]
        print(UPLOADS_PATH)
        token=list(request.files.keys())[0]
        path=join(UPLOADS_PATH,image.filename)
        image.save(UPLOADS_PATH)
        print(UPLOADS_PATH)
        img = Image.open(UPLOADS_PATH).resize((400,400)) # (x,y) pixels
        uid=uuid.uuid4().hex
        img.convert("RGB").save(f'{uid}.jpg')
        os.remove(UPLOADS_PATH)
        return f.upload_photo(token,f'{uid}.jpg')
    else:
        print('non args')
        return{'status':'error'},401
    

@user_route.route('/get_user',methods=['GET'])
def get_user():
    form=dict(request.args)
    token=form.get('token',False)
    if token:
        
        return f.get_data(token)
    else:
        print('non args')
        return{'status':'error'},401
    
@user_route.route('/change_field',methods=['POST'])
def change_field():
    form=dict(request.form)
    field=form.get('field',False)
    token=form.get('token',False)
    value=form.get('value',False)
    if token and value and field:
        
        return f.set_field(token,field,value)
    else:
        print('non args')
        return{'status':'error'},401
    
@user_route.route('/get_city',methods=['GET'])
def get_city(): 
    
    form=dict(request.args)
    city=form.get('city',False)
    if city:
        city=city.lower()
        return f.get_city(city)
    else:
        print('non args')
        return{'status':'error'},401
    
@user_route.route('/get_user/<id>',methods=['GET'])
def get_f_user(id):
    
    print(id)
    if id:
        return f.get_user(id)
    else:
        print('non args')
        return{'status':'error'},401

@user_route.route('/add_money',methods=['POST'])
def add_money():
    form=dict(request.form)
    token=form.get('token',False)
    value=form.get('value',False)
    if value and token:
        return f.set_money(token,int(value))
    else:
        print('non args')
        return{'status':'error'},401
@user_route.route('/minus_money',methods=['POST'])
def minus_money():
    form=dict(request.form)
    token=form.get('token',False)
    value=form.get('value',False)
    if token and value:
        return f.set_money(token,-int(value))
    else:
        print('non args')
        return{'status':'error'},401
@user_route.route('/get_commands',methods=['POST'])
def get_commands():
    form=dict(request.form)
    id=form.get('id')

    if id:
        r_data={}
        try:
            data=f.get_user(id)['commands']
        except:
            data={}
        
        r_data=Command_base().get_commands(list(data.keys()))
        return r_data
    else:
        print('non args')
        return{'status':'error'},401