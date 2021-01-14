from flask import Flask,request
from .login_r import login_route
from .user_r import user_route
from .courts_r import court
from .games_r import game_r
app = Flask(__name__)
app.register_blueprint(login_route, url_prefix='/api/auth')
app.register_blueprint(user_route, url_prefix='/api/user')
app.register_blueprint(court, url_prefix='/api/court')
app.register_blueprint(game_r, url_prefix='/api/games')
if __name__ == '__main__':
    app.run()