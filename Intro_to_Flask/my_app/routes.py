from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user
import sqlalchemy as sa

from my_app import app
from my_app import db
from my_app.forms import LoginForm
from my_app.models import User


@app.route('/')
@app.route('/index')
def index():
    title = 'Index'
    user = {'username': 'BK'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Tejas!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Bob'}
        }
    ]    
    
    return render_template('index.html', title=title, user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:       # checks if user is already logged in
        return redirect(url_for('index'))
    
    form = LoginForm()

    if form.validate_on_submit():
        user =  db.session.scalar(sa.select(User).where(User.username == form.username.data))
        
        if user is None or not user.check_password(form.password.data): # if user is not valid...
            flash('Invalid Usernamer or Password!')
            return redirect(url_for('index'))
        
        login_user(user, remember=form.remember_me.data)    # if user is valid, login
        return redirect(url_for('index'))
    
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

