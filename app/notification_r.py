from flask import Blueprint, render_template, abort,request
import app.firebase as f
from os.path import join, dirname, realpath
from werkzeug.utils import secure_filename
import uuid
from app.com_fb import Command_base
from PIL import Image
import os
from app.notes_base import Notes_base
notes = Blueprint('notes', __name__)
UPLOADS_PATH = join(dirname(realpath(__file__)), 'img')
rpath=dirname(realpath(__file__))
@notes.route('/send_message',methods=['POST'])
def send_message():
    form=dict(request.form)
    f=form.get('from')
    t=form.get('to')
    text=form.get('text')
    if f and t and text:
        return Notes_base().send_message(f,t,text)
    else:
            print('non args')
            return{'status':'error'},401
    
@notes.route('/check_messages',methods=['POST'])
def check_messages():
    form=dict(request.form)
    id=form.get('id')

    if id:
        return Notes_base().check_messages(id)
    else:
            print('non args')
            return{'status':'error'},401
    
@notes.route('/confirm_game',methods=['POST'])
def confirm_game():
    # Поставить статус, удалить в уведомлениях
    form=dict(request.form)
    id=form.get('id')
    game_id=form.get('game_id')
    confirm=form.get('confirm')
    if not confirm:
        confirm=True
    
    if game_id and id:
        return Notes_base().confirm_game(game_id,id,confirm=int(confirm))
    else:
            print('non args')
            return{'status':'error'},401
    
@notes.route('/confirm_command',methods=['POST'])
def confirm_command():
    # Поставить статус, удалить в уведомлениях
    form=dict(request.form)
    id=form.get('id')
    command_id=form.get('command_id')
    confirm=form.get('confirm')
    if not confirm:
        confirm=True
    if command_id and id:
        return Notes_base().confirm_command(command_id,id,confirm=int(confirm))
    else:
            print('non args')
            return{'status':'error'},401
        
@notes.route('/get',methods=['POST'])
def get():
    # Поставить статус, удалить в уведомлениях
    form=dict(request.form)
    id=form.get('id')
    
    if id:
        return Notes_base().get(id)
    else:
            print('non args')
            return{'status':'error'},401
    