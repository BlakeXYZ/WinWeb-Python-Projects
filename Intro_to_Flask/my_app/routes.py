from datetime import datetime, timezone

from flask import request, render_template, flash, redirect, url_for
from flask_login import current_user, login_required, login_user, logout_user
from urllib.parse import urlsplit
import sqlalchemy as sa

from my_app import app
from my_app import db
from my_app.forms import LoginForm
from my_app.forms import RegistrationForm
from my_app.forms import EditProfileForm
from my_app.models import User


@app.before_request
def before_request():                           # For storing Last Seen model in DB inside user.html
    if current_user.is_authenticated:
        current_user.last_seen = datetime.now(timezone.utc)
        db.session.commit()

@app.route('/')
@app.route('/index')
@login_required
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
    
    return render_template('index.html', title=title, posts=posts)

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

        next_page = request.args.get('next')                # redirect user to original URL after logging in
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('index')

        return redirect(url_for('index'))
    
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():

    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    
    return render_template('register.html', title='Register', form=form)

@app.route('/user/<username>')
@login_required
def user(username):

    user = db.first_or_404(sa.select(User).where(User.username == username))
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]

    return render_template('user.html', user=user, posts=posts)


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('user', username=current_user.username))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile',
                           form=form)   

