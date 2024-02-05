from flask import Flask,session,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_restful import Api, Resource
from flask_migrate import Migrate
from models import User, Event, Review, Attended, Following,db,bcrypt
##
from flask import request,jsonify,make_response
from flask_restful import Resource, reqparse
from serializer import  serialize_user, serialize_event, serialize_review, serialize_attended, serialize_following
##
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)
api = Api(app)



app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'b$A9pL!q2o#Z8s*'

app.json.compact = False

CORS(app)
migrate = Migrate(app, db)
db.init_app(app)
bcrypt.init_app(app)

# @app.before_request
# def check_if_logged_in():
#     allowed_endpoints = ['event_list', 'login', 'signup', 'home','followings']

#     if 'user_id' not in session and request.endpoint not in allowed_endpoints:
#         return {'error': 'Unauthorized'}, 401


class Home(Resource):
    def get(self):
        response_dict = {
            'index':'Welcome to social vibes RESTful API'
        }
        response = make_response(jsonify(response_dict),200)

        return response

api.add_resource(Home,'/')
   

class Login(Resource):
    def post(self):
        email = request.get_json()['email']

        user = User.query.filter(User.email == email).first()

        password = request.get_json()['password']

        if user and user.authenticate(password):
            session['user_id'] = user.id
            return user.to_dict(), 200
        else:
            return {'error':'Invalid username or password'}
        
api.add_resource(Login,'/login')

class Logout(Resource):
    def delete(self):
        session['user_id'] = None
        return jsonify({'message':'204: No content'})

api.add_resource(Logout,'/logout')

class CheckSession(Resource):
    def get(self):
        user = User.query.filter(User.id == session.get('user_id')).first()
        if user:
            return jsonify(user.to_dict())
        else:
            return jsonify({'message':'401: Not authorized'}), 401
        
api.add_resource(CheckSession,'/check_session')

class Users(Resource):
    def get(self):
        all_users = User.query.all()
        if all_users:
            response_dict = [serialize_user(x) for x in all_users]
            response = make_response(jsonify(response_dict), 200)
            return response
        else:
            response_dict = {
                'error':'Resources not found'
            }
            response = make_response(jsonify(response_dict),404)
            return response
        
    def post(self):
        data = request.get_json()
        if data:
            new_user = User(
                username=data['username'],
                _password_hash=data['password'],
                email=data['email'],
                image=data['image'],
            )
            new_user.set_password(data['password'])
            
            db.session.add(new_user)
            db.session.commit()

            response_dict = new_user.to_dict()
            response = make_response(jsonify(response_dict),200)
            return response
        else:
            response_dict = {
                'error':['validation errors']
            }
            response = make_response(jsonify(response_dict),400)
            return response
        
api.add_resource(Users,'/users')

class UserById(Resource):
    def get(self,id):
        user = User.query.filter_by(id=id).first()
        if user:
            response_dict = serialize_user(user)
            response = make_response(jsonify(response_dict),200)
            return response
        else:
            response_dict = {
                'error':'user does not exist'
            }
            response = make_response(jsonify(response_dict),404)
            return response

    def patch(self,id):
         user = User.query.filter_by(id=id).first()
         if user:
            data = request.get_json()
            for attr in data:
                setattr(user,attr,data[attr])
                 
            db.session.commit()

            response_dict = serialize_user(user)
            response = make_response(jsonify(response_dict),200)
            return response
         else:
            response_dict = {
                'error':'failed to update'
            }
            response = make_response(jsonify(response_dict),404)
            return response
         
    def delete(self,id):
        user = User.query.filter_by(id=id).first()
        if user:
            db.session.delete(user)
            db.session.commit()

            response_dict = {
                'message':'user successfully deleted'
            }
            response = make_response(jsonify(response_dict),200)
            return response
        
api.add_resource(UserById,'/user/<int:id>')

class UserReviews(Resource):
    def get(self, user_id):
        reviews = Review.query.filter_by(user_id=user_id).all()

        if reviews:
            response_dict = [serialize_review(review) for review in reviews]
            response = make_response(jsonify(response_dict), 200)
            return response
        else:
            response_dict = {
                'error': 'No reviews found for the specified user'
            }
            response = make_response(jsonify(response_dict), 404)
            return response

