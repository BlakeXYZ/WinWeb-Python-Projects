from flask import render_template, flash, redirect, url_for
from my_app import app
from my_app.forms import LoginForm

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
    form = LoginForm()

    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    
    return render_template('login.html', title='Sign In', form=form)

