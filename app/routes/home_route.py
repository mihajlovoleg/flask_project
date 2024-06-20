from flask import render_template, Blueprint

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home_page():
    return render_template('home.html')