api.add_resource(UserReviews, '/user/<int:user_id>/reviews')

class UserEventsFollowed(Resource):
    def get(self, user_id):
        user = User.query.get(user_id)

        if user:
            events_followed = [[serialize_following(follow) for follow in user.events_followed]]
            response = make_response(jsonify(events_followed), 200)
            return response
        else:
            response_dict = {
                'error': 'User not found'
            }
            response = make_response(jsonify(response_dict), 404)
            return response

api.add_resource(UserEventsFollowed, '/user/<int:user_id>/events/followed')


class Events(Resource):
    def get(self):
        all_events = Event.query.all()
        if all_events:
            response_dict = [serialize_event(x) for x in all_events]
            response = make_response(jsonify(response_dict), 200)
            return response
        else:
            response_dict = {
                'error': 'Resources not found'
            }
            response = make_response(jsonify(response_dict), 404)
            return response

    def post(self):
        data = request.get_json()
        if data:
            new_event = Event(
                title=data['title'],
                image=data['image'],
                description=data['description'],
                date=data['date'],
                time=data['time'],
                location=data['location'],
                user_id=data['user_id'],  # creator's id
            )

            db.session.add(new_event)
            db.session.commit()

            response_dict = serialize_event(new_event)
            response = make_response(jsonify(response_dict), 200)
            return response
        else:
            response_dict = {
                'error': ['validation errors']
            }
            response = make_response(jsonify(response_dict), 400)
            return response

api.add_resource(Events, '/events',endpoint='events_list')

class EventById(Resource):
    def get(self, id):
        event = Event.query.filter_by(id=id).first()
        if event:
            response_dict = serialize_event(event)
            response = make_response(jsonify(response_dict), 200)
            return response
        else:
            response_dict = {
                'error': 'event does not exist'
            }
            response = make_response(jsonify(response_dict), 404)
            return response

    def patch(self, id):
        event = Event.query.filter_by(id=id).first()
        if event:
            data = request.get_json()
            for attr in data:
                setattr(event, attr, data[attr])

            db.session.commit()

            response_dict = serialize_event(event)
            response = make_response(jsonify(response_dict), 200)
            return response
        else:
            response_dict = {
                'error': 'failed to update'
            }
            response = make_response(jsonify(response_dict), 404)
            return response

    def delete(self, id):
        event = Event.query.filter_by(id=id).first()
        if event:
            db.session.delete(event)
            db.session.commit()

            response_dict = {
                'message': 'event successfully deleted'
            }
            response = make_response(jsonify(response_dict), 200)
            return response

api.add_resource(EventById, '/event/<int:id>', endpoint='event')

# Reviews routes
class Reviews(Resource):
    def get(self):
        all_reviews = Review.query.all()
        if all_reviews:
            response_dict = [serialize_review(x) for x in all_reviews]
            response = make_response(jsonify(response_dict), 200)
            return response
        else:
            response_dict = {
                'error': 'Resources not found'
            }
            response = make_response(jsonify(response_dict), 404)
            return response

    def post(self):
        data = request.get_json()
        if data:
            new_review = Review(
                user_id=data['user_id'],
                event_id=data['event_id'],
                rating=data['rating'],
                comment=data['comment'],
            )

            db.session.add(new_review)
            db.session.commit()

            response_dict = serialize_review(new_review)
            response = make_response(jsonify(response_dict), 200)
            return response
        else:
            response_dict = {
                'error': ['validation errors']
            }
            response = make_response(jsonify(response_dict), 400)
            return response

api.add_resource(Reviews, '/reviews')

