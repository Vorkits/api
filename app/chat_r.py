from flask import Blueprint, render_template, abort,request
import app.firebase as f
from os.path import join, dirname, realpath
from werkzeug.utils import secure_filename
import uuid
from app.com_fb import Command_base
from app.Chat_base import Chat_base
from PIL import Image
import os

chat = Blueprint('chat', __name__)
UPLOADS_PATH = join(dirname(realpath(__file__)), 'img')
rpath=dirname(realpath(__file__))
@chat.route('/create',methods=['POST'])
def create():
    form=dict(request.form)
    id=form.get('id')
    users=form.get('users')
    name=form.get('name')
    if id and users:
        print(users)
        return Chat_base().create_chat(id,users,name)
    else:
        return {'status':'no args'},401
    
    
@chat.route('/get',methods=['GET'])
def get():
    form=dict(request.args)
    id=form.get('id')
    if id:
        return Chat_base().get_chat(id)
    else:
        return {'status':'no args'},401

@chat.route('/send',methods=['POST'])
def send():
    form=dict(request.form)
    id=form.get('id')
    message=form.get('message')
    owner=form.get('owner')
    if id and owner and message:
        return Chat_base().send_message(id,message,owner)
    else:
        return {'status':'no args'},401
    
@chat.route('/add_chat',methods=['POST'])
def add_chat():
    form=dict(request.form)
    id=form.get('id')
    user=form.get('user')
    if id and user:
        return Chat_base().add_chat(id,user)
    else:
        return {'status':'no args'},401