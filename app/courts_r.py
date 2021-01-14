from flask import Blueprint, render_template, abort,request
import app.firebase as f
from os.path import join, dirname, realpath
from werkzeug.utils import secure_filename
import uuid
from PIL import Image
import os

court = Blueprint('court_route', __name__)
UPLOADS_PATH = join(dirname(realpath(__file__)), 'img')
rpath=dirname(realpath(__file__))
@court.route('/create',methods=['POST'])
def create():
    form=dict(request.form)
    token=form.get('token',False)
    city=form.get('city',False)
    phone=form.get('phone',False)
    addres=form.get('addres',False)
    if  token and city and addres and phone and request.files.get('c_photo',False).filename != '':
        city=city.lower()
        image = request.files['c_photo']
        image.save(UPLOADS_PATH)
        img = Image.open(UPLOADS_PATH) # (x,y) pixels
        uid=uuid.uuid4().hex
        img.convert("RGB").save(f'{uid}.jpg')
        os.remove(UPLOADS_PATH)
        return f.c_create(token=token,photo=f'{uid}.jpg',city=city,addres=addres,phone=phone)
    else:
        print('non args')
        return{'status':'error','desc':'non args'},401
    
@court.route('/get',methods=['GET'])
def get():
    form=dict(request.args)
    coart_id=form.get('coart_id',False)
    if coart_id:
        return f.get_coart(coart_id)
    else:
        print('non args')
        return{'status':'error','desc':'non args'},401
    

@court.route('/set',methods=['POST'])
def set():
    
    form=dict(request.form)
    field=form.get('field')
    token=form.get('token')
    value=form.get('value')
    coart_id=form.get('coart_id')
    if coart_id and value and token and field :
        return f.set_field_coart(token,coart_id,field,value)
    else:
        print('non args')
        return{'status':'error','desc':'non args'},401
    