class ReviewById(Resource):
    def get(self, id):
        review = Review.query.filter_by(id=id).first()
        if review:
            response_dict = serialize_review(review)
            response = make_response(jsonify(response_dict), 200)
            return response
        else:
            response_dict = {
                'error': 'review does not exist'
            }
            response = make_response(jsonify(response_dict), 404)
            return response

    def patch(self, id):
        review = Review.query.filter_by(id=id).first()
        if review:
            data = request.get_json()
            for attr in data:
                setattr(review, attr, data[attr])

            db.session.commit()

            response_dict = serialize_review(review)
            response = make_response(jsonify(response_dict), 200)
            return response
        else:
            response_dict = {
                'error': 'failed to update'
            }
            response = make_response(jsonify(response_dict), 404)
            return response

    def delete(self, id):
        review = Review.query.filter_by(id=id).first()
        if review:
            db.session.delete(review)
            db.session.commit()

            response_dict = {
                'message': 'review successfully deleted'
            }
            response = make_response(jsonify(response_dict), 200)
            return response

api.add_resource(ReviewById, '/review/<int:id>')

class ReviewsForEvent(Resource):
    def get(self, event_id):
        reviews = Review.query.filter_by(event_id=event_id).all()

        if reviews:
            response_dict = [serialize_review(review) for review in reviews]
            response = make_response(jsonify(response_dict), 200)
            return response
        else:
            response_dict = {
                'error': 'No reviews found for the specified event'
            }
            response = make_response(jsonify(response_dict), 404)
            return response
        
    def post(self, event_id):
        data = request.get_json()
        if data:
            new_review = Review(
                user_id=data['user_id'],
                event_id=event_id,
                rating=data['rating'],
                comment=data['comment'],
            )

            db.session.add(new_review)
            db.session.commit()

            response_dict = serialize_review(new_review)
            response = make_response(jsonify(response_dict), 200)
            return response
        else:
            response_dict = {
                'error': ['validation errors']
            }
            response = make_response(jsonify(response_dict), 400)
            return response

    def delete(self, event_id):
        data = request.get_json()
        if data:
            user_id = data.get('user_id')

            if user_id is not None:
                review_to_delete = Review.query.filter_by(user_id=user_id, event_id=event_id).first()

                if review_to_delete:
                    db.session.delete(review_to_delete)
                    db.session.commit()

                    response_dict = {'message': 'Review deleted successfully'}
                    return make_response(jsonify(response_dict), 200)
                else:
                    response = {'error': 'Review not found'}
                    return response

api.add_resource(ReviewsForEvent, '/event/<int:event_id>/reviews')

# Following routes
class Followings(Resource):
    def get(self):
        all_followings = Following.query.all()
        if all_followings:
            response_dict = [serialize_following(x) for x in all_followings]
            response = make_response(jsonify(response_dict), 200)
            return response
        else:
            response_dict = {
                'error': 'Resources not found'
            }
            response = make_response(jsonify(response_dict), 404)
            return response
        
        

    def post(self):
        data = request.get_json()
        if data:
            new_following = Following(
                user_id=data['user_id'],
                event_id=data['event_id'],
            )

            db.session.add(new_following)
            db.session.commit()

            response_dict = serialize_following(new_following)
            response = make_response(jsonify(response_dict), 200)
            return response
        else:
            response_dict = {
                'error': ['validation errors']
            }
            response = make_response(jsonify(response_dict), 400)
            return response
        

    def delete(self):
        data = request.get_json()
        if data:
            user_id = data.get('user_id')
            event_id = data.get('event_id')

            if user_id is not None and event_id is not None:
                following_to_delete = Following.query.filter_by(user_id=user_id, event_id=event_id).first()

                if following_to_delete:
                    db.session.delete(following_to_delete)
                    db.session.commit()
                    
                    response_dict = {'message': 'Following deleted successfully'}
                    return make_response(jsonify(response_dict), 200)
                else:
                    response = {'error':'Following not found'}
                    return response


api.add_resource(Followings, '/followings')

class FollowingById(Resource):
    def get(self, id):
        following = Following.query.filter_by(id=id).first()
        if following:
            response_dict = serialize_following(following)
            response = make_response(jsonify(response_dict), 200)
            return response
        else:
            response_dict = {
                'error': 'following does not exist'
            }
            response = make_response(jsonify(response_dict), 404)
            return response

    def patch(self, id):
        following = Following.query.filter_by(id=id).first()
        if following:
            data = request.get_json()
            for attr in data:
                setattr(following, attr, data[attr])

            db.session.commit()

            response_dict = serialize_following(following)
            response = make_response(jsonify(response_dict), 200)
            return response
        else:
            response_dict = {
                'error': 'failed to update'
            }
            response = make_response(jsonify(response_dict), 404)
            return response

    def delete(self, id):
        following = Following.query.filter_by(id=id).first()
        if following:
            db.session.delete(following)
            db.session.commit()

            response_dict = {
                'message': 'following successfully deleted'
            }
            response = make_response(jsonify(response_dict), 200)
            return response

