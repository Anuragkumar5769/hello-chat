from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db=SQLAlchemy()

# undermixin flask-login le liye use hua
class User(UserMixin,db.Model):

    __tablename__="users"
    id=db.Column(db.Integer, primary_key=True )
    username= db.Column(db.String(20), unique=True, nullable=False)
    password= db.Column(db.String(),nullable=False)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

class message_history(db.Model):

    __tablename__="messages"
    id=id=db.Column(db.Integer, primary_key=True )
    sender=db.Column(db.String(),nullable=False)
    message=db.Column(db.String(),nullable=False)
    room=db.Column(db.String(),nullable=False)
    time=db.Column(db.Time)

    def __init__(self, **kwargs):
        super(message_history, self).__init__(**kwargs)

    