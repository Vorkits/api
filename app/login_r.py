from flask import Blueprint, render_template, abort,request
import app.firebase as f

login_route = Blueprint('login_r', __name__)

@login_route.route('/create_user',methods=['POST'])
def create_user():
    form=dict(request.form)
    name=form.get('name',False)
    email=form.get('email',False)
    city=form.get('city',False)
    password=form.get('password',False)
    if form and name and city and password:
        user=f.create_user(password=form.get('password'),email=form.get('email'),name=name,city=city)
        return user
    else:
        print('non args')
        return{'status':'error'},401
    
@login_route.route('/logout',methods=['POST'])
def logout():
    form=dict(request.form)
    token=form.get('token',False)
    if token:
        user=f.logout(token)
        return user
    else:
        print('non args')
        return{'status':'error'},401

@login_route.route('/sign_in',methods=['POST'])
def sign_in():
    form=dict(request.form)
    email=form.get('email',False)
    password=form.get('password',False)
    if email and password:
        user=f.sign_in_user(password,email)
        return user
    else:
        print('non args')
        return{'status':'error'},401
    
@login_route.route('/reset',methods=['POST'])
def reset():
    form=dict(request.form)
    email=form.get('email',False)
    if email :
        user=f.send_reset(email)
        return user
    else:
        print('non args')
        return{'status':'error'},401
    
@login_route.route('/check_token',methods=['POST'])
def check_token():
    form=dict(request.form)
    token=form.get('token',False)
    if token :
        user=f.checktoken(token)
        return user
    else:
        print('non args')
        return{'status':'error'},401