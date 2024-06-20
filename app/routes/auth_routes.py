from flask import Blueprint, render_template, redirect, url_for, flash
from app.forms import RegistrationForm, LoginForm
from app.models import User
from app import db



auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/signin", methods=['GET', 'POST'])
def sign_in():
    form = LoginForm()
    if form.validate_on_submit():
        
        user = User.query.filter_by(email=form.email.data, password=form.password.data).first()
        
        if user is None:
            return redirect(url_for('auth.sign_in'))
        return redirect(url_for('home.home_page'))
    return render_template('sign_in.html', form=form)

@auth_bp.route('/signup', methods=['GET', 'POST'])
def sign_up():
    form = RegistrationForm()
    if form.validate_on_submit():
        
        name = form.name.data
        surname = form.surname.data
        login = form.login.data
        password = form.password.data
        email = form.email.data
        
        new_user = User(
            name=name,
            surname=surname,
            login=login,
            password=password,
            email=email
        )
        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('auth.sign_in'))
        except Exception as e:
            
            db.session.rollback()
            print(f"Error occurred: {str(e)}")
            
            return render_template('sign_up.html', form=form, error=str(e))
       

    return render_template('sign_up.html', form=form)