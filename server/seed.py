from faker import Faker
from models import User, Event, Following ,db
from random import randint
from app import app
from datetime import datetime

fake = Faker()

with app.app_context():

    User.query.delete()
    Event.query.delete()
    Following.query.delete
    # Review.query.delete()
    # Follow.query.delete()
    # Attended.query.delete()


    for _ in range(10):
        user = User(
            username=fake.user_name(),
            password=fake.password(),
            email=fake.email(),
            image=fake.image_url(),
        )
        db.session.add(user)
        

    for _ in range(10):
        event = Event(
            title=fake.word(),
            description=fake.text(),
            date=datetime.strptime(fake.date(), '%Y-%m-%d').date(),
            time=datetime.strptime(fake.time(), '%H:%M:%S').time(),
            location=fake.address(),
            user_id=randint(1, 10),  # Assign a random user_id as the creator
            image=fake.image_url(),
        )
        db.session.add(event)

    pair1 = Following(
        id=1,
        user_id=5,
        event_id=8
        )
    db.session.add(pair1)
    

    # for _ in range(10):
    #     following = Following(
    #         user_id=randint(1,10),
    #         event_id=randint(1,10)
    #     )
    #     db.session.add(following)

    db.session.commit()

    # for _ in range(10):
    #     review = Review(
    #         user_id=randint(1, 10),
    #         event_id=randint(1, 10),
    #         rating=fake.random_element(elements=(1.0, 2.0, 3.0, 4.0, 5.0)),
    #         comment=fake.text(),
    #     )
    #     db.session.add(review)

    # for _ in range(10):
    #     follow = Follow(
    #         user_id=randint(1, 10),
    #         event_id=randint(1, 10),
    #     )
    #     db.session.add(follow)

    # for _ in range(10):
    #     attended = Attended(
    #         user_id=randint(1, 10),
    #         event_id=randint(1, 10),
    #     )
    #     db.session.add(attended)

        
    # db.session.commit()
