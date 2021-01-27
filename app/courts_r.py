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
    city=form.get('city',False)
    phone=form.get('phone',False)
    addres=form.get('addres',False)
    name=form.get('name',False)
    cost=form.get('cost',False)
    if   city and addres and phone and name and cost:
        city=city.lower()
        return f.c_create(photo='',city=city,addres=addres,phone=phone,name=name,cost=cost)
    else:
        print(addres,phone,city,name,cost)
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
    value=form.get('value')
    coart_id=form.get('coart_id')
    if coart_id and value  and field :
        return f.set_field_coart(coart_id,field,value)
    else:
        print('non args')
        return{'status':'error','desc':'non args'},401
@court.route('/upload_photo',methods=['POST'])
def upload_photo():
    form=dict(request.form)

    if request.files :
        image = request.files[list(request.files.keys())[0]]
        print(UPLOADS_PATH)
        token=list(request.files.keys())[0]
        image.save(UPLOADS_PATH)
        img = Image.open(UPLOADS_PATH) # (x,y) pixels
        uid=uuid.uuid4().hex
        img.convert("RGB").save(f'{uid}.jpg')
        os.remove(UPLOADS_PATH)
        return f.coart_photo(token,f'{uid}.jpg')
    else:
        print('non args')
        return{'status':'error','desc':'non args'},401

@court.route('/get_all',methods=['GET'])
def get_all():
    form=dict(request.form)

    try :
        return f.get_coarts()
    except:
        print('non args')
        return{'status':'error','desc':'non args'},401
    