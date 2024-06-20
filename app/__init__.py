from flask import Flask
from app.config import SQLALCHEMY_DATABASE_URI, SECRET_KEY
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

app = Flask(__name__)

app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

csrf = CSRFProtect(app)

db = SQLAlchemy(app)


from app.routes.auth_routes import auth_bp
from app.routes.home_route import home_bp
from app.routes.password_routes import pw_bp


app.register_blueprint(auth_bp)
app.register_blueprint(home_bp)
app.register_blueprint(pw_bp)


from app.models import User
