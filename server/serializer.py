
def serialize_user(user):
    return{
        'id':user.id,
        'username':user.username,
        'password':user.password,
        'email':user.email,
        'image':user.image,
        'reviews':[serialize_review(review)for review in user.reviews],
        'events_attended':[serialize_attended(attendance)for attendance in user.events_attended],
        'events_followed':[serialize_following(follow)for follow in user.events_followed],
        'created_events':[serialize_event(event)for event in user.created_events],
        'created_at': user.created_at.isoformat(),
        'updated_at': user.updated_at.isoformat()
    }

def serialize_event(event):
    return{
        'id':event.id,
        'title':event.title,
        'image':event.image,
        'description':event.description,
        'date':event.date.strftime('%Y-%m-%d'),
        'time':event.time.strftime('%H:%M:%S'),
        'location':event.location,
        'user_id':event.user_id,
        'event_reviews':[serialize_review(review)for review in event.event_reviews],
        'users_following':[serialize_following(follow)for follow in event.users_following],
        'users_attended':[serialize_attended(attendance)for attendance in event.users_attended],
        'created_at': event.created_at.isoformat(),
        'updated_at': event.updated_at.isoformat()
    }


def serialize_review(review):
    return{
        'id':review.id,
        'user_id':review.user_id,
        'event_id':review.event_id,
        'rating':review.rating,
        'comment':review.comment,
        'created_at': review.created_at.isoformat(),
        'updated_at': review.updated_at.isoformat()
    }

def serialize_following(following):
    return{
        'id':following.id,
        'user_id':following.user_id,
        'event_id':following.event_id
    }

def serialize_attended(attended):
    return{
        'id':attended.id,
        'user_id':attended.user_id,
        'event_id':attended.event_id
    }