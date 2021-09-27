from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Required, Email, EqualTo, Length
from wtforms import ValidationError
from ..models import User
from ..commands import db


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
    remember = BooleanField('Remember Me!')
    submit = SubmitField('Login')


class RegForm(FlaskForm):
    username: StringField = StringField('Enter Your Username', validators=[Required(), Length(min=4, max=20)])
    email = StringField('Email Address', validators=[Required(), Email()])
    password = PasswordField('Password',
                             validators=[Required(), EqualTo('password_confirm', message='Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords', validators=[Required()])
    submit = SubmitField('Sign Up')

    @staticmethod
    def validate_email(data_field):
        if db.session.query(User.email).filter_by(email=data_field.data).first():
            raise ValidationError(message="The Email is already in use!")

    @staticmethod
    def validate_username(data_field):
        if db.session.query(User.username).filter_by(username=data_field.data).first():
            raise ValidationError(message="The Username is already in use!")
