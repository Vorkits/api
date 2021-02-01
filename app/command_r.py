from flask import Blueprint, render_template, abort,request
import app.firebase as f
from os.path import join, dirname, realpath
from werkzeug.utils import secure_filename
import uuid
from app.com_fb import Command_base
from PIL import Image
import os

commands = Blueprint('commands_route', __name__)
UPLOADS_PATH = join(dirname(realpath(__file__)), 'img')
rpath=dirname(realpath(__file__))
@commands.route('/create',methods=['POST'])
def create():
    form=dict(request.form)
    player1=form.get('player1')
    player2=form.get('player2')
    if player1 and player2:
        return Command_base().create_command(player1,player2)
    else:
        return {'status':'no args'},401
@commands.route('/get',methods=['GET'])
def get():
    form=dict(request.args)
    id=form.get('id')

    if id:
        return Command_base().get_command(id)
    else:
        return {'status':'no args'},401
@commands.route('/get_city',methods=['GET'])
def get_city():
    form=dict(request.args)
    city=form.get('city')

    if city:
        return Command_base().get_by_city(city)
    else:
        return {'status':'no args'},401
@commands.route('/set_field',methods=['POST'])
def set_field():
    form=dict(request.args)
    id=form.get('id')
    field=form.get('field')
    value=form.get('value')
    if value and field and id:
        return Command_base().set_field(id,field,value)
    else:
        return {'status':'no args'},401