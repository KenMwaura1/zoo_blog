from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, ValidationError
from wtforms.validators import Required, Email
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed

from ..models import User


class CreateBlog(FlaskForm):
    title = StringField('Title of blog', validators=[Required()])
    content = TextAreaField('Content of the blog', validators=[Required()])
    submit = SubmitField('Post')


class UpdateProfile(FlaskForm):
    username = StringField('Enter Your Username', validators=[Required()])
    email = StringField('Email Address', validators=[Required(), Email()])
    bio = TextAreaField('Write a brief bio about you.', validators=[Required()])
    profile_picture = FileField('profile picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    @staticmethod
    def validate_email(self, email):
        if (
                email.data != current_user.email
                and User.query.filter_by(email=email.data).first()
        ):
            raise ValidationError("The Email is already n use!")

    @staticmethod
    def validate_username(self, username):
        if (
                username.data != current_user.username
                and User.query.filter_by(username=username.data).first()
        ):
            raise ValidationError("The username is already in use")