api.add_resource(FollowingById, '/following/<int:id>')

class FollowingsForEvent(Resource):
    def get(self, event_id):
        followings = Following.query.filter_by(event_id=event_id).all()

        if followings:
            response_dict = [serialize_following(following) for following in followings]
            response = make_response(jsonify(response_dict), 200)
            return response
        else:
            response_dict = {
                'error': 'No followings found for the specified event'
            }
            response = make_response(jsonify(response_dict), 404)
            return response
        
    def post(self, event_id):
        data = request.get_json()
        if data:
            new_following = Following(
                user_id=data['user_id'],
                event_id=event_id,
            )

            db.session.add(new_following)
            db.session.commit()

            response_dict = serialize_following(new_following)
            response = make_response(jsonify(response_dict), 200)
            return response
        else:
            response_dict = {
                'error': ['validation errors']
            }
            response = make_response(jsonify(response_dict), 400)
            return response

    def delete(self, event_id):
        data = request.get_json()
        if data:
            user_id = data.get('user_id')

            if user_id is not None:
                following_to_delete = Following.query.filter_by(user_id=user_id, event_id=event_id).first()

                if following_to_delete:
                    db.session.delete(following_to_delete)
                    db.session.commit()

                    response_dict = {'message': 'Following deleted successfully'}
                    return make_response(jsonify(response_dict), 200)
                else:
                    response = {'error': 'Following not found'}
                    return response

api.add_resource(FollowingsForEvent, '/event/<int:event_id>/followings')

# Attended routes
class Attendeds(Resource):
    def get(self):
        all_attendeds = Attended.query.all()
        if all_attendeds:
            response_dict = [serialize_attended(x) for x in all_attendeds]
            response = make_response(jsonify(response_dict), 200)
            return response
        else:
            response_dict = {
                'error': 'Resources not found'
            }
            response = make_response(jsonify(response_dict), 404)
            return response

    def post(self):
        data = request.get_json()
        if data:
            new_attended = Attended(
                user_id=data['user_id'],
                event_id=data['event_id'],
            )

            db.session.add(new_attended)
            db.session.commit()

            response_dict = serialize_attended(new_attended)
            response = make_response(jsonify(response_dict), 200)
            return response
        else:
            response_dict = {
                'error': ['validation errors']
            }
            response = make_response(jsonify(response_dict), 400)
            return response

api.add_resource(Attendeds, '/attendeds')

class AttendedById(Resource):
    def get(self, id):
        attended = Attended.query.filter_by(id=id).first()
        if attended:
            response_dict = serialize_attended(attended)
            response = make_response(jsonify(response_dict), 200)
            return response
        else:
            response_dict = {
                'error': 'attended record does not exist'
            }
            response = make_response(jsonify(response_dict), 404)
            return response

    def patch(self, id):
        attended = Attended.query.filter_by(id=id).first()
        if attended:
            data = request.get_json()
            for attr in data:
                setattr(attended, attr, data[attr])

            db.session.commit()

            response_dict = serialize_attended(attended)
            response = make_response(jsonify(response_dict), 200)
            return response
        else:
            response_dict = {
                'error': 'failed to update'
            }
            response = make_response(jsonify(response_dict), 404)
            return response

    def delete(self, id):
        attended = Attended.query.filter_by(id=id).first()
        if attended:
            db.session.delete(attended)
            db.session.commit()

            response_dict = {
                'message': 'attended record successfully deleted'
            }
            response = make_response(jsonify(response_dict), 200)
            return response

api.add_resource(AttendedById, '/attended/<int:id>')






if __name__ == '__main__':
    app.run(port=5555)

# from server import routes


