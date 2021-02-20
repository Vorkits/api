from flask import Blueprint, render_template, abort,request
import app.firebase as f
from os.path import join, dirname, realpath
from werkzeug.utils import secure_filename
import uuid
from PIL import Image
import os
import json
from app.firebase_class import Games_base
from app.com_fb import Command_base
game_r = Blueprint('game_route', __name__)
UPLOADS_PATH = join(dirname(realpath(__file__)), 'img')
rpath=dirname(realpath(__file__))

@game_r.route('/create',methods=['POST'])
def create():
        form=dict(request.form)
        player1=form.get('player1_id')
        player2=form.get('player2_id')
        time=form.get('time')
        t=form.get('type')
        place=form.get('place')
        data=()
        if player1 and player2 and time and t :
            t=int(t)
            
            data=Games_base().create_match(player1,player2,time,coart=False,t=t,hour=1,place=place)
            return {'status':'success','match_id':data[0],'data':data[1]},200
        else:
            print('non args')
            return{'status':'error'},401
    
    
@game_r.route('/edit',methods=['POST'])
def edit():
    try:
        form=dict(request.form)
        match_id=form.get('match_id')
        field=form.get('field')
        value=form.get('value')
        if match_id and value and field:
        
            data=Games_base().change_field(field,value,match_id)
            return {'status':'success','desc':data},200
        else:
            print('non args')
            return{'status':'error'},401
    except Exception as e:
        print('non args')
        return{'status':str(e)},401
    
@game_r.route('/get',methods=['GET'])
def get():
    print('gbnbns')
    try:
        data=Games_base().get_matches()
        return json.dumps({'status':'success','data':data}),200
    except Exception as e:
        print('non args')
        print(e)
        return{'status':str(e)},400
@game_r.route('/get_match',methods=['POST'])
def get_match():
    try:
        form=dict(request.form)
        match_id=form.get('match_id')
    
        if match_id :
        
            data=Games_base().get_match(match_id)
            
            return {'status':'success','data':data},200
        else:
            print('non args')
            return{'status':'error'},401
    except Exception as e:
        print('non args')
        return{'status':str(e)},401
@game_r.route('/get_users_match',methods=['POST'])
def get_users_match():
    try:
        form=dict(request.form)
        id=form.get('id')
    
        if id:
        
            data=Games_base().get_users_match(id)
            
            return {'status':'success','data':data},200
        else:
            print('non args')
            return{'status':'error'},401
    except Exception as e:
        print('non args')
        return{'status':str(e)},401
@game_r.route('/get_command_match',methods=['POST'])
def get_command_match():
    try:
        form=dict(request.form)
        id=form.get('id')
    
        if id:
        
            data=Command_base().get_command(id)['data']
            
            
            return {'status':'success','data':data['matches']},200
        else:
            print('non args')
            return{'status':'error'},401
    except Exception as e:
        print('non args')
        return{'status':str(e)},401
    
@game_r.route('/finish',methods=['POST'])
def finish():
    try:
        print('finish')
        # score1,score2,match_id
        form=dict(request.form)
        match_id=form.get('match_id')
        score1=form.get('score1')
        score2=form.get('score2')
        if match_id and score1 and score2 :
        
            data=Games_base().finish_match(score1,score2,match_id)
            return json.dumps({'status':'success','data':data}),200
        else:
            print('non args')
            return{'status':'error'},401
    except Exception as e:
        print('non args')
        return{'status':'error','error':str(e)},401
