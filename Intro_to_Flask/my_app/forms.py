'''
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms

forms.py usage:

Login Form setup using Flask Extension: wtforms

using inside routes.py:
from my_app.forms import LoginForm


'''

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
import sqlalchemy as sa
from my_app import db
from my_app.models import User

class LoginForm(FlaskForm):
    username =      StringField('Username', validators=[DataRequired()])
    password =      PasswordField('Password', validators=[DataRequired()])
    remember_me =   BooleanField('Remember Me')
    submit =        SubmitField('Click me to sign in!')

class RegistrationForm(FlaskForm):
    username =      StringField('Username', validators=[DataRequired()])
    email =         StringField('Email', validators=[DataRequired(), Email()])
    password =      PasswordField('Password', validators=[DataRequired()])
    password2 =     PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit =        SubmitField('Register!')

    def validate_username(self, username):              # When you add any methods that match the pattern validate_<field_name>, WTForms takes those as custom validators and invokes them in addition to the stock validators
        user = db.session.scalar(sa.select(User).where(
            User.username == username.data))
        if user is not None:
            raise ValidationError(f"Username '{username.data}' is already taken! :(")
        
    def validate_email(self, email):
        user = db.session.scalar(sa.select(User).where(
            User.email == email.data))
        if user is not None:
            raise ValidationError(f"Email '{email.data}' is already taken! :(")
        
class EditProfileForm(FlaskForm):
    username =      StringField('Username', validators=[DataRequired()])
    about_me =      TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit =        SubmitField('Submit')

        

