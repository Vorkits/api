from flask import Flask,request
from .login_r import login_route
from .user_r import user_route
app = Flask(__name__)
app.register_blueprint(login_route, url_prefix='/api/auth')
app.register_blueprint(user_route, url_prefix='/api/user')
if __name__ == '__main__':
    app.run()