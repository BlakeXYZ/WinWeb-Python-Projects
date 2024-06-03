from flask import render_template
from my_app import app

@app.route('/')
@app.route('/index')
def index():
    title = 'Home'
    user = {'username': 'BK'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portl!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]    
    
    return render_template('index.html', title=title, user=user, posts=posts)