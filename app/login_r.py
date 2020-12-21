from flask import Blueprint, render_template, abort,request
import app.firebase as f

login_route = Blueprint('login_route', __name__)

@login_route.route('/create_user',methods=['POST'])
def create_user():
    form=dict(request.form)
    if form.get('email',False) and form.get('password',False):
        user=f.create_user(password=form.get('password'),email=form.get('email'))
        return user
    else:
        return{'status':'error'},401