from flask import Blueprint, render_template, abort,request
import app.firebase as f
from os.path import join, dirname, realpath
from werkzeug.utils import secure_filename
import uuid
from app.com_fb import Command_base
from app.Chat_base import Chat_base
from PIL import Image
import os
from app.tour_base import Tournament_base
tournament = Blueprint('tournament', __name__)
UPLOADS_PATH = join(dirname(realpath(__file__)), 'img')
rpath=dirname(realpath(__file__))
@tournament.route('/create',methods=['POST'])
def create():
    form=dict(request.form)
    # date,count,owner,t,place
    date=form.get('date')
    count=form.get('count')
    owner=form.get('owner')
    t=form.get('type')
    place=form.get('place')
    name=form.get('name')
    price=form.get('price')
    print(place,date,t,owner,count)
    if date and count and owner and t and place and name and price:
        t=int(t)
        print('s')
        return Tournament_base().create(date,count,owner,t,place,name,price)
    else:
        return {'status':'no args'},401
    
@tournament.route('/join',methods=['POST'])
def join():
    form=dict(request.form)
    # self,tournament_id,t,command_id,place=0,group_id=0,bracket_id=0
    tournament_id=form.get('tournament_id')
    command_id=form.get('command_id')
    t=form.get('type')  
    
    if tournament_id and command_id and t :
        t=int(t)
        return Tournament_base().join_command(tournament_id,t,command_id)
    else:
        return {'status':'no args'},401
    
    
@tournament.route('/get',methods=['POST'])
def get():
    form=dict(request.form)
    # self,tournament_id,t,command_id,place=0,group_id=0,bracket_id=0
    tournament_id=form.get('tournament_id')
    if tournament_id :
        return Tournament_base().get_t(tournament_id)
    else:
        return {'status':'no args'},401

@tournament.route('/get_all',methods=['POST'])
def get_all():
    form=dict(request.form)
    return Tournament_base().get_all()

    
@tournament.route('/finish',methods=['POST'])
def finish():
    form=dict(request.form)
    # self,tournament_id,t,command_id,place=0,group_id=0,bracket_id=0
    tournament_id=form.get('tournament_id')
    winner=form.get('winner')
    if tournament_id :
        return Tournament_base().finish_t(tournament_id,winner)
    else:
        return {'status':'no args'},401