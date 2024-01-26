from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

db = SQLAlchemy()




class User(db.Model, SerializerMixin):
     
     id = db.Column(db.Integer, primary_key=True)
     username = db.Column(db.String(255), nullable=False, unique=True)
     password = db.Column(db.String(255), nullable=False)
     email = db.Column(db.String(255), nullable=False, unique=True)
     image = db.Column(db.String(255))
     reviews = db.relationship('Review',backref='review',lazy=True)
     events_followed = db.relationship('Following',backref='events',lazy=True)
     events_attended = db.relationship('Attended', backref='attends',lazy=True) 
     created_events = db.relationship('Event', backref='creator', lazy=True) 
     created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
     updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

     @validates('email')
     def validate_email(self, key, address):
         if "@" not in address:
             raise ValueError("Failed simple email validation")
         return address
     
     @validates('password')
     def validate_password(self, key, password):
        if not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password):
            raise ValueError("Password must contain a mixture of letters and numbers.")
        return password
     
class Following(db.Model, SerializerMixin):
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)



class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(255))  
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    location = db.Column(db.String(255), nullable=False)
    event_reviews = db.relationship('Review',backref='e_reviews',lazy=True)# one review or many
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)# for creator
    users_following = db.relationship('Following',backref='users',lazy=True)#following and followers
    users_attended = db.relationship('Attended',backref='attendants',lazy = True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())


    @validates('image')
    def validate_image_url(self, key, image_url):
        if not image_url.startswith(('http://', 'https://')):
            raise ValueError("Invalid image URL format. It should start with 'http' or 'https'.")
        return image_url

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    comment = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())


class Attended(db.Model): # many to many
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))