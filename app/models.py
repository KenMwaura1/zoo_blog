from dataclasses import dataclass
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app.commands import db, login


@login.user_loader
def load_user(user_id: int):
    return db.session.query(User).get(user_id)


@dataclass
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    bio = db.Column(db.String(255), default='My default Bio')
    profile_pic_path = db.Column(db.String(150), default='default.png')
    secure_password = db.Column(db.String(255), nullable=False)
    blog = db.relationship('Blog', backref='user', lazy='dynamic')
    comment = db.relationship('UserComment', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError("You cannot read password attribute")

    @password.setter
    def password(self, password):
        self.secure_password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.secure_password, password)

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'User: {self.username}'


@dataclass
class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    comment = db.relationship('UserComment', backref='blog', lazy='dynamic')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def get_blog(id):
        return db.session.query(Blog).filter(Blog.id == id).first()

    @staticmethod
    def get_all_blogs():
        return db.session.query(Blog).order_by(db.desc(Blog.date_posted))

    def __repr__(self):
        return f'Blog: {self.title}'


@dataclass()
class UserComment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    comment = db.Column(db.String)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow())
    blog_id = db.Column(db.Integer, db.ForeignKey("blogs.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.remove(self)
        db.session.commit()

    @staticmethod
    def get_comment(id):
        return db.session.query(UserComment).filter(id=id)

    @staticmethod
    def get_all_comments():
        return db.session.query(UserComment).order_by(db.desc(UserComment.date_posted))

    def __repr__(self):
        return f'Comment: {self.comment}'


class Subscriber(db.Model):
    __tablename__ = 'subscribers'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, index=True)

    def save_subscriber(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Subscriber: {self.email}'
