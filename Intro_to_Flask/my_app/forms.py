'''
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms

forms.py usage:

Login Form setup using Flask Extension: wtforms

using inside routes.py:
from my_app.forms import LoginForm


'''

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Click me to sign in!')