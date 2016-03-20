import datetime
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    comment = db.relationship("Comment", back_populates="usr")

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


class Post(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50))
    # comments = db.relationship('Comment', backref='post',
    #                             lazy='dynamic')
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    comments = db.relationship('Comment', backref='post', order_by="desc(Comment.created_date)")

    def __repr__(self):
        return '<Post %r> <Comment %r>' % (self.title, self.comments)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(50))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    usr = db.relationship("User", back_populates="comment")
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    def __repr__(self):
        return '<Comment %r>' % (self.text)
