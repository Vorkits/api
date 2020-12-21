from flask import Flask,request
import app.firebase as f
app = Flask(__name__)
 
@app.route('/api/create_user',methods=['POST'])
def create_user():
    form=dict(request.form)
    if form.get('email',False) and form.get('password',False):
        user=f.create_user(password=form.get('password'),email=form.get('email'))
        return user
if __name__ == '__main__':
    app.run()