from dataclasses import dataclass
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app.commands import db, login


@login.user_loader
def load_user(user_id: int):
    return db.session.query(User).get(user_id)


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    bio = db.Column(db.String(255), default='My default Bio')
    profile_pic_path = db.Column(db.String(150), default='default.png')
    secure_password = db.Column(db.String(255), nullable=False)
    blog = db.relationship('Blog', backref='user', lazy='dynamic')
    comment = db.relationship('Comment', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError("You cannot read password attribute")

    @password.setter
    def password(self, password):
        self.secure_password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.secure_password, password)

    def __repr__(self):
        return f'User: {self.username}'
