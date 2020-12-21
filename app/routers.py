from flask import Flask,request
from .login_r import login_route
app = Flask(__name__)
app.register_blueprint(login_route, url_prefix='/api/auth')

if __name__ == '__main__':
    app.